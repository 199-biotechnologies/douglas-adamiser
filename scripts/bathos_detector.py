#!/usr/bin/env python3
"""
Detect and analyse bathos patterns in text.

Usage:
    python bathos_detector.py <file>
    python bathos_detector.py <file> --verbose

Outputs a report of all detected bathos patterns with locations and types.
"""

import sys
import re
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional
import argparse


@dataclass
class BathosInstance:
    """A detected instance of bathos."""
    type: str
    pattern: str
    text: str
    position: int
    line_number: int
    score: float  # 1.0 = strong, 0.5 = moderate

    def __str__(self):
        preview = self.text[:80] + "..." if len(self.text) > 80 else self.text
        return f"[{self.type}] Line {self.line_number}: {preview}"


BATHOS_PATTERNS = {
    'brick_simile': {
        'pattern': r'(?:in )?(?:much |very )?(?:the )?same way (?:that |as ).{5,60}(?:don\'t|doesn\'t|can\'t|won\'t|isn\'t|aren\'t|never)',
        'description': 'Inverted simile (the signature Adams pattern)',
        'score': 1.0,
    },
    'philosophical_deflation': {
        'pattern': r'(?:why|what|how|where|when).{10,50}\?[^.]*(?:why|what|how).{10,50}\?[^.]*(?:why|what|how).{5,30}(?:digital watch|tea|towel|sock|lunch|parking)',
        'description': 'Profound questions ending in trivial concern',
        'score': 1.0,
    },
    'answer_bathos': {
        'pattern': r'(?:answer|solution|result|meaning|purpose|point).{0,30}(?:was|is|turned out to be).{0,20}(?:forty-two|\d+|nothing|none|unclear|unknown|"[^"]{1,10}")',
        'description': 'Important answer that explains nothing',
        'score': 0.8,
    },
    'cosmic_mundane': {
        'pattern': r'(?:universe|galaxy|cosmos|infinity|eternity|existence|reality|civilisation|million years).{0,80}(?:tea|towel|biscuit|queue|paperwork|form|appointment|parking|lunch)',
        'description': 'Cosmic scale deflated to mundane concern',
        'score': 1.0,
    },
    'staccato_punch': {
        'pattern': r'[^.]{80,}[.!?]\s+[A-Z][^.]{1,15}\.',
        'description': 'Long buildup followed by very short sentence',
        'score': 0.7,
    },
    'importance_deflation': {
        'pattern': r'(?:important|crucial|vital|essential|critical|momentous|significant|historic).{0,40}(?:wasn\'t|isn\'t|didn\'t|weren\'t|hadn\'t|would.{0,10}matter)',
        'description': 'Statement of importance immediately undercut',
        'score': 0.8,
    },
    'helpful_unhelpful': {
        'pattern': r'(?:which|this) (?:meant|means|is to say|implied).{0,40}(?:nothing|very little|not much|absolutely nothing|precisely nothing)',
        'description': 'Clarification that clarifies nothing',
        'score': 0.9,
    },
    'scale_understatement': {
        'pattern': r'(?:destroy|explode|annihilate|obliterate|end|terminate).{0,40}(?:slightly|somewhat|rather|marginally|a bit|mildly)',
        'description': 'Catastrophe described with understatement',
        'score': 0.8,
    },
    'bureaucratic_horror': {
        'pattern': r'(?:form|document|paperwork|regulation|procedure|committee|department).{0,60}(?:\d+[A-Z]|\d{3,}|seventeen|hundred|thousand|century|centuries)',
        'description': 'Horror administered through bureaucracy',
        'score': 0.7,
    },
    'qualified_absolute': {
        'pattern': r'(?:almost certainly|nearly always|practically never|virtually impossible).{0,30}(?:give or take|plus or minus|more or less|approximately)',
        'description': 'Absolute statement immediately qualified',
        'score': 0.6,
    },
    'redundant_precision': {
        'pattern': r'\d{4,}(?:,\d{3})*(?:\s+(?:and|,)\s+\d+)?(?:\s+to\s+one|\s+percent|\s+years)',
        'description': 'Absurdly precise number for unknowable quantity',
        'score': 0.7,
    },
    'cascade_deflation': {
        'pattern': r'(?:\w+,\s+){3,}\w+,?\s+and\s+(?:slightly|somewhat|rather|mostly|largely)\s+\w+',
        'description': 'Adjective cascade ending in deflation',
        'score': 0.8,
    },
}


