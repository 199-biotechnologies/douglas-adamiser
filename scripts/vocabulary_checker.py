#!/usr/bin/env python3
"""
Check vocabulary against Douglas Adams style standards.

Usage:
    python vocabulary_checker.py <file>
    python vocabulary_checker.py <file> --fix  # Suggest replacements

Analyses British English, signature vocabulary, and forbidden words.
"""

import sys
import re
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Tuple
import argparse


@dataclass
class VocabularyIssue:
    """A vocabulary issue found in text."""
    category: str
    word: str
    suggestion: str
    line_number: int
    context: str
    severity: str = 'warning'  # 'error' or 'warning'

    def __str__(self):
        return f"Line {self.line_number}: '{self.word}' → '{self.suggestion}' ({self.category})"


# American to British spelling conversions
AMERICAN_TO_BRITISH = {
    'color': 'colour',
    'colors': 'colours',
    'colored': 'coloured',
    'favor': 'favour',
    'favors': 'favours',
    'favorite': 'favourite',
    'honor': 'honour',
    'honors': 'honours',
    'honored': 'honoured',
    'labor': 'labour',
    'labors': 'labours',
    'neighbor': 'neighbour',
    'neighbors': 'neighbours',
    'center': 'centre',
    'centers': 'centres',
    'centered': 'centred',
    'theater': 'theatre',
    'theaters': 'theatres',
    'fiber': 'fibre',
    'fibers': 'fibres',
    'meter': 'metre',
    'meters': 'metres',
    'liter': 'litre',
    'liters': 'litres',
    'analyze': 'analyse',
    'analyzed': 'analysed',
    'analyzing': 'analysing',
    'realize': 'realise',
    'realized': 'realised',
    'realizing': 'realising',
    'organize': 'organise',
    'organized': 'organised',
    'organizing': 'organising',
    'recognize': 'recognise',
    'recognized': 'recognised',
    'gray': 'grey',
    'grays': 'greys',
    'traveling': 'travelling',
    'traveled': 'travelled',
    'traveler': 'traveller',
    'canceled': 'cancelled',
    'canceling': 'cancelling',
    'program': 'programme',  # except for computer programs
    'programs': 'programmes',
    'defense': 'defence',
    'offense': 'offence',
    'license': 'licence',  # noun
    'practice': 'practise',  # verb
    'airplane': 'aeroplane',
    'airplanes': 'aeroplanes',
    'pajamas': 'pyjamas',
    'jewelry': 'jewellery',
    'catalog': 'catalogue',
    'dialog': 'dialogue',
    'analog': 'analogue',
    'skeptic': 'sceptic',
    'skeptical': 'sceptical',
    'fulfill': 'fulfil',
    'fulfillment': 'fulfilment',
    'skillful': 'skilful',
    'willful': 'wilful',
    'enrollment': 'enrolment',
    'installment': 'instalment',
}

# American vocabulary to British
AMERICAN_VOCAB_TO_BRITISH = {
    'apartment': 'flat',
    'apartments': 'flats',
    'elevator': 'lift',
    'elevators': 'lifts',
    'sidewalk': 'pavement',
    'sidewalks': 'pavements',
    'trash': 'rubbish',
    'garbage': 'rubbish',
    'vacation': 'holiday',
    'vacations': 'holidays',
    'cookie': 'biscuit',
    'cookies': 'biscuits',
    'fries': 'chips',
    'chips': 'crisps',  # context dependent
    'pants': 'trousers',
    'sweater': 'jumper',
    'sneakers': 'trainers',
    'truck': 'lorry',
    'trucks': 'lorries',
    'hood': 'bonnet',  # car
    'trunk': 'boot',  # car
    'gas': 'petrol',
    'gasoline': 'petrol',
    'line': 'queue',  # context dependent
    'subway': 'underground',  # or tube
    'mail': 'post',
    'mailbox': 'postbox',
    'cell phone': 'mobile',
    'cellphone': 'mobile',
    'soccer': 'football',
    'fall': 'autumn',  # season
    'closet': 'wardrobe',
    'diaper': 'nappy',
    'diapers': 'nappies',
    'candy': 'sweets',
    'check': 'cheque',  # money
    'mom': 'mum',
    'mommy': 'mummy',
}

