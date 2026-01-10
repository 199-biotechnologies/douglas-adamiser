#!/usr/bin/env python3
"""
Analyse Douglas Adams corpus to extract style patterns and statistics.

Usage:
    python analyse_corpus.py <directory_with_markdown_files>
    python analyse_corpus.py <directory> --output <stats_file.json>

Extracts:
- Vocabulary frequency (signature words)
- Sentence length distribution
- Phrase pattern frequencies
- Bathos indicator frequencies
- Paragraph structure statistics
"""

import sys
import re
import json
from pathlib import Path
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple
import argparse


@dataclass
class CorpusStats:
    """Statistics extracted from Adams corpus."""
    total_words: int
    total_sentences: int
    total_paragraphs: int

    # Sentence length distribution
    sentence_length_avg: float
    sentence_length_median: float
    sentence_length_min: int
    sentence_length_max: int
    short_sentences_pct: float  # <= 10 words
    medium_sentences_pct: float  # 11-30 words
    long_sentences_pct: float  # 31-50 words
    very_long_sentences_pct: float  # > 50 words

    # Vocabulary
    top_intensifiers: Dict[str, int]
    top_adjectives: Dict[str, int]
    signature_phrases: Dict[str, int]

    # Bathos indicators
    bathos_patterns_found: Dict[str, int]

    # Structural patterns
    parenthetical_density: float  # parentheticals per 1000 words
    em_dash_density: float  # em-dashes per 1000 words
    question_density: float  # questions per 1000 words


def clean_text(text: str) -> str:
    """Remove markdown formatting and clean text."""
    # Remove code blocks
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    # Remove markdown links
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    # Remove images
    text = re.sub(r'!\[[^\]]*\]\([^)]+\)', '', text)
    # Remove headers
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    # Remove emphasis markers but keep text
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    text = re.sub(r'_([^_]+)_', r'\1', text)
    # Normalise whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text


def extract_sentences(text: str) -> List[str]:
    """Extract sentences from text."""
    # Split on sentence-ending punctuation
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)
    # Filter out empty and very short
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
    return sentences


def extract_paragraphs(text: str) -> List[str]:
    """Extract paragraphs from text."""
    paragraphs = re.split(r'\n\n+', text)
    paragraphs = [p.strip() for p in paragraphs if len(p.strip()) > 20]
    return paragraphs


