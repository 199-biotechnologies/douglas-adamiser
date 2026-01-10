# Changelog

All notable changes to the Douglas Adamiser will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [0.5.0] - 2025-01-10

### Added - The "Adams Essence" System

Addressing feedback that output was "Great Pastiche" but not "Indistinguishable from the Real Thing." Major improvements to worldview consistency, comparison variety, and avoiding "book report" mode.

#### New Core Principles (reference/original_patterns.md)

**Five Adams Essence Principles:**
1. **Industrial/Domestic Collision** - Compare abstract concepts to specific household objects
2. **Animals Must Be Bureaucratic/Depressed/Confused** - Never cute or twee
3. **Avoid Standard Earth Clichés** - Adams was an alien observer
4. **Don't Echo Famous Structural Riffs** - Avoid copying the "hung in the air" structure
5. **Describe Entropy, Don't List Formats** - Avoid "viral meme" style

**Five Adams Universe Rules (Internal Logic):**
1. **Bureaucracy Always Increases** - Never decreases, even with technology
2. **Technology Creates New Problems** - Never cleanly solves old ones
3. **Cosmic Indifference, Institutional Hostility** - Universe doesn't care, committees do
4. **Specific Triviality Over Generic Profundity** - "buttered toast" not "fire is hot"
5. **Humans Are Proud of Embarrassing Things** - Trivial achievements celebrated

**Six Comparison Structure Alternatives:**
- Structure A: Negative Definition ("did not help, in the sense that...")
- Structure B: Precise Trivial Truth (buttered toast, not fire)
- Structure C: Scale Comparison ("roughly as useful as...")
- Structure D: "Provided You Understood" Inversion
- Structure E: Behavioural Animal (bureaucratic/depressed/confused)
- Structure F: "Which Is To Say" Reframe

#### "Not a Book Report" Rule (prompts/content_extractor.md)

- **BANNED:** "The author notes/describes/argues..."
- **BANNED:** Any reference to "the author" or "the original"
- Source content becomes ABSOLUTE FACT in Adams universe
- Events simply ARE, opinions simply EXIST
- Write Guide Entries, not book reviews

#### Enhanced Anti-Cliché Detection (prompts/anti_cliche_layer.md)

New detection categories:
- Standard Earth clichés (Titanic, elephant in room, etc.)
- Cute animal violations
- Viral meme patterns
- Book report constructions
- Simile loop frequency tracking
- Adams Universe logic violations

#### Pattern Fixes

Fixed 4 patterns that violated newly established principles:
- #1: Removed "hung in air" structure clone
- #10: Replaced cute hedgehog with bureaucratic badger
- #45: Replaced Titanic cliché with crashing plane metaphor
- #84: Replaced viral "email cascade" with entropy description

### Changed

- `metaphor_engineer.md`: Added Technique F (Industrial/Domestic Collision) and animal rules
- `observation_engine.md`: Added Step 6 (Industrial/Domestic Collision Brainstorm)
- Simile loop frequency limit: max 2 of any structure per 1000 words

---

## [0.4.0] - 2025-01-10

### Added - The Originality System

The skill now generates original content rather than recycling Adams' specific tropes.

#### New Components

- **Observation Engine** (`prompts/observation_engine.md`)
  - Questions assumptions in source text
  - Generates FRESH observations graded A/B/C
  - Key method: "What's actually strange about this if you think about it?"
  - Provides raw material for original jokes

- **Contemporary Adams Vision** (`prompts/contemporary_adams_vision.md`)
  - Identifies 2015-2025 absurdities relevant to topic
  - Modern equivalents for digital watches, Vogon bureaucracy
  - Optional web search for recent examples (last 2 years prioritised)
  - Covers: tech pride, bureaucracy 2.0, philosophy, unquestioned behaviour

- **Anti-Cliché Layer** (`prompts/anti_cliche_layer.md`)
  - Runs between Layer 1 and Layer 2
  - BANNED items (0 uses): brick similes, 42, Vogons, Babel fish, "Don't Panic"
  - LIMITED items (budget system): "not entirely unlike", tea, towels
  - "Twist more than once" audit: single-twist jokes flagged
  - Originality verification

- **Original Patterns Bank** (`reference/original_patterns.md`)
  - 100+ pre-generated Adams-esque patterns
  - Organized by category: bathos, metaphor, tangent, etc.
  - Ready-to-use templates with [TOPIC] placeholders
  - All original - no recycled Adams material

#### Updated Workflow

Phase 0 now includes:
1. Content Extractor (as before)
2. Observation Engine (parallel)
3. Contemporary Adams Vision (parallel)

Phase 3 now includes 4 layers:
1. Style Fidelity Check
2. Anti-Cliché Layer (NEW)
3. Technique Refinement (now includes cliché replacement)
4. Meaning Amplification