# Words that are too American/casual for Adams
FORBIDDEN_WORDS = {
    'awesome': 'remarkable/splendid',
    'super': 'thoroughly/utterly',
    'totally': 'entirely/completely',
    'guys': 'people/everyone',
    'cool': 'good/fine',
    'yeah': 'yes',
    'gonna': 'going to',
    'wanna': 'want to',
    'gotta': 'got to/have to',
    'kinda': 'rather/somewhat',
    'sorta': 'somewhat/rather',
    'basically': '[often delete]',
    'actually': '[use sparingly]',
    'literally': '[use very sparingly]',
    'incredible': 'remarkable/unexpected',
    'amazing': 'surprising/unusual',
    'insane': 'remarkable/extraordinary',
    'crazy': 'remarkable/unusual',
    'epic': 'considerable/significant',
}

# Signature Adams words to check for presence
ADAMS_VOCABULARY = [
    'utterly', 'thoroughly', 'perfectly', 'entirely',
    'rather', 'somewhat', 'marginally', 'slightly',
    'practically', 'theoretically', 'technically',
    'improbable', 'infinite', 'preposterously',
    'unremarkable', 'unfashionable', 'uncharted',
    'bewildered', 'resigned', 'weary',
]


def find_line_number(text: str, position: int) -> int:
    """Find line number for character position."""
    return text[:position].count('\n') + 1


def get_context(text: str, position: int, word: str) -> str:
    """Get surrounding context for a word."""
    start = max(0, position - 30)
    end = min(len(text), position + len(word) + 30)
    context = text[start:end].replace('\n', ' ')
    if start > 0:
        context = '...' + context
    if end < len(text):
        context = context + '...'
    return context


def check_spelling(text: str) -> List[VocabularyIssue]:
    """Check for American spellings."""
    issues = []

    for american, british in AMERICAN_TO_BRITISH.items():
        pattern = rf'\b{american}\b'
        for match in re.finditer(pattern, text, re.IGNORECASE):
            issues.append(VocabularyIssue(
                category='American Spelling',
                word=match.group(),
                suggestion=british,
                line_number=find_line_number(text, match.start()),
                context=get_context(text, match.start(), match.group()),
            ))

    return issues


def check_vocabulary(text: str) -> List[VocabularyIssue]:
    """Check for American vocabulary."""
    issues = []

    for american, british in AMERICAN_VOCAB_TO_BRITISH.items():
        pattern = rf'\b{american}\b'
        for match in re.finditer(pattern, text, re.IGNORECASE):
            issues.append(VocabularyIssue(
                category='American Vocabulary',
                word=match.group(),
                suggestion=british,
                line_number=find_line_number(text, match.start()),
                context=get_context(text, match.start(), match.group()),
            ))

    return issues


def check_forbidden(text: str) -> List[VocabularyIssue]:
    """Check for forbidden/un-Adams words."""
    issues = []

    for forbidden, suggestion in FORBIDDEN_WORDS.items():
        pattern = rf'\b{forbidden}\b'
        for match in re.finditer(pattern, text, re.IGNORECASE):
            issues.append(VocabularyIssue(
                category='Un-Adams Word',
                word=match.group(),
                suggestion=suggestion,
                line_number=find_line_number(text, match.start()),
                context=get_context(text, match.start(), match.group()),
                severity='warning',
            ))

    return issues


def check_adams_presence(text: str) -> Dict[str, int]:
    """Check for presence of Adams signature vocabulary."""
    text_lower = text.lower()
    presence = {}

    for word in ADAMS_VOCABULARY:
        count = len(re.findall(rf'\b{word}\b', text_lower))
        if count > 0:
            presence[word] = count

    return presence


