# The Douglas Adamiser

## A Mostly Harmless Guide to Making Any Text Sound Like Douglas Adams Wrote It (When He Almost Certainly Didn't)

In the beginning, there was text. It was formal. It was dry. It was the kind of prose that made readers feel like they were being gently but firmly escorted out of a building by someone who was very sorry but rules were rules.

This was a problem.

The Douglas Adamiser is a Claude Code skill that transforms any piece of writing into something that sounds like Douglas Adams might have written it after three cups of tea, a long bath, and a particularly illuminating conversation with his cat. It does this not through the crude application of random absurdity – which would be rather like trying to make a soufflé by throwing eggs at an oven – but through careful, corpus-validated analysis of what actually made Adams' writing work.

## What It Does

The skill analyses 528,808 words of authentic Adams text across 10 books. This is quite a lot of words. If you laid them all end to end, they would spell something, though probably not anything useful.

From this corpus, the skill learned that:

- Adams used "quite" and "rather" far more than "utterly" (which imitators overuse by a factor of roughly seven)
- 30% of his sentences were short punches of 10 words or fewer
- 31.9% of his paragraphs were single sentences, deployed for maximum impact
- The first instance of bathos could appear anywhere from 30 words to 2,200 words into a piece
- 90% of his dialogue tags were simply "said"

These are facts. They are the kind of facts that separate authentic Adams voice from the sort of pastiche that sounds like someone read The Hitchhiker's Guide once on a train and thought, "How hard can it be?"

Quite hard, as it turns out.

## The Three-Layer Ultrathink System

Most style transfer produces parody. This skill produces something rather better, through a three-layer quality system:

**Layer 1: Style Fidelity Check** – Detects deviations from corpus-validated patterns. Does not fix anything. Merely points and, in its way, judges.

**Layer 2: Technique Refinement** – Applies surgical corrections to flagged issues. Replaces "very" with "quite". Restructures monotonous sentences. Inserts bathos at appropriate moments.

**Layer 3: Meaning Amplification** – This is the important bit. It ensures that every Adams technique doesn't just mimic his style but actually makes the content *stronger*. Decorative absurdity fails this layer. Truth dressed in comedy passes.

The principle is simple: Adams used humour as a precision instrument for truth-telling. The Adamiser does the same, or it does nothing at all.

## Installation

```bash
# Clone to your Claude Code skills directory
git clone https://github.com/199-biotechnologies/douglas-adamiser.git ~/.claude/skills/douglas-adamiser
```

Then simply ask Claude to "Adamise this", "write like Douglas Adams", or "make this absurd" while providing your source text.

## Usage

```
"Adamise this news article about climate change"
"Transform this technical documentation into Hitchhiker's Guide style"
"Make this academic paper sound like Douglas Adams wrote it"
```

The skill will:
1. Analyse your source text
2. Launch parallel specialist agents (Bathos Architect, Metaphor Engineer, Rhythm Analyst, Dialogue Transformer)
3. Synthesise their recommendations
4. Run the three-layer quality review
5. Validate against corpus statistics
6. Return transformed text with a full report

## Project Structure

```
douglas-adamiser/
├── SKILL.md                    # Main skill definition
├── prompts/                    # Agent prompts for multi-layer system
│   ├── orchestrator.md         # Coordinates the whole show
│   ├── bathos_architect.md     # Finds things to deflate
│   ├── metaphor_engineer.md    # Crafts comparisons
│   ├── rhythm_analyst.md       # Ensures proper sentence flow
│   ├── dialogue_transformer.md # Fixes dialogue tags
│   ├── layer1_fidelity_check.md
│   ├── layer2_technique_refinement.md
│   └── layer3_meaning_amplification.md
├── reference/                  # Corpus analysis and style guides
│   ├── literary_analysis.md    # 10-book literary analysis
│   ├── corpus_analysis_summary.md
│   ├── corpus_stats.json
│   └── [style guides...]
├── scripts/                    # Validation tools
│   ├── validate_adams_style.py
│   ├── bathos_detector.py
│   ├── vocabulary_checker.py
│   └── analyse_corpus.py
├── examples/                   # Transformation examples
└── templates/                  # Output templates
```

## The Corpus

The skill was calibrated against:
- The Hitchhiker's Guide to the Galaxy
- The Restaurant at the End of the Universe
- Life, the Universe and Everything
- So Long, and Thanks for All the Fish
- Mostly Harmless
- Dirk Gently's Holistic Detective Agency
- The Long Dark Tea-Time of the Soul
- The Salmon of Doubt
- Last Chance to See
- The Meaning of Liff

This represents essentially everything Adams wrote that wasn't a shopping list, and possibly some things that were.

## A Note on Authenticity

This skill does not claim to replace Douglas Adams. Nothing could. What it does is apply his techniques – the real ones, verified against half a million words of his actual writing – to transform text in ways that honour his approach to comedy and truth.

Adams wrote to expose absurdity in the ordinary, to find cosmic significance in the mundane, and to make philosophy accessible through laughter. The Adamiser attempts to do the same.

Whether it succeeds is, of course, entirely up to you.

## Author

**Boris Djordjevic**

## License

MIT License – which is to say, do what you like with it, just don't blame us when your quarterly report about synergising cross-functional deliverables comes back explaining that the universe is a lot bigger than most people think, and also quite old, and that synergy is what happens when you put two things together and pretend the result is more impressive than either thing was on its own.

---

*"The ships hung in the sky in much the same way that bricks don't."*

*– Douglas Adams (who definitely wrote that bit)*
