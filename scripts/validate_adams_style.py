#!/usr/bin/env python3
"""
Validate output against Douglas Adams style standards.

Usage:
    python validate_adams_style.py <output_file>

Returns exit code 0 if all checks pass, 1 if any fail.
"""

import sys
import re
from pathlib import Path
from collections import Counter
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class ValidationResult:
    category: str
    message: str
    severity: str = 'error'  # 'error' or 'warning'

    def __str__(self):
        icon = '✗' if self.severity == 'error' else '⚠'
        return f"{icon} [{self.category}] {self.message}"


def count_words(text: str) -> int:
    """Count words, excluding code blocks and markdown."""
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'[*_`#]', '', text)
    return len(text.split())


def check_bathos_density(text: str) -> List[ValidationResult]:
    """Check for bathos/anti-climax patterns (calibrated to real Adams corpus)."""
    errors = []
    word_count = count_words(text)

    # Bathos indicator patterns
    bathos_patterns = [
        r'in much the same way that.+(?:don\'t|doesn\'t|can\'t|won\'t)',  # Brick simile
        r'(?:and yet|but|however).{0,30}(?:slightly|somewhat|rather|marginally)',  # Scale bathos
        r'(?:the answer|the solution|the result) was.{0,20}(?:forty-two|\d+|nothing|surprisingly mundane)',  # Answer bathos
        r'(?:universe|galaxy|cosmos|existence).{0,50}(?:tea|towel|biscuit|queue|form|paperwork)',  # Cosmic to mundane
        r'\. (?:He|She|It|Arthur|Ford|They) (?:blinked|shrugged|sighed|yawned)\.',  # Staccato deflation
        r'(?:important|crucial|vital|essential).{0,30}(?:wasn\'t|isn\'t|didn\'t)',  # Importance deflation
        r'which (?:was|is) to say.{0,30}(?:nothing|very little|not much)',  # Clarification that doesn't
    ]

    bathos_count = 0
    for pattern in bathos_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
        bathos_count += len(matches)

    # CRITICAL: Staccato deflation is Adams' PRIMARY bathos technique (369 found in corpus)
    # Check for long sentence then very short (his most common pattern)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    for i in range(1, len(sentences)):
        prev_len = len(sentences[i-1].split())
        curr_len = len(sentences[i].split())
        if prev_len > 25 and curr_len <= 8:  # Adjusted thresholds based on corpus
            bathos_count += 1

    # Target: ~1 per 500 words based on corpus analysis (369 staccato in 528k words)
    target = max(1, word_count // 500)

    if bathos_count < target:
        errors.append(ValidationResult(
            'Bathos',
            f'Found {bathos_count} bathos patterns (target: {target} for {word_count} words). '
            f'Add more anti-climaxes.',
            'error' if bathos_count < target // 2 else 'warning'
        ))
    else:
        errors.append(ValidationResult(
            'Bathos',
            f'Found {bathos_count} bathos patterns. Good density.',
            'info'
        ))

    return [e for e in errors if e.severity != 'info']


def check_simile_inversions(text: str) -> List[ValidationResult]:
    """Check for Adams-style inverted comparisons (based on corpus analysis)."""
    errors = []

    # The signature "much the same way that X doesn't" pattern (USE SPARINGLY - only 0.15/10k in corpus)
    brick_pattern = r'(?:much the same way|same way|similar way) that.+(?:don\'t|doesn\'t|can\'t|won\'t|isn\'t|aren\'t)'
    brick_matches = re.findall(brick_pattern, text, re.IGNORECASE)

    # NEW: The "not like X, but like Y" pattern (signature technique from corpus analysis)
    # This is Adams' primary inverted comparison technique
    inverted_pattern = r'not like.{5,50}(?:is|was|were).{5,50}but like.{5,50}(?:is|was|were)'
    inverted_matches = re.findall(inverted_pattern, text, re.IGNORECASE)

    # Also check for simpler "not like X" constructions
    simple_not_like = r'not like (?:a |the |ice |bricks? |water |stone )'
    simple_matches = re.findall(simple_not_like, text, re.IGNORECASE)

    total_inversions = len(brick_matches) + len(inverted_matches) + len(simple_matches)
    word_count = count_words(text)

    # Target: at least 1 per 500 words based on corpus frequency
    target = max(1, word_count // 500)

    if total_inversions < target:
        errors.append(ValidationResult(
            'Inverted Comparison',
            f'Found {total_inversions} inverted comparison(s). Target: {target}. '
            f'Add "not like X, but like Y" patterns (Adams signature technique).',
            'warning'
        ))

    return errors


def check_digression_density(text: str) -> List[ValidationResult]:
    """Check for digression patterns."""
    errors = []
    word_count = count_words(text)

    # Digression indicators
    digression_patterns = [
        r'\([^)]{100,}\)',  # Long parentheticals (100+ chars)
        r'which,? (?:as (?:everyone|anyone|it happens|it turned out|we all) knows?)',  # "as everyone knows"
        r'(?:not to be confused with|for reasons (?:that|which)|although.{20,}is perhaps)',  # Digression entries
        r'(?:but that|though that).{0,30}(?:is another|was another|would be another) story',  # Digression exits
        r'(?:anyway|in any case|regardless|but I digress)',  # Return markers
    ]

    digression_count = 0
    for pattern in digression_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
        digression_count += len(matches)

    # Target: 1 per 300 words
    target = max(1, word_count // 300)

    if digression_count < target:
        errors.append(ValidationResult(
            'Digressions',
            f'Found {digression_count} digression markers (target: {target}). '
            f'Add more tangential asides and parenthetical escapes.',
            'warning'
        ))

    return errors


def check_sentence_rhythm(text: str) -> List[ValidationResult]:
    """Check for sentence length variation."""
    errors = []

    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s for s in sentences if s.strip()]

    if len(sentences) < 5:
        return errors  # Too short to evaluate

    lengths = [len(s.split()) for s in sentences]

    # Check for variety
    has_long = any(l > 35 for l in lengths)
    has_short = any(l <= 5 for l in lengths)
    has_medium = any(15 <= l <= 25 for l in lengths)

    if not has_long:
        errors.append(ValidationResult(
            'Sentence Rhythm',
            'No long sentences (35+ words) found. Adams uses cumulative builds.',
            'warning'
        ))

    if not has_short:
        errors.append(ValidationResult(
            'Sentence Rhythm',
            'No very short sentences (5 words or less). Adams uses staccato punches.',
            'warning'
        ))

    # Check for consecutive same-length sentences
    same_length_streak = 0
    for i in range(1, len(lengths)):
        if abs(lengths[i] - lengths[i-1]) < 5:
            same_length_streak += 1
        else:
            same_length_streak = 0

        if same_length_streak >= 4:
            errors.append(ValidationResult(
                'Sentence Rhythm',
                'Found 4+ consecutive similar-length sentences. Vary rhythm more.',
                'warning'
            ))
            break

    return errors


def check_vocabulary_markers(text: str) -> List[ValidationResult]:
    """Check for Adams-style vocabulary (calibrated to real corpus frequencies)."""
    errors = []

    # CRITICAL: Based on corpus analysis, "quite" and "rather" are Adams' TOP intensifiers
    # "utterly" is often OVERUSED in imitations (only 0.96 per 10k in real Adams)
    # Priority markers ranked by actual Adams usage:
    priority_markers = {
        'quite': 8.13,      # ESSENTIAL - most common
        'rather': 6.73,     # ESSENTIAL - second most common
        'slightly': 3.18,   # HIGH
        'perfectly': 2.86,  # HIGH
        'completely': 2.27, # MEDIUM
        'particularly': 2.10, # MEDIUM
        'entirely': 1.32,   # MEDIUM
        'utterly': 0.96,    # LOW - often overused in imitations!
        'thoroughly': 0.68, # LOW
    }

    text_lower = text.lower()
    found_markers = {}
    for word in priority_markers:
        count = len(re.findall(rf'\b{word}\b', text_lower))
        if count > 0:
            found_markers[word] = count

    total_positive = sum(found_markers.values())
    word_count = count_words(text)

    # Check for essential markers (quite, rather)
    has_quite = 'quite' in found_markers
    has_rather = 'rather' in found_markers

    if not has_quite and not has_rather and word_count > 500:
        errors.append(ValidationResult(
            'Vocabulary',
            'Missing essential Adams intensifiers "quite" or "rather". '
            'These are his TOP markers (8.13 and 6.73 per 10k words in corpus).',
            'warning'
        ))

    # Target based on corpus: ~20 intensifiers per 10k words
    target = max(2, word_count // 500)

    if total_positive < target:
        errors.append(ValidationResult(
            'Vocabulary',
            f'Found {total_positive} signature intensifiers (target: {target}). '
            f'Use more: utterly, thoroughly, rather, somewhat, etc.',
            'warning'
        ))

    # Negative markers (should be avoided)
    american_markers = ['awesome', 'super ', 'totally', 'guys', 'cool']
    american_count = sum(len(re.findall(rf'\b{word}\b', text_lower)) for word in american_markers)

    if american_count > 0:
        errors.append(ValidationResult(
            'Vocabulary',
            f'Found {american_count} American-ism(s) (awesome, super, totally, etc.). '
            f'Replace with British alternatives.',
            'warning'
        ))

    return errors


def check_british_english(text: str) -> List[ValidationResult]:
    """Check for British English usage."""
    errors = []

    american_patterns = [
        (r'\bcolor\b', 'colour'),
        (r'\bfavor\b', 'favour'),
        (r'\bhonor\b', 'honour'),
        (r'\bcenter\b', 'centre'),
        (r'\btheater\b', 'theatre'),
        (r'\banalyze\b', 'analyse'),
        (r'\brealize\b', 'realise'),
        (r'\borganize\b', 'organise'),
        (r'\bgray\b', 'grey'),
        (r'\bapartment\b', 'flat'),
        (r'\belevator\b', 'lift'),
        (r'\btrash\b', 'rubbish'),
        (r'\bgarbage\b', 'rubbish'),
        (r'\bvacation\b', 'holiday'),
        (r'\bcookie\b', 'biscuit'),
    ]

    american_count = 0
    for pattern, british in american_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        american_count += len(matches)

    if american_count > 5:
        errors.append(ValidationResult(
            'British English',
            f'Found ~{american_count} American spellings/words. Use British English.',
            'warning'
        ))

    return errors


def check_cosmic_mundane_juxtaposition(text: str) -> List[ValidationResult]:
    """Check for cosmic/mundane juxtapositions (signature Adams)."""
    errors = []

    cosmic_words = ['universe', 'galaxy', 'cosmos', 'infinity', 'eternity',
                   'existence', 'reality', 'dimension', 'spacetime', 'civilisation']
    mundane_words = ['tea', 'towel', 'biscuit', 'queue', 'paperwork', 'form',
                    'appointment', 'lunch', 'parking', 'umbrella', 'sock']

    text_lower = text.lower()

    has_cosmic = any(word in text_lower for word in cosmic_words)
    has_mundane = any(word in text_lower for word in mundane_words)

    if has_cosmic and not has_mundane:
        errors.append(ValidationResult(
            'Juxtaposition',
            'Found cosmic concepts but no mundane deflations. '
            'Add tea, towels, or bureaucratic concerns.',
            'warning'
        ))

    return errors


def check_deadpan_delivery(text: str) -> List[ValidationResult]:
    """Check for appropriate deadpan tone (not too exclamatory)."""
    errors = []

    # Count exclamation marks (should be rare)
    exclamation_count = text.count('!')
    word_count = count_words(text)

    # More than 1 per 500 words is too many
    if exclamation_count > word_count // 500:
        errors.append(ValidationResult(
            'Tone',
            f'Found {exclamation_count} exclamation marks. Adams uses deadpan delivery. '
            f'Remove most exclamation marks.',
            'warning'
        ))

    # Check for breathless phrases
    breathless = ['amazing!', 'incredible!', 'unbelievable!', 'wow', 'oh my god']
    breathless_count = sum(len(re.findall(rf'\b{phrase}\b', text, re.IGNORECASE))
                         for phrase in breathless)

    if breathless_count > 0:
        errors.append(ValidationResult(
            'Tone',
            f'Found {breathless_count} breathless exclamation(s). '
            f'Adams observes absurdity with resigned amusement, not wonder.',
            'warning'
        ))

    return errors


def check_paragraph_structure(text: str) -> List[ValidationResult]:
    """Check for single-sentence paragraph ratio (~31.9% in real Adams)."""
    errors = []

    # Split into paragraphs
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]

    if len(paragraphs) < 5:
        return errors  # Too short to evaluate

    # Count single-sentence paragraphs
    single_sentence_count = 0
    for para in paragraphs:
        sentences = re.split(r'(?<=[.!?])\s+', para)
        sentences = [s for s in sentences if s.strip()]
        if len(sentences) == 1:
            single_sentence_count += 1

    ratio = single_sentence_count / len(paragraphs) * 100

    # Target: ~31.9% based on corpus analysis
    if ratio < 20:
        errors.append(ValidationResult(
            'Paragraph Structure',
            f'Single-sentence paragraphs: {ratio:.1f}% (target: ~32%). '
            f'Use more short paragraphs for rhythm and punchlines.',
            'warning'
        ))

    return errors


def check_dialogue_tags(text: str) -> List[ValidationResult]:
    """Check dialogue tag distribution (90% 'said' in real Adams)."""
    errors = []

    # Find all dialogue tags
    said_pattern = r'["\']\s*(?:,?\s*)?(?:he|she|it|they|[A-Z][a-z]+)\s+said'
    other_tags = r'["\']\s*(?:,?\s*)?(?:he|she|it|they|[A-Z][a-z]+)\s+(?:shouted|yelled|whispered|muttered|exclaimed|cried|screamed|asked|replied|answered|responded|declared)'

    said_count = len(re.findall(said_pattern, text, re.IGNORECASE))
    other_count = len(re.findall(other_tags, text, re.IGNORECASE))

    total_tags = said_count + other_count

    if total_tags > 5:  # Only check if there's meaningful dialogue
        said_ratio = (said_count / total_tags) * 100 if total_tags > 0 else 0

        if said_ratio < 70:
            errors.append(ValidationResult(
                'Dialogue Tags',
                f'"said" usage: {said_ratio:.0f}% (target: ~90%). '
                f'Adams uses "said" almost exclusively. Reserve other tags for special cases.',
                'warning'
            ))

    return errors


def validate_file(filepath: Path) -> Tuple[List[ValidationResult], List[ValidationResult]]:
    """Run all validation checks."""
    text = filepath.read_text(encoding='utf-8')

    all_checks = [
        check_bathos_density,
        check_simile_inversions,
        check_digression_density,
        check_sentence_rhythm,
        check_paragraph_structure,      # NEW: Single-sentence paragraph ratio
        check_dialogue_tags,            # NEW: Dialogue tag distribution
        check_vocabulary_markers,
        check_british_english,
        check_cosmic_mundane_juxtaposition,
        check_deadpan_delivery,
    ]

    all_results = []
    for check_fn in all_checks:
        all_results.extend(check_fn(text))

    errors = [r for r in all_results if r.severity == 'error']
    warnings = [r for r in all_results if r.severity == 'warning']

    return errors, warnings


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_adams_style.py <output_file>")
        print("\nValidates text against Douglas Adams style standards.")
        print("Checks: bathos density, inverted comparisons, digressions,")
        print("        sentence rhythm, paragraph structure, dialogue tags,")
        print("        vocabulary, British English, cosmic/mundane, tone.")
        sys.exit(1)

    input_path = Path(sys.argv[1])

    if not input_path.exists():
        print(f"Error: File not found: {input_path}")
        sys.exit(1)

    print(f"Validating Adams Style: {input_path}\n")
    print("=" * 50)

    try:
        errors, warnings = validate_file(input_path)
    except Exception as e:
        print(f"Error during validation: {e}")
        sys.exit(1)

    # Report word count
    text = input_path.read_text(encoding='utf-8')
    word_count = count_words(text)
    print(f"Word count: {word_count}\n")

    # Report warnings
    if warnings:
        print(f"⚠ WARNINGS ({len(warnings)}):")
        for warning in warnings:
            print(f"  {warning}")
        print()

    # Report errors
    if errors:
        print(f"✗ ERRORS ({len(errors)}):")
        for error in errors:
            print(f"  {error}")
        print()
        print("Validation FAILED. Address errors and re-run.")
        return 1

    # Success
    print("=" * 50)
    if warnings:
        print(f"✓ Validation PASSED with {len(warnings)} warning(s).")
        print("  Review warnings to improve Adams authenticity.")
    else:
        print("✓ Validation PASSED. All checks passed!")
        print("  The text achieves Douglas Adams style markers.")

    return 0


if __name__ == '__main__':
    sys.exit(main())