def find_line_number(text: str, position: int) -> int:
    """Find line number for a character position."""
    return text[:position].count('\n') + 1


def detect_bathos(text: str) -> List[BathosInstance]:
    """Find all bathos instances in text."""
    instances = []

    for bathos_type, config in BATHOS_PATTERNS.items():
        pattern = config['pattern']
        score = config['score']

        for match in re.finditer(pattern, text, re.IGNORECASE | re.DOTALL):
            instance = BathosInstance(
                type=bathos_type,
                pattern=config['description'],
                text=match.group(0).strip(),
                position=match.start(),
                line_number=find_line_number(text, match.start()),
                score=score
            )
            instances.append(instance)

    # Sort by position
    instances.sort(key=lambda x: x.position)

    return instances


def calculate_bathos_score(instances: List[BathosInstance], word_count: int) -> float:
    """Calculate overall bathos score (0-100)."""
    if word_count == 0:
        return 0.0

    # Weight by instance scores
    total_score = sum(i.score for i in instances)

    # Target: 3 per 500 words = 6 points per 500 words
    target = (word_count / 500) * 6

    # Score as percentage of target (capped at 100)
    return min(100, (total_score / target) * 100) if target > 0 else 0


def print_report(instances: List[BathosInstance], text: str, verbose: bool = False):
    """Print bathos analysis report."""
    word_count = len(text.split())

    print("=" * 60)
    print("BATHOS DETECTION REPORT")
    print("=" * 60)
    print(f"\nWord count: {word_count}")
    print(f"Bathos instances found: {len(instances)}")

    # Group by type
    by_type = {}
    for inst in instances:
        by_type.setdefault(inst.type, []).append(inst)

    print(f"\nBy type:")
    for btype, insts in sorted(by_type.items(), key=lambda x: -len(x[1])):
        desc = BATHOS_PATTERNS[btype]['description']
        print(f"  {btype}: {len(insts)} ({desc})")

    # Calculate score
    score = calculate_bathos_score(instances, word_count)
    print(f"\nBathos Score: {score:.1f}/100")

    if score < 50:
        print("  Status: INSUFFICIENT - Add more anti-climaxes")
    elif score < 80:
        print("  Status: ADEQUATE - Good bathos presence")
    else:
        print("  Status: EXCELLENT - Strong Adams bathos density")

    if verbose and instances:
        print("\n" + "-" * 60)
        print("DETAILED INSTANCES:")
        print("-" * 60)
        for i, inst in enumerate(instances, 1):
            print(f"\n{i}. {inst}")
            print(f"   Type: {inst.pattern}")
            print(f"   Score: {inst.score}")

    # Suggestions if score is low
    if score < 50:
        print("\n" + "-" * 60)
        print("SUGGESTIONS:")
        print("-" * 60)

        missing_types = set(BATHOS_PATTERNS.keys()) - set(by_type.keys())
        if missing_types:
            print("\nMissing bathos types to try:")
            for mtype in list(missing_types)[:3]:
                print(f"  - {mtype}: {BATHOS_PATTERNS[mtype]['description']}")

        print("\nGeneral tips:")
        print("  - Add 'in much the same way that X doesn't' comparisons")
        print("  - Follow long sentences with very short ones")
        print("  - Understate disasters ('somewhat inconvenient')")
        print("  - Mix cosmic scope with mundane concerns (tea, towels)")


def main():
    parser = argparse.ArgumentParser(
        description='Detect bathos patterns in text (Douglas Adams style)'
    )
    parser.add_argument('file', help='File to analyse')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Show detailed instance list')

    args = parser.parse_args()

    filepath = Path(args.file)
    if not filepath.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    text = filepath.read_text(encoding='utf-8')
    instances = detect_bathos(text)
    print_report(instances, text, args.verbose)


if __name__ == '__main__':
    main()