def apply_fixes(text: str, issues: List[VocabularyIssue]) -> str:
    """Apply suggested fixes to text."""
    # Sort by position (reverse) to avoid offset issues
    sorted_issues = sorted(issues, key=lambda x: -x.line_number)

    lines = text.split('\n')

    for issue in sorted_issues:
        if issue.suggestion.startswith('['):
            continue  # Skip suggestions that are notes

        line_idx = issue.line_number - 1
        if 0 <= line_idx < len(lines):
            # Replace word in line (case-preserving)
            old_word = issue.word
            new_word = issue.suggestion

            # Preserve case
            if old_word.isupper():
                new_word = new_word.upper()
            elif old_word[0].isupper():
                new_word = new_word.capitalize()

            lines[line_idx] = re.sub(
                rf'\b{re.escape(old_word)}\b',
                new_word,
                lines[line_idx],
                count=1
            )

    return '\n'.join(lines)


def print_report(issues: List[VocabularyIssue], adams_presence: Dict[str, int],
                word_count: int, show_fixes: bool = False):
    """Print vocabulary analysis report."""
    print("=" * 60)
    print("VOCABULARY ANALYSIS REPORT")
    print("=" * 60)
    print(f"\nWord count: {word_count}")

    # Group issues by category
    by_category = {}
    for issue in issues:
        by_category.setdefault(issue.category, []).append(issue)

    # Print issues by category
    for category, cat_issues in by_category.items():
        print(f"\n{category} ({len(cat_issues)} issues):")
        for issue in cat_issues[:10]:  # Limit to first 10 per category
            print(f"  {issue}")
        if len(cat_issues) > 10:
            print(f"  ... and {len(cat_issues) - 10} more")

    # Adams vocabulary presence
    print(f"\n{'-' * 60}")
    print("ADAMS SIGNATURE VOCABULARY PRESENT:")
    if adams_presence:
        for word, count in sorted(adams_presence.items(), key=lambda x: -x[1]):
            print(f"  {word}: {count}")
    else:
        print("  None detected! Add: utterly, thoroughly, rather, somewhat, etc.")

    # Calculate score
    spelling_issues = len(by_category.get('American Spelling', []))
    vocab_issues = len(by_category.get('American Vocabulary', []))
    forbidden_issues = len(by_category.get('Un-Adams Word', []))
    adams_score = len(adams_presence)

    total_negative = spelling_issues + vocab_issues + forbidden_issues
    score = max(0, 100 - (total_negative * 2) + (adams_score * 5))
    score = min(100, score)

    print(f"\n{'-' * 60}")
    print(f"VOCABULARY SCORE: {score}/100")

    if score >= 80:
        print("  Status: EXCELLENT - Strong Adams vocabulary")
    elif score >= 60:
        print("  Status: GOOD - Mostly Adams-appropriate")
    elif score >= 40:
        print("  Status: NEEDS WORK - Too many non-Adams elements")
    else:
        print("  Status: POOR - Significant vocabulary revision needed")


def main():
    parser = argparse.ArgumentParser(
        description='Check vocabulary for Douglas Adams style'
    )
    parser.add_argument('file', help='File to analyse')
    parser.add_argument('--fix', action='store_true',
                       help='Output fixed version to stdout')

    args = parser.parse_args()

    filepath = Path(args.file)
    if not filepath.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    text = filepath.read_text(encoding='utf-8')
    word_count = len(text.split())

    # Run all checks
    issues = []
    issues.extend(check_spelling(text))
    issues.extend(check_vocabulary(text))
    issues.extend(check_forbidden(text))

    adams_presence = check_adams_presence(text)

    if args.fix:
        # Apply fixes and output
        fixed_text = apply_fixes(text, issues)
        print(fixed_text)
    else:
        # Print report
        print_report(issues, adams_presence, word_count)

        if issues:
            print(f"\nRun with --fix to see corrected version.")


if __name__ == '__main__':
    main()
