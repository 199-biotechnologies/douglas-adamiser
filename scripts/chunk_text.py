#!/usr/bin/env python3
"""
Douglas Adamiser - Text Chunking Script

Splits long texts into ~3000-word chunks at natural breaks.
For use with parallel agent processing of very long texts (>10k words).

Usage:
    python chunk_text.py --input long_text.txt --output-dir chunks/
    python chunk_text.py --input long_text.txt --chunk-size 5000
"""

import argparse
import json
import re
import sys
from pathlib import Path


def count_words(text: str) -> int:
    """Count words in text."""
    return len(text.split())


def find_break_point(text: str, target_pos: int, window: int = 500) -> int:
    """
    Find a natural break point near target_pos.
    Prefers: section breaks > paragraph breaks > sentence breaks
    """
    start = max(0, target_pos - window)
    end = min(len(text), target_pos + window)
    search_area = text[start:end]

    # Look for section breaks (double newline with heading patterns)
    section_breaks = list(re.finditer(r'\n\n(?=[A-Z#])', search_area))
    if section_breaks:
        # Find closest to middle of search area
        mid = len(search_area) // 2
        best = min(section_breaks, key=lambda m: abs(m.start() - mid))
        return start + best.start()

    # Look for paragraph breaks (double newline)
    para_breaks = list(re.finditer(r'\n\n', search_area))
    if para_breaks:
        mid = len(search_area) // 2
        best = min(para_breaks, key=lambda m: abs(m.start() - mid))
        return start + best.start()

    # Look for sentence breaks
    sentence_breaks = list(re.finditer(r'[.!?]\s+', search_area))
    if sentence_breaks:
        mid = len(search_area) // 2
        best = min(sentence_breaks, key=lambda m: abs(m.start() - mid))
        return start + best.end()

    # Fallback: just use target position
    return target_pos


def chunk_text(text: str, target_chunk_words: int = 3000) -> list[dict]:
    """
    Split text into chunks of approximately target_chunk_words.
    Returns list of chunk dicts with text, word count, and position info.
    """
    total_words = count_words(text)

    if total_words <= target_chunk_words:
        return [{
            "chunk_number": 1,
            "total_chunks": 1,
            "text": text,
            "word_count": total_words,
            "start_word": 0,
            "end_word": total_words
        }]

    # Estimate characters per word for position calculation
    chars_per_word = len(text) / total_words
    target_chunk_chars = int(target_chunk_words * chars_per_word)

    chunks = []
    current_pos = 0
    chunk_num = 1

    while current_pos < len(text):
        # Calculate target end position
        target_end = current_pos + target_chunk_chars

        if target_end >= len(text):
            # Last chunk - take everything remaining
            chunk_text = text[current_pos:].strip()
            if chunk_text:
                chunks.append({
                    "chunk_number": chunk_num,
                    "text": chunk_text,
                    "word_count": count_words(chunk_text),
                })
            break

        # Find natural break point
        break_pos = find_break_point(text, target_end)

        # Extract chunk
        chunk_text = text[current_pos:break_pos].strip()
        if chunk_text:
            chunks.append({
                "chunk_number": chunk_num,
                "text": chunk_text,
                "word_count": count_words(chunk_text),
            })
            chunk_num += 1

        current_pos = break_pos

        # Skip whitespace
        while current_pos < len(text) and text[current_pos] in '\n\r\t ':
            current_pos += 1

    # Add total_chunks to each
    total = len(chunks)
    for chunk in chunks:
        chunk["total_chunks"] = total

    return chunks


def main():
    parser = argparse.ArgumentParser(description="Split long text into chunks for parallel processing")
    parser.add_argument("--input", "-i", required=True, help="Input text file")
    parser.add_argument("--output-dir", "-o", help="Output directory for chunk files")
    parser.add_argument("--chunk-size", "-c", type=int, default=3000, help="Target words per chunk (default: 3000)")
    parser.add_argument("--json", "-j", action="store_true", help="Output chunk info as JSON")
    parser.add_argument("--threshold", "-t", type=int, default=10000, help="Only chunk if above this word count (default: 10000)")

    args = parser.parse_args()

    # Read input
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: File not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    text = input_path.read_text()
    total_words = count_words(text)

    print(f"Input: {input_path.name}")
    print(f"Total words: {total_words}")
    print(f"Threshold: {args.threshold} words")

    if total_words <= args.threshold:
        print(f"\nText is under threshold ({total_words} <= {args.threshold}). No chunking needed.")
        if args.json:
            print(json.dumps({"needs_chunking": False, "total_words": total_words}))
        sys.exit(0)

    # Chunk the text
    chunks = chunk_text(text, args.chunk_size)

    print(f"\nChunked into {len(chunks)} parts:")
    for chunk in chunks:
        print(f"  Chunk {chunk['chunk_number']}: {chunk['word_count']} words")

    # Output
    if args.output_dir:
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        manifest = {
            "source_file": str(input_path),
            "total_words": total_words,
            "chunk_size_target": args.chunk_size,
            "chunks": []
        }

        for chunk in chunks:
            filename = f"chunk_{chunk['chunk_number']:02d}.txt"
            filepath = output_dir / filename
            filepath.write_text(chunk["text"])

            manifest["chunks"].append({
                "chunk_number": chunk["chunk_number"],
                "filename": filename,
                "word_count": chunk["word_count"]
            })

            print(f"  Written: {filepath}")

        # Write manifest
        manifest_path = output_dir / "manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2))
        print(f"  Manifest: {manifest_path}")

    if args.json:
        output = {
            "needs_chunking": True,
            "total_words": total_words,
            "num_chunks": len(chunks),
            "chunks": [{"chunk_number": c["chunk_number"], "word_count": c["word_count"]} for c in chunks]
        }
        print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
