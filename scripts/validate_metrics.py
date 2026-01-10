#!/usr/bin/env python3
"""
Douglas Adamiser - Statistical Validation Script

Handles deterministic metrics that LLMs are unreliable at calculating.
Outputs JSON report for LLM interpretation.

Usage:
    python validate_metrics.py --source source.txt --output output.txt
    python validate_metrics.py --output output.txt  # output-only mode
    python validate_metrics.py --text "inline text to check"
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Optional


# Banned phrases (exact matches, case-insensitive)
BANNED_PHRASES = [
    # Adams-specific (too signature)
    "hung in the air",
    "bricks don't",
    "much the same way that bricks",
    "babel fish",
    "don't panic",
    "infinite improbability",
    "heart of gold",
    "so long and thanks for all the fish",
    "forty-two",
    "42",  # as standalone answer reference
    "vogon",
    "marvin",
    "slartibartfast",
    "magrathea",

    # VERBATIM ADAMS OPENINGS (v0.9.0 - karaoke prevention)
    "far out in the uncharted backwaters",
    "unfashionable end of the western spiral arm",
    "small unregarded yellow sun",
    "utterly insignificant little blue-green planet",
    "ape-descended life forms",
    "still think digital watches are a pretty neat idea",
    "in the beginning the universe was created",
    "this has made a lot of people very angry",
    "been widely regarded as a bad move",
    "the ships hung in the sky",
    "in much the same way that bricks don't",
    "a bowl of petunias",
    "oh no, not again",
    "mostly harmless",  # moved from LIMITED to BANNED

    # Standard Earth cliches
    "deck chairs on the titanic",
    "rearranging deck chairs",
    "elephant in the room",
    "putting lipstick on a pig",
    "lipstick on a pig",
    "low-hanging fruit",
    "boiling frog",
    "tip of the iceberg",
    "silver lining",
    "at the end of the day",
    "think outside the box",
    "move the needle",
    "circle back",
    "deep dive",
    "synergy",
    "take it offline",
    "get buy-in",
    "raise the bar",
    "paradigm shift",
    "leverage",
]

# Limited phrases (track count, max 1 per 2000 words)
LIMITED_PHRASES = [
    "not entirely unlike",
    "thursday",
    "tea",  # Track but don't ban - Adams loved tea
    "towel",
]

# Book report constructions (banned) - v0.9.0 expanded
BOOK_REPORT_PATTERNS = [
    # "The author" patterns
    r"the author (notes|describes|argues|proposes|states|mentions|explains|suggests|writes|observes)",
    r"the writer('s| notes| describes| argues)",

    # "The letter/article/essay" patterns (v0.9.0 - critical addition)
    r"the letter (states|mentions|notes|describes|argues|explains|says)",
    r"the article (states|mentions|notes|describes|argues|explains)",
    r"the essay (states|mentions|notes|describes|argues|explains)",
    r"the text (states|mentions|notes|describes|argues|explains)",
    r"the document (states|mentions|notes|describes|argues|explains)",
    r"the piece (states|mentions|notes|describes|argues|explains)",
    r"the post (states|mentions|notes|describes|argues|explains)",
    r"the blog (states|mentions|notes|describes|argues|explains)",

    # "In the letter/article" patterns
    r"in the (letter|article|essay|text|document|piece|post|original)",
    r"from the (letter|article|essay|text|document|piece|source)",

    # "According to" patterns
    r"according to the (source|author|letter|article|text|original)",

    # "This piece/essay" patterns
    r"this (piece|essay|article|letter|text|document) (explains|describes|argues|states|notes)",

    # Generic attribution patterns
    r"the original (text|letter|article|source)",
    r"as (stated|mentioned|noted|described) in the",
]

# PowerPoint header patterns (v0.9.0 - new detection)
POWERPOINT_HEADER_PATTERNS = [
    r"^[A-Z][A-Z\s]{3,}$",  # ALL CAPS headers like "THE BITTER LESSON"
    r"^#{1,3}\s+[A-Z][A-Z\s:,]{5,}$",  # Markdown headers in ALL CAPS
]


def count_words(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def count_sentences(text: str) -> list[int]:
    """Return list of sentence lengths (word counts)."""
    # Split on sentence-ending punctuation
    sentences = re.split(r'[.!?]+', text)
    lengths = []
    for s in sentences:
        s = s.strip()
        if s:
            lengths.append(len(s.split()))
    return lengths


def analyze_sentence_distribution(lengths: list[int]) -> dict:
    """Analyze sentence length distribution."""
    if not lengths:
        return {"short": 0, "medium": 0, "long": 0, "very_long": 0, "total": 0}

    total = len(lengths)
    short = sum(1 for l in lengths if l <= 10)
    medium = sum(1 for l in lengths if 11 <= l <= 30)
    long_ = sum(1 for l in lengths if 31 <= l <= 50)
    very_long = sum(1 for l in lengths if l > 50)

    return {
        "short": round(short / total * 100, 1),
        "medium": round(medium / total * 100, 1),
        "long": round(long_ / total * 100, 1),
        "very_long": round(very_long / total * 100, 1),
        "total": total,
        "targets": {
            "short": "25-35%",
            "medium": "40-50%",
            "long": "12-18%",
            "very_long": "5-10%"
        }
    }


def count_pattern(text: str, pattern: str, case_insensitive: bool = True) -> int:
    """Count occurrences of a pattern."""
    flags = re.IGNORECASE if case_insensitive else 0
    return len(re.findall(pattern, text, flags))


def find_banned_phrases(text: str) -> list[dict]:
    """Find all banned phrases with locations."""
    found = []
    text_lower = text.lower()

    for phrase in BANNED_PHRASES:
        if phrase.lower() in text_lower:
            # Find approximate line number
            for i, line in enumerate(text.split('\n'), 1):
                if phrase.lower() in line.lower():
                    found.append({
                        "phrase": phrase,
                        "line": i,
                        "type": "banned_phrase",
                        "context": line.strip()[:100]
                    })
                    break
            else:
                found.append({"phrase": phrase, "line": "unknown", "type": "banned_phrase"})

    # Check book report patterns
    for pattern in BOOK_REPORT_PATTERNS:
        # Use finditer to get full match objects, not just groups
        for match in re.finditer(pattern, text, re.IGNORECASE):
            full_match = match.group(0)  # Get the entire matched string
            # Find line number
            line_num = text[:match.start()].count('\n') + 1
            found.append({
                "phrase": full_match,
                "type": "book_report_construction",
                "line": line_num
            })

    # Check PowerPoint header patterns (v0.9.0)
    for i, line in enumerate(text.split('\n'), 1):
        line_stripped = line.strip()
        for pattern in POWERPOINT_HEADER_PATTERNS:
            if re.match(pattern, line_stripped):
                # Exclude legitimate short headers
                if len(line_stripped) > 4 and line_stripped not in ["THE", "AND", "BUT"]:
                    found.append({
                        "phrase": line_stripped,
                        "type": "powerpoint_header",
                        "line": i,
                        "fix": "Replace with narrative bridge: 'This leads us to...'"
                    })

    return found


def count_limited_phrases(text: str) -> dict:
    """Count limited-use phrases."""
    result = {}
    for phrase in LIMITED_PHRASES:
        count = count_pattern(text, re.escape(phrase))
        if count > 0:
            result[phrase] = count
    return result


def validate_length_ratio(source_words: int, output_words: int) -> dict:
    """Validate output is within 60-115% of source."""
    if source_words == 0:
        return {"status": "NO_SOURCE", "ratio": None}

    ratio = output_words / source_words * 100

    if ratio < 60:
        status = "TOO_SHORT"
    elif ratio > 115:
        status = "TOO_LONG"
    else:
        status = "PASS"

    return {
        "status": status,
        "ratio": round(ratio, 1),
        "source_words": source_words,
        "output_words": output_words,
        "min_target": round(source_words * 0.60),
        "max_target": round(source_words * 1.15),
    }


def analyze_text(text: str, source_text: Optional[str] = None) -> dict:
    """Full analysis of transformed text."""
    word_count = count_words(text)
    sentence_lengths = count_sentences(text)

    # Core metrics
    result = {
        "word_count": word_count,
        "sentence_count": len(sentence_lengths),
        "sentence_distribution": analyze_sentence_distribution(sentence_lengths),
    }

    # Length validation (if source provided)
    if source_text:
        source_words = count_words(source_text)
        result["length_validation"] = validate_length_ratio(source_words, word_count)

    # Deadpan markers
    in_fact_count = count_pattern(text, r'\bin fact\b')
    of_course_count = count_pattern(text, r'\bof course\b')
    result["deadpan_markers"] = {
        "in_fact": in_fact_count,
        "of_course": of_course_count,
        "total": in_fact_count + of_course_count,
        "target": f"1+ per 2000 words ({word_count // 2000 + 1}+ for this text)",
        "status": "PASS" if (in_fact_count + of_course_count) >= max(1, word_count // 2000) else "NEEDS_MORE"
    }

    # Exclamation marks
    exclamation_count = text.count('!')
    result["exclamation_marks"] = {
        "count": exclamation_count,
        "target": f"<{max(1, word_count // 2000)} for this text",
        "status": "PASS" if exclamation_count < max(1, word_count // 2000) else "TOO_MANY"
    }

    # Question frequency
    question_count = text.count('?')
    questions_per_1000 = round(question_count / word_count * 1000, 1) if word_count > 0 else 0
    result["questions"] = {
        "count": question_count,
        "per_1000_words": questions_per_1000,
        "target": "8-10 per 1000 words",
        "status": "PASS" if 5 <= questions_per_1000 <= 15 else "OUTSIDE_RANGE"
    }

    # Intensifier check
    quite_count = count_pattern(text, r'\bquite\b')
    rather_count = count_pattern(text, r'\brather\b')
    utterly_count = count_pattern(text, r'\butterly\b')
    result["intensifiers"] = {
        "quite": quite_count,
        "rather": rather_count,
        "utterly": utterly_count,
        "quite_rather_total": quite_count + rather_count,
        "status": "PASS" if utterly_count <= max(1, word_count // 1000) else "UTTERLY_OVERUSED"
    }

    # Banned phrases
    banned = find_banned_phrases(text)
    result["banned_phrases"] = {
        "found": banned,
        "count": len(banned),
        "status": "PASS" if len(banned) == 0 else "VIOLATIONS_FOUND"
    }

    # Limited phrases
    limited = count_limited_phrases(text)
    result["limited_phrases"] = limited

    # Single-sentence paragraphs
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    single_sentence_paras = sum(1 for p in paragraphs if len(re.split(r'[.!?]+', p.strip())) <= 2)
    para_ratio = round(single_sentence_paras / len(paragraphs) * 100, 1) if paragraphs else 0
    result["paragraph_structure"] = {
        "total_paragraphs": len(paragraphs),
        "single_sentence_paragraphs": single_sentence_paras,
        "percentage": para_ratio,
        "target": "25-35%",
        "status": "PASS" if 20 <= para_ratio <= 45 else "OUTSIDE_RANGE"
    }

    # Overall status
    failures = []
    if result.get("length_validation", {}).get("status") == "TOO_SHORT":
        failures.append("LENGTH_TOO_SHORT")
    if result["deadpan_markers"]["status"] != "PASS":
        failures.append("MISSING_DEADPAN_MARKERS")
    if result["exclamation_marks"]["status"] != "PASS":
        failures.append("TOO_MANY_EXCLAMATION_MARKS")
    if result["banned_phrases"]["status"] != "PASS":
        failures.append("BANNED_PHRASES_FOUND")
    if result["intensifiers"]["status"] != "PASS":
        failures.append("UTTERLY_OVERUSED")

    result["overall"] = {
        "status": "PASS" if not failures else "NEEDS_ATTENTION",
        "failures": failures,
        "failure_count": len(failures)
    }

    return result


def main():
    parser = argparse.ArgumentParser(description="Validate Douglas Adams style metrics")
    parser.add_argument("--source", "-s", help="Source text file (original)")
    parser.add_argument("--output", "-o", help="Output text file (transformed)")
    parser.add_argument("--text", "-t", help="Inline text to check")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON only")

    args = parser.parse_args()

    # Get output text
    if args.text:
        output_text = args.text
    elif args.output:
        output_text = Path(args.output).read_text()
    else:
        print("Error: Must provide --output file or --text", file=sys.stderr)
        sys.exit(1)

    # Get source text (optional)
    source_text = None
    if args.source:
        source_text = Path(args.source).read_text()

    # Analyze
    result = analyze_text(output_text, source_text)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        # Pretty print
        print("\n" + "=" * 60)
        print("DOUGLAS ADAMISER - VALIDATION REPORT")
        print("=" * 60)

        print(f"\nWord Count: {result['word_count']}")
        print(f"Sentences: {result['sentence_count']}")

        if "length_validation" in result:
            lv = result["length_validation"]
            status_icon = "✓" if lv["status"] == "PASS" else "✗"
            print(f"\n{status_icon} Length Ratio: {lv['ratio']}% (target: 60-115%)")
            print(f"  Source: {lv['source_words']} words → Output: {lv['output_words']} words")

        sd = result["sentence_distribution"]
        print(f"\nSentence Distribution:")
        print(f"  Short (≤10):    {sd['short']}% (target: {sd['targets']['short']})")
        print(f"  Medium (11-30): {sd['medium']}% (target: {sd['targets']['medium']})")
        print(f"  Long (31-50):   {sd['long']}% (target: {sd['targets']['long']})")
        print(f"  Very Long (>50): {sd['very_long']}% (target: {sd['targets']['very_long']})")

        dm = result["deadpan_markers"]
        status_icon = "✓" if dm["status"] == "PASS" else "✗"
        print(f"\n{status_icon} Deadpan Markers: {dm['total']} found")
        print(f"  'in fact': {dm['in_fact']}, 'of course': {dm['of_course']}")

        em = result["exclamation_marks"]
        status_icon = "✓" if em["status"] == "PASS" else "✗"
        print(f"\n{status_icon} Exclamation Marks: {em['count']} (target: {em['target']})")

        q = result["questions"]
        status_icon = "✓" if q["status"] == "PASS" else "✗"
        print(f"\n{status_icon} Questions: {q['per_1000_words']}/1000 words (target: {q['target']})")

        i = result["intensifiers"]
        status_icon = "✓" if i["status"] == "PASS" else "✗"
        print(f"\n{status_icon} Intensifiers:")
        print(f"  'quite': {i['quite']}, 'rather': {i['rather']}, 'utterly': {i['utterly']}")

        bp = result["banned_phrases"]
        status_icon = "✓" if bp["status"] == "PASS" else "✗"
        print(f"\n{status_icon} Banned Phrases: {bp['count']} found")
        if bp["found"]:
            for item in bp["found"]:
                print(f"  - \"{item['phrase']}\" (line {item.get('line', '?')})")

        ps = result["paragraph_structure"]
        status_icon = "✓" if ps["status"] == "PASS" else "✗"
        print(f"\n{status_icon} Single-Sentence Paragraphs: {ps['percentage']}% (target: {ps['target']})")

        print("\n" + "-" * 60)
        o = result["overall"]
        if o["status"] == "PASS":
            print("OVERALL: ✓ PASS")
        else:
            print(f"OVERALL: ✗ {len(o['failures'])} issue(s) to fix")
            for f in o["failures"]:
                print(f"  - {f}")
        print("=" * 60 + "\n")

    # Exit with status
    sys.exit(0 if result["overall"]["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
