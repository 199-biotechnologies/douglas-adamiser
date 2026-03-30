<div align="center">

# The Douglas Adamiser

### A Claude Code skill that makes any text sound like Douglas Adams wrote it. He didn't. But now it does.

<br>

[![Star this repo](https://img.shields.io/github/stars/199-biotechnologies/douglas-adamiser?style=for-the-badge&logo=github&label=%E2%AD%90%20Star%20this%20repo&color=yellow)](https://github.com/199-biotechnologies/douglas-adamiser/stargazers)
[![Follow @longevityboris](https://img.shields.io/badge/Follow_%40longevityboris-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/longevityboris)

<br>

[![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-F96854?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJ3aGl0ZSI+PHBhdGggZD0iTTEyIDJDNi40OCAyIDIgNi40OCAyIDEyczQuNDggMTAgMTAgMTAgMTAtNC40OCAxMC0xMFMxNy41MiAyIDEyIDJ6Ii8+PC9zdmc+)](https://github.com/199-biotechnologies/douglas-adamiser)
[![Corpus](https://img.shields.io/badge/Corpus-528%2C808_words-blue?style=for-the-badge)](https://github.com/199-biotechnologies/douglas-adamiser)
[![Books Analysed](https://img.shields.io/badge/Books_Analysed-10-green?style=for-the-badge)](https://github.com/199-biotechnologies/douglas-adamiser)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

</div>

<br>

The Douglas Adamiser is not a vague "make it funnier" button. It is a Claude Code skill calibrated against **528,808 words** from every major Douglas Adams book -- the entire Hitchhiker's trilogy (all five of them), both Dirk Gentlys, *Last Chance to See*, *The Salmon of Doubt*, and *The Meaning of Liff*. It learned that Adams used "quite" and "rather" far more than "utterly" (which imitators overuse by a factor of roughly seven), that 30% of his sentences were short punches of 10 words or fewer, and that the first instance of bathos could appear anywhere from 30 words to 2,200 words into a piece. These are facts. They are the kind of facts that separate authentic Adams voice from the sort of pastiche that sounds like someone read *The Hitchhiker's Guide* once on a train and thought, "How hard can it be?"

Quite hard, as it turns out.

<br>

**[Why This Exists](#why-this-exists)** &#8226; **[Before vs After](#before-vs-after)** &#8226; **[Install](#install)** &#8226; **[Quick Start](#quick-start)** &#8226; **[How It Works](#how-it-works)** &#8226; **[Features](#features)** &#8226; **[Contributing](#contributing)** &#8226; **[License](#license)**

---

## Why This Exists

Most AI "style transfer" produces parody. Worse, it produces the *same* parody every time -- all bricks and digital watches and "not entirely unlike" constructions deployed with the subtlety of a Vogon reading poetry.

Adams was original. "Hordes of writers have tried to copy his style," noted one literary analyst, "but none successfully."

This skill aims to be the first to try *properly*. Not by recycling his jokes -- that would be rather like photocopying someone's smile and expecting it to charm -- but by applying his actual techniques, measured against his actual corpus, verified by deterministic validation scripts. The Adamiser doesn't quote Adams. It thinks like Adams. Or at least, it thinks like a very dedicated student of Adams who has done considerably more homework than is strictly healthy.

## Before vs After

**Input:**

> Tech company announces new AI assistant. The artificial intelligence system, developed over three years by a team of 200 engineers, can process natural language queries and provide helpful responses. The CEO stated that this represents a significant advancement in AI technology.

**After the Adamiser:**

> The technology company (which had, in fact, been a sandwich shop until a particularly aggressive investment round in 2019, and still occasionally smelled of tuna) announced on Tuesday that it had created something.
>
> The something in question was, they claimed, an artificial intelligence. This was not entirely accurate. It was, in fact, artificial, in much the same way that a plastic plant is artificial -- present, vaguely green-shaped, and fundamentally incapable of the thing it was pretending to be. The intelligence part remained, as it were, aspirational.
>
> Two hundred engineers had worked on the project. This is rather a lot of engineers. If you were to line up two hundred engineers end to end, they would stretch approximately 350 metres and would, almost certainly, complain about it.
>
> The CEO -- a man whose smile had been focus-grouped seventeen times and was now perfectly optimised for conveying the impression that he knew what he was talking about -- stated that this represented a "significant advancement." He did not specify what it was an advancement from, or towards, which is quite often how significant advancements work.

Notice: no brick similes. No 42 references. No "Don't Panic." Fresh observations about *this specific text*, not warmed-over Adams quotations. That is the point.

## Install

```bash
git clone https://github.com/199-biotechnologies/douglas-adamiser.git ~/.claude/skills/douglas-adamiser
```

That's it. Claude Code will detect the skill automatically.

## Quick Start

Open Claude Code and say any of:

```
"Adamise this news article about climate change"
"Transform this technical doc into Hitchhiker's Guide style"
"Make this academic paper sound like Douglas Adams wrote it"
```

Provide your source text, and the skill handles everything: content extraction, fresh observation generation, parallel specialist analysis, transformation, four-layer quality review, and corpus validation.

For long texts (over 10,000 words), the skill automatically chunks and processes in parallel.

## How It Works

The Adamiser runs a seven-step pipeline. This may seem like a lot of steps. It is a lot of steps. Adams himself had a simpler process, which was to sit in a bath for several hours and then write something brilliant, but unfortunately that technique has proven difficult to automate.

```
Source Text
    |
    v
[1] Content Extraction ---- measures length, maps structure, sets targets
    |
    v
[2] Originality Engines ---- Observation Engine + Contemporary Adams Vision (parallel)
    |                         "What's actually strange about this?"
    v
[3] Parallel Specialists --- Bathos Architect | Metaphor Engineer | Rhythm Analyst | Tangent Injector
    |
    v
[4] Transformation --------- Opening -> Body (paragraph-by-paragraph) -> Closing
    |
    v
[5] Four-Layer Review ------ Fidelity Check -> Anti-Cliche -> Technique Refinement -> Meaning Amplification
    |
    v
[6] Validation ------------- validate_metrics.py (deterministic, no vibes)
    |
    v
[7] Output + Report
```

**The four-layer review** is the critical differentiator. Style fidelity alone produces parody. The anti-cliche layer bans recycled tropes and demands every joke be "twisted more than once" -- because Adams never settled for the first punchline when a better one was hiding behind it. The meaning amplification layer ensures that every technique *serves the content*. Decorative absurdity fails this layer. Truth dressed in comedy passes.

## Features

### Corpus-Validated Statistics

Every metric is measured, not guessed:

| Metric | Adams' Actual Usage | What Imitators Do Wrong |
|--------|-------------------|----------------------|
| "quite" / "rather" | 8.13 / 6.73 per 10k words | Overuse "utterly" (7x too much) |
| Short sentences (10 words or fewer) | 30% | Too few -- miss the punchy rhythm |
| Single-sentence paragraphs | 31.9% | Barely use them |
| Dialogue tag "said" | 90% | Replace with "exclaimed", "retorted", etc. |
| Questions per 1000 words | ~9 | Too few -- lose the philosophical voice |
| First bathos placement | 30 to 2,200 words in | Fixed intervals (formulaic) |

### Parallel Specialist Agents

Four agents analyse your text simultaneously, each with corpus-calibrated targets:

- **Bathos Architect** -- identifies serious statements to deflate, maps insertion points using 4 distinct patterns
- **Metaphor Engineer** -- crafts comparisons across 5 domain categories (Mechanical, Animal, Human, Abstract, Natural)
- **Rhythm Analyst** -- audits sentence and paragraph structure against corpus targets
- **Tangent Injector** -- identifies digression opportunities using fresh material from the Observation Engine

### Anti-Cliche System

The Adamiser maintains a banned list and a budget system:

- **Banned entirely:** brick similes, 42 references, Vogon anything, Babel fish, "Don't Panic", whale/petunias
- **Budget-limited:** max 1 "not entirely unlike" per 2,000 words; tea and towels on strict rations
- **Twist depth:** 70%+ of jokes must have multiple twists

### Five Contextual Modes

Adams wrote differently depending on what he was writing. The skill detects and adapts:

| Mode | Short Sentences | Tangent Density | Character |
|------|:-:|:-:|---|
| Guide Entry | 20-25% | Low | Confident absurdity |
| Narrative Action | 35-40% | Medium | High reluctance (Arthur), low (Ford) |
| Philosophical Musing | 15-20% | High | Weary omniscience |
| Dialogue Scene | 45-55% | Low | Character-dependent |
| Descriptive Passage | 25-30% | Medium-High | Bored by magnificence |

### Deterministic Validation

Python scripts that check the output with no AI involved -- just counting:

```bash
python scripts/validate_metrics.py --source original.txt --output transformed.txt --json
```

Checks word count ratio, banned phrases, deadpan marker density, sentence distribution, exclamation marks (fewer than 1 per 2,000 words -- Adams was not the exclaiming type), and question frequency.

## Project Structure

```
douglas-adamiser/
├── SKILL.md                           # Main skill definition (Claude reads this)
├── prompts/                           # 13 agent prompts
│   ├── orchestrator.md                # Coordinates the whole show
│   ├── content_extractor.md           # Preserves source content
│   ├── observation_engine.md          # Generates fresh observations
│   ├── contemporary_adams_vision.md   # 2015-2025 absurdities
│   ├── anti_cliche_layer.md           # Bans recycled tropes
│   ├── bathos_architect.md            # Finds things to deflate
│   ├── metaphor_engineer.md           # Crafts comparisons
│   ├── rhythm_analyst.md              # Ensures proper sentence flow
│   ├── dialogue_transformer.md        # Fixes dialogue tags
│   ├── tangent_injector.md            # Inserts digressions
│   ├── layer1_fidelity_check.md       # Style deviation detection
│   ├── layer2_technique_refinement.md # Surgical corrections
│   └── layer3_meaning_amplification.md # Ensures techniques serve meaning
├── reference/                         # Corpus analysis and style guides
│   ├── literary_analysis.md           # 10-book literary analysis
│   ├── corpus_analysis_summary.md     # Statistics from 528,808 words
│   ├── contextual_modes.md            # 5 writing modes with targets
│   ├── original_patterns.md           # 100+ pre-generated Adams-esque patterns
│   ├── corpus_stats.json              # Raw corpus statistics
│   └── ...style guides                # Bathos, sentence, digression, vocabulary
├── scripts/                           # Validation tools (Python)
│   ├── validate_metrics.py            # Mandatory pipeline validation
│   ├── chunk_text.py                  # Long text chunking
│   ├── validate_adams_style.py        # Comprehensive style check
│   └── ...analysis tools              # Bathos detector, vocabulary checker, corpus analyser
├── examples/                          # Before/after transformations
├── templates/                         # Guide entry, chapter opening, cosmic zoom
├── CHANGELOG.md                       # Version history
├── CONTRIBUTING.md                    # How to contribute
└── LICENSE                            # MIT
```

## The Corpus

Calibrated against 10 books -- essentially everything Adams wrote that wasn't a shopping list:

- *The Hitchhiker's Guide to the Galaxy*
- *The Restaurant at the End of the Universe*
- *Life, the Universe and Everything*
- *So Long, and Thanks for All the Fish*
- *Mostly Harmless*
- *Dirk Gently's Holistic Detective Agency*
- *The Long Dark Tea-Time of the Soul*
- *Last Chance to See*
- *The Salmon of Doubt*
- *The Meaning of Liff*

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The short version: PRs welcome, corpus evidence required, vibes insufficient.

## License

[MIT](LICENSE) -- do what you like with it, just don't blame us when your quarterly report about synergising cross-functional deliverables comes back explaining that synergy is what happens when you put two things together and pretend the result is more impressive than either thing was on its own.

---

<div align="center">

Built by [Boris Djordjevic](https://github.com/longevityboris) at [199 Biotechnologies](https://github.com/199-biotechnologies) | [Paperfoot AI](https://paperfoot.ai)

<br>

[![Star this repo](https://img.shields.io/github/stars/199-biotechnologies/douglas-adamiser?style=for-the-badge&logo=github&label=%E2%AD%90%20Star%20this%20repo&color=yellow)](https://github.com/199-biotechnologies/douglas-adamiser/stargazers)
[![Follow @longevityboris](https://img.shields.io/badge/Follow_%40longevityboris-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/longevityboris)

<br>

*"The skill attempted to capture something ineffable, in much the same way that a net attempts to capture fog. It worked about as well as you'd expect, which is to say better than nothing but not as well as anyone hoped."*

</div>