#### New Quality Gates

- 0 BANNED items in output
- LIMITED items within budget
- ≥70% of jokes have multiple twists
- Fresh observations used, not recycled Adams

### Changed

- Updated orchestrator with new workflow diagram
- Updated SKILL.md with originality requirements
- Layer 2 now receives Anti-Cliché report for cliché replacement
- README updated with Four-Layer system description

---

## [0.3.0] - 2025-01-09

### Added - Content Preservation System

Addressing feedback that output was too short and lost source content.

#### New Components

- **Content Extractor** (`prompts/content_extractor.md`)
  - Runs BEFORE any transformation
  - Extracts ALL key points with importance ratings (HIGH/MEDIUM/LOW)
  - Sets length targets (60-115% of source)
  - Creates coverage checklist for Layer 3 verification

- **Length Validation** in Layer 1
  - Checks output is within 60-115% of source
  - TOO SHORT (<60%): Fails, returns to Phase 2
  - Content has been lost if below floor

- **Content Coverage Check** in Layer 3
  - Verifies ≥90% of key points survived
  - HIGH importance: 100% required (non-negotiable)
  - MEDIUM importance: 85%+ required

### Changed

- Updated orchestrator with Phase 0 for content extraction
- Layer 1 now checks length BEFORE style checks
- Layer 3 now verifies content coverage BEFORE meaning amplification

### Principles

- **Preserve-First**: Adams added tangents ON TOP of content, he didn't compress
- Output length should be source length + Adams additions, not source length compressed

---

## [0.2.0] - 2025-01-08

### Added - Anti-Efficiency System

Addressing feedback about "Marketing Copy in Adams Style" - output was too punchy and efficient.

#### New Components

- **Contextual Modes** (`reference/contextual_modes.md`)
  - 5 modes: Guide Entry, Narrative Action, Philosophical Musing, Dialogue Scene, Descriptive Passage
  - Each mode has specific targets for short sentences, tangent density, reluctance
  - Mode detection runs BEFORE applying style metrics

- **Anti-Efficiency Checks** in Layer 1
  - Over-punchiness detection (flagged if short sentences exceed mode target by >10%)
  - Linearity check (A→B→C progressions flagged)
  - Reluctance audit (eager/helpful tone flagged)

- **Pattern Diversity Tracking**
  - Bathos patterns tracked (flag if any used >3 times)
  - Metaphor domains tracked (flag if any >50%)
  - Sentence openers tracked (flag if any used >4 times)

- **Tangent Injector** (`prompts/tangent_injector.md`)
  - 5 tangent categories
  - Target: 1 tangent per 300-500 words
  - Linearity detection

### Changed

- Layer 1 now has 12 checkpoints (up from 8)
- Mode detection runs before all other checks
- Short sentence targets are now mode-specific, not global

---

## [0.1.0] - 2025-01-07

### Added - Initial Release

The Douglas Adamiser: A Claude Code skill for transforming text into Douglas Adams' style.

#### Core Features

- **Corpus Analysis**: 528,808 words across 10 Adams books
- **Multi-Agent System**: Bathos Architect, Metaphor Engineer, Rhythm Analyst, Dialogue Transformer
- **Three-Layer Review**: Fidelity Check, Technique Refinement, Meaning Amplification
- **Validation Scripts**: Python tools calibrated to corpus statistics

#### Agent Prompts

- `orchestrator.md` - Workflow coordination
- `bathos_architect.md` - Bathos analysis (4 patterns)
- `metaphor_engineer.md` - Comparison crafting (5 domains)
- `rhythm_analyst.md` - Sentence structure (corpus targets)
- `dialogue_transformer.md` - Dialogue tags (90% "said" rule)
- `layer1_fidelity_check.md` - Style deviation detection
- `layer2_technique_refinement.md` - Surgical corrections
- `layer3_meaning_amplification.md` - Meaning > style enforcement

#### Reference Materials

- `literary_analysis.md` - 10-book literary analysis
- `corpus_analysis_summary.md` - Statistics from corpus
- `adams_style_guide.md` - Complete style breakdown
- `bathos_patterns.md` - 12 bathos formulas
- `sentence_architecture.md` - Adams sentence patterns
- `digression_systems.md` - Tangent techniques
- `vocabulary_guide.md` - Adams vocabulary

#### Key Statistics

- "quite" (8.13/10k) and "rather" (6.73/10k) are top intensifiers
- "utterly" is overused in imitations (only 0.96/10k in real Adams)
- 30% short sentences (≤10 words)
- 31.9% single-sentence paragraphs
- 90% "said" for dialogue tags
- Bathos timing: 30-2200 words (NOT formulaic)

---

## Author

**Boris Djordjevic**

## License

MIT