def count_words(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def analyse_sentence_lengths(sentences: List[str]) -> Dict:
    """Analyse sentence length distribution."""
    lengths = [len(s.split()) for s in sentences]

    if not lengths:
        return {}

    lengths.sort()
    n = len(lengths)

    return {
        'avg': sum(lengths) / n,
        'median': lengths[n // 2],
        'min': min(lengths),
        'max': max(lengths),
        'short_pct': len([l for l in lengths if l <= 10]) / n * 100,
        'medium_pct': len([l for l in lengths if 11 <= l <= 30]) / n * 100,
        'long_pct': len([l for l in lengths if 31 <= l <= 50]) / n * 100,
        'very_long_pct': len([l for l in lengths if l > 50]) / n * 100,
    }


def extract_intensifiers(text: str) -> Counter:
    """Extract and count intensifier usage."""
    intensifiers = [
        'utterly', 'thoroughly', 'perfectly', 'entirely', 'completely',
        'absolutely', 'rather', 'somewhat', 'marginally', 'slightly',
        'practically', 'theoretically', 'technically', 'virtually',
        'fairly', 'quite', 'remarkably', 'incredibly', 'extraordinarily',
        'particularly', 'especially', 'extremely', 'highly', 'deeply',
    ]

    text_lower = text.lower()
    counts = Counter()

    for word in intensifiers:
        count = len(re.findall(rf'\b{word}\b', text_lower))
        if count > 0:
            counts[word] = count

    return counts


def extract_adjectives(text: str) -> Counter:
    """Extract common adjectives (simplified approach)."""
    # Common adjectives Adams uses
    adjectives = [
        'improbable', 'infinite', 'vast', 'enormous', 'tiny', 'small',
        'large', 'great', 'terrible', 'wonderful', 'remarkable', 'ordinary',
        'extraordinary', 'unusual', 'strange', 'peculiar', 'odd', 'normal',
        'simple', 'complex', 'ancient', 'modern', 'old', 'new', 'dark',
        'bright', 'cold', 'warm', 'wet', 'dry', 'happy', 'sad', 'angry',
        'calm', 'quiet', 'loud', 'fast', 'slow', 'heavy', 'light',
        'beautiful', 'ugly', 'stupid', 'intelligent', 'wise', 'foolish',
        'important', 'trivial', 'significant', 'meaningless', 'pointless',
        'useful', 'useless', 'dangerous', 'safe', 'deadly', 'harmless',
        'unfashionable', 'uncharted', 'unregarded', 'insignificant',
        'bewildered', 'confused', 'resigned', 'weary', 'tired',
    ]

    text_lower = text.lower()
    counts = Counter()

    for word in adjectives:
        count = len(re.findall(rf'\b{word}\b', text_lower))
        if count > 0:
            counts[word] = count

    return counts


def extract_signature_phrases(text: str) -> Counter:
    """Extract Adams signature phrase patterns."""
    patterns = {
        'much the same way': r'(?:much |very )?(?:the )?same way (?:that |as )',
        'as everyone knows': r'as (?:everyone|anyone|it happens|we all) knows?',
        'of course': r'\bof course\b',
        'in fact': r'\bin fact\b',
        'it turned out': r'(?:it |as it )turned out',
        'or rather': r'\bor rather\b',
        'which is to say': r'which (?:is|was) to say',
        'not to mention': r'not to mention',
        'give or take': r'give or take',
        'more or less': r'more or less',
        'in other words': r'in other words',
        'for reasons': r'for reasons (?:that|which)',
        'the fact that': r'the fact that',
        'at least': r'\bat least\b',
        'at most': r'\bat most\b',
        'after all': r'\bafter all\b',
    }

    counts = Counter()
    text_lower = text.lower()

    for name, pattern in patterns.items():
        count = len(re.findall(pattern, text_lower))
        if count > 0:
            counts[name] = count

    return counts


def extract_bathos_indicators(text: str) -> Counter:
    """Count bathos pattern indicators."""
    patterns = {
        'brick_simile': r'same way.{5,40}(?:don\'t|doesn\'t|can\'t|won\'t)',
        'staccato_deflation': r'[^.]{60,}[.!?]\s+[A-Z][^.]{1,12}\.',
        'cosmic_mundane': r'(?:universe|galaxy|infinity).{0,60}(?:tea|towel|paperwork)',
        'importance_undercut': r'(?:important|crucial|vital).{0,30}(?:wasn\'t|isn\'t|didn\'t)',
        'helpful_unhelpful': r'which (?:meant|means).{0,30}(?:nothing|very little)',
        'qualified_absolute': r'(?:almost certainly|nearly always).{0,20}(?:give or take|plus or minus)',
    }

    counts = Counter()

    for name, pattern in patterns.items():
        count = len(re.findall(pattern, text, re.IGNORECASE | re.DOTALL))
        if count > 0:
            counts[name] = count

    return counts


def calculate_densities(text: str) -> Dict[str, float]:
    """Calculate structural element densities per 1000 words."""
    word_count = count_words(text)
    if word_count == 0:
        return {}

    per_1000 = 1000 / word_count

    # Count parentheticals
    parentheticals = len(re.findall(r'\([^)]+\)', text))

    # Count em-dashes (various representations)
    em_dashes = text.count('—') + text.count('--') + text.count(' – ')

    # Count questions
    questions = text.count('?')

    return {
        'parenthetical_density': parentheticals * per_1000,
        'em_dash_density': em_dashes * per_1000,
        'question_density': questions * per_1000,
    }


def analyse_corpus(directory: Path) -> CorpusStats:
    """Analyse all markdown files in directory."""
    all_text = ""

    for md_file in directory.glob("*.md"):
        text = md_file.read_text(encoding='utf-8', errors='ignore')
        text = clean_text(text)
        all_text += text + "\n\n"

    if not all_text.strip():
        raise ValueError("No text found in markdown files")

    # Basic counts
    sentences = extract_sentences(all_text)
    paragraphs = extract_paragraphs(all_text)
    word_count = count_words(all_text)

    # Sentence analysis
    sent_stats = analyse_sentence_lengths(sentences)

    # Vocabulary analysis
    intensifiers = extract_intensifiers(all_text)
    adjectives = extract_adjectives(all_text)
    phrases = extract_signature_phrases(all_text)

    # Bathos analysis
    bathos = extract_bathos_indicators(all_text)

    # Density analysis
    densities = calculate_densities(all_text)

    return CorpusStats(
        total_words=word_count,
        total_sentences=len(sentences),
        total_paragraphs=len(paragraphs),
        sentence_length_avg=sent_stats.get('avg', 0),
        sentence_length_median=sent_stats.get('median', 0),
        sentence_length_min=sent_stats.get('min', 0),
        sentence_length_max=sent_stats.get('max', 0),
        short_sentences_pct=sent_stats.get('short_pct', 0),
        medium_sentences_pct=sent_stats.get('medium_pct', 0),
        long_sentences_pct=sent_stats.get('long_pct', 0),
        very_long_sentences_pct=sent_stats.get('very_long_pct', 0),
        top_intensifiers=dict(intensifiers.most_common(15)),
        top_adjectives=dict(adjectives.most_common(20)),
        signature_phrases=dict(phrases.most_common(15)),
        bathos_patterns_found=dict(bathos),
        parenthetical_density=densities.get('parenthetical_density', 0),
        em_dash_density=densities.get('em_dash_density', 0),
        question_density=densities.get('question_density', 0),
    )


def print_report(stats: CorpusStats):
    """Print analysis report."""
    print("=" * 60)
    print("DOUGLAS ADAMS CORPUS ANALYSIS")
    print("=" * 60)

    print(f"\n📊 BASIC STATISTICS")
    print(f"  Total words: {stats.total_words:,}")
    print(f"  Total sentences: {stats.total_sentences:,}")
    print(f"  Total paragraphs: {stats.total_paragraphs:,}")

    print(f"\n📏 SENTENCE LENGTH DISTRIBUTION")
    print(f"  Average: {stats.sentence_length_avg:.1f} words")
    print(f"  Median: {stats.sentence_length_median:.0f} words")
    print(f"  Range: {stats.sentence_length_min} - {stats.sentence_length_max} words")
    print(f"  Short (≤10 words): {stats.short_sentences_pct:.1f}%")
    print(f"  Medium (11-30): {stats.medium_sentences_pct:.1f}%")
    print(f"  Long (31-50): {stats.long_sentences_pct:.1f}%")
    print(f"  Very long (>50): {stats.very_long_sentences_pct:.1f}%")

    print(f"\n🔤 TOP INTENSIFIERS")
    for word, count in stats.top_intensifiers.items():
        per_10k = count / stats.total_words * 10000
        print(f"  {word}: {count} ({per_10k:.2f} per 10k words)")

    print(f"\n📝 TOP ADJECTIVES")
    for word, count in list(stats.top_adjectives.items())[:10]:
        per_10k = count / stats.total_words * 10000
        print(f"  {word}: {count} ({per_10k:.2f} per 10k words)")

    print(f"\n💬 SIGNATURE PHRASES")
    for phrase, count in stats.signature_phrases.items():
        per_10k = count / stats.total_words * 10000
        print(f"  '{phrase}': {count} ({per_10k:.2f} per 10k words)")

    print(f"\n🎭 BATHOS PATTERN INDICATORS")
    for pattern, count in stats.bathos_patterns_found.items():
        print(f"  {pattern}: {count}")

    print(f"\n📐 STRUCTURAL DENSITIES (per 1000 words)")
    print(f"  Parentheticals: {stats.parenthetical_density:.2f}")
    print(f"  Em-dashes: {stats.em_dash_density:.2f}")
    print(f"  Questions: {stats.question_density:.2f}")


def main():
    parser = argparse.ArgumentParser(
        description='Analyse Douglas Adams corpus for style patterns'
    )
    parser.add_argument('directory', help='Directory containing markdown files')
    parser.add_argument('--output', '-o', help='Output JSON file for stats')

    args = parser.parse_args()

    directory = Path(args.directory)
    if not directory.exists():
        print(f"Error: Directory not found: {directory}")
        sys.exit(1)

    print(f"Analysing corpus in: {directory}\n")

    try:
        stats = analyse_corpus(directory)
    except Exception as e:
        print(f"Error during analysis: {e}")
        sys.exit(1)

    print_report(stats)

    if args.output:
        output_path = Path(args.output)
        with open(output_path, 'w') as f:
            json.dump(asdict(stats), f, indent=2)
        print(f"\n✓ Statistics saved to: {output_path}")


if __name__ == '__main__':
    main()
