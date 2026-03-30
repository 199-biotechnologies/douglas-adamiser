# Contributing to The Douglas Adamiser

First: thank you. The fact that you want to contribute to a tool that transforms text into Douglas Adams' style suggests you are a person of excellent taste, or at least a person who has read the right books, which amounts to the same thing.

## How to Contribute

### Reporting Issues

If the Adamiser produces output that sounds more like a Vogon poetry recital than Douglas Adams, please open an issue with:

- The input text (or a representative sample)
- The output that made you wince
- What you expected instead
- Which specific Adams technique was misapplied

### Improving the Corpus Analysis

The skill is calibrated against 528,808 words from 10 Adams books. If you've identified a pattern we've missed, or a statistic that needs correction:

1. Reference the specific book and passage
2. Show your methodology
3. Include before/after examples of how this changes the output

### Adding Prompts or Reference Material

New agent prompts, reference guides, or templates are welcome. Please ensure they:

- Follow the existing format in `prompts/` or `reference/`
- Include corpus-backed evidence (not vibes)
- Have been tested against at least 3 different input types
- Do not introduce banned Adams tropes (see `prompts/anti_cliche_layer.md`)

### Improving Validation Scripts

Scripts in `scripts/` are Python. When modifying:

- Maintain backward compatibility with existing CLI flags
- Add tests for new validation rules
- Document threshold values and their corpus sources

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/better-bathos-detection`)
3. Make your changes
4. Run the validation suite against the examples in `examples/`
5. Submit a PR with a clear description of what changed and why

## Code of Conduct

Be kind. Be constructive. Remember that Adams himself was, by all accounts, a thoroughly decent person who was very patient with people, even when they asked him about the meaning of 42 for the ten thousandth time.

## Style Guide for Contributions

When writing documentation or comments for this project, you are not required to write in Adams' style. In fact, please don't -- clear technical writing is more useful than clever technical writing, and Adams himself would have been the first to agree.

When writing *about* Adams' techniques, however, precision matters. "He was funny" is not useful. "He used bathos at variable intervals, with first placement ranging from 30 to 2,200 words" is useful.

## Questions?

Open an issue. We don't bite, and we almost certainly won't read you poetry.
