---
name: douglas-adamiser
description: This skill should be used when the user asks to "write like Douglas Adams", "transform text into Adams style", "Hitchhiker's Guide style", "make this funnier", "add absurdist humor", "write sci-fi comedy", "parody this", or mentions Douglas Adams, bathos, anti-climax, or British absurdist humor. Transforms any text into Douglas Adams' distinctive style with bathos, cosmic irony, philosophical tangents, and perfectly timed anti-climaxes. Includes validation scripts and vocabulary checks.
---

# Douglas Adamiser

## Purpose

Transform any text (news articles, academic papers, technical documentation, rough drafts, book chapters) into Douglas Adams' distinctive style: deadpan British absurdism, cosmic-scale bathos, philosophical tangents that arrive at profound irrelevance, and sentences that hang in the air much the same way that bricks don't.

## When to Use

- News articles needing absurdist transformation
- Technical/academic writing requiring comic deflation
- Book chapters or stories needing Adams voice
- Any text where user requests "Douglas Adams style" or "Hitchhiker's style"
- Parody requests for sci-fi or technical subjects
- User wants to add British absurdist humor

## When NOT to Use

- Already comedic text in different style (Pratchett, Wodehouse)
- Serious content requiring gravity (eulogies, medical instructions)
- User explicitly wants different humor style
- Very short snippets (<100 words) unless expanding to full piece

## Core Style Principles

### The Adams Formula

**Setup → Elevation → Bathos → Recovery → Deeper Absurdity**

Every paragraph follows this arc: establish something seemingly important, elevate reader expectations, deflate with anti-climax, briefly recover, then reveal the deflation was itself setup for greater absurdity.

### Signature Techniques

1. **Cosmic Bathos** - Universe-scale importance deflated to trivial concern
2. **The Brick Simile** - Comparisons to what things DON'T resemble
3. **Digressive Tangents** - Parenthetical asides that become the point
4. **Deadpan Delivery** - Ludicrous statements in matter-of-fact tone
5. **Philosophical Anti-Climax** - Deep questions answered with mundane observations

## Execution Workflow

### Step 1: Analyse Source

Read input and extract:
- Subject matter and key facts to preserve
- Tone to subvert (formal, urgent, technical)
- Natural bathos opportunities (anything presented as important)
- Digression hooks (concepts begging for absurd elaboration)

### Step 2: Plan Transformation

Produce 5-bullet strategy:
1. Opening approach (cosmic scale or mundane zoom-in)
2. Primary bathos targets (what to deflate)
3. Digression opportunities (tangent subjects)
4. Simile/metaphor inversions planned
5. Closing anti-climax structure

### Step 3: Parallel Agent Analysis

**CRITICAL: Launch these 4 specialist agents IN PARALLEL using a single message with multiple Task tool calls:**

```
Agent 1: Bathos Architect
- Prompt: prompts/bathos_architect.md
- Task: Identify serious statements, map bathos insertion points
- Output: Bathos insertion map with patterns (A-D) and locations

Agent 2: Metaphor Engineer
- Prompt: prompts/metaphor_engineer.md
- Task: Inventory existing comparisons, suggest new ones using domain taxonomy
- Output: Comparison inventory and insertion suggestions (Mechanical/Animal/Human/Abstract/Natural)

Agent 3: Rhythm Analyst
- Prompt: prompts/rhythm_analyst.md
- Task: Audit sentence/paragraph structure against corpus targets
- Output: Rhythm map with correction recommendations (30% short, 32% single-sentence paragraphs)

Agent 4: Dialogue Transformer (if dialogue present)
- Prompt: prompts/dialogue_transformer.md
- Task: Audit dialogue tags (90% "said" rule), structure exchanges
- Output: Tag corrections and structural recommendations
```

Wait for all agents to complete, then synthesize outputs following priority order: Rhythm → Bathos → Metaphor → Dialogue.

### Step 4: Transform (Multi-Phase)

#### Phase A: Opening

Apply opening system from `reference/adams_style_guide.md`:
- **Cosmic Zoom**: Start at universal scale, crash to trivial
- **Mundane Enormity**: Begin with boring detail, reveal cosmic significance
- **Authoritative Absurdity**: Guide-entry format with deadpan impossibility

#### Phase B: Body Transformation

For each paragraph:
1. Identify the "serious point"
2. Elevate its apparent importance
3. Insert digressive tangent (see `reference/digression_systems.md`)
4. Apply bathos formula (see `reference/bathos_patterns.md`)
5. Weave sentence architecture (see `reference/sentence_architecture.md`)

#### Phase C: Closing

Apply triple-layer Adams closing:
- Layer 1: Return to original subject as if nothing absurd occurred
- Layer 2: Casual mention of universe-ending implication
- Layer 3: Character worrying about tea/towels/bureaucracy

### Step 5: Three-Layer Quality Review (Ultrathink)

**This is the critical differentiator: Style fidelity alone produces parody. Meaning amplification produces excellence.**

Run sequentially - each layer feeds the next:

#### Layer 1: Style Fidelity Check
- Prompt: `prompts/layer1_fidelity_check.md`
- Input: First draft from Step 4
- Task: DETECT (not fix) style deviations using corpus-calibrated metrics
- Output: Fidelity report with specific flags (target: ≥6/8 checks passed)

#### Layer 2: Technique Refinement
- Prompt: `prompts/layer2_technique_refinement.md`
- Input: First draft + Layer 1 report
- Task: Apply SURGICAL corrections to flagged issues only
- Output: Refined text + change log

#### Layer 3: Meaning Amplification
- Prompt: `prompts/layer3_meaning_amplification.md`
- Input: Refined text + original source
- Task: Ensure Adams techniques AMPLIFY (not obscure) the message
- Output: Final text + amplification report

**The Ultrathink Principle:** Every Adams technique must serve the content's truth. Decorative mimicry fails Layer 3.

See `prompts/orchestrator.md` for complete workflow coordination.

### Step 6: Validate

Run validation suite:
```bash
python scripts/validate_adams_style.py <output_file>
```

Checks for:
- Bathos presence (varied placement, NOT formulaic intervals)
- Digression density (at least 1 tangent per 300 words)
- Inverted comparisons ("not like X, but like Y")
- Sentence rhythm (30% short ≤10 words, 31% single-sentence paragraphs)
- Adams vocabulary markers ("quite"/"rather" > "utterly")
- Dialogue tag distribution (90% "said")

### Step 7: Report

```
Transformation Complete

**Source Analysis:**
- Original style: [formal/journalistic/technical]
- Original length: [X words]
- Bathos opportunities identified: [Y]

**Output Specifications:**
- Final length: [X words]
- Bathos instances: [N]
- Digressions inserted: [M]
- Simile inversions: [K]
- Validation: [PASS/FAIL with details]

**Key Transformations:**
1. [e.g., Converted Q3 earnings report to Vogon poetry analysis]
2. [e.g., Inserted 400-word tangent on digital watches]
3. [e.g., Applied cosmic bathos to meeting agenda]
```

## CRITICAL: Corpus-Validated Insights

Based on analysis of 528,808 words of authentic Adams text across 10 books:

### Vocabulary (Often Imitated Wrong)

**Top Intensifiers:**
- "quite" (8.13/10k) and "rather" (6.73/10k) are #1 and #2
- "utterly" is OVERUSED in imitations (only 0.96/10k in real Adams)

**Sentence Distribution:**
- 30% short (≤10 words) - MORE punchy than commonly assumed
- 46% medium (11-30 words)
- 15% long (31-50 words)
- 8% very long (>50 words)

**Questions:** ~9 per 1000 words (high - drives philosophical voice)

**Signature "brick simile":** Use sparingly - only 0.15 per 10k words

### Opening Patterns (NEW)

| Type | Frequency | Example |
|------|-----------|---------|
| Cosmic Zoom | 33% | "Far out in the uncharted backwaters..." |
| Character Action | 25% | "The regular early morning yell of horror..." |
| Philosophical | 17% | "There is a theory which states..." |
| Meta-Commentary | 17% | "The history of the Galaxy has got muddled..." |

### Bathos Timing is NOT Formulaic (NEW)

Real Adams places first bathos anywhere from **30 words to 2,200 words** into a piece. The variation IS the pattern. Do not apply bathos at fixed intervals.

### Dialogue (NEW)

- Use "said" for 90% of dialogue tags
- Reserve "burbled" for machines, "rasped/rumbled" for authority figures
- ~31.9% of paragraphs are single sentences (use for punchlines)

### Metaphor Patterns (NEW)

- 693 comparisons across corpus: 37.5% "like a/the", 28.3% "as if"
- Inverted comparisons ("not like X, but like Y") are signature technique
- Categories: Mechanical (34%), Animal (28%), Human (22%), Abstract (10%)

### Chapter Endings (NEW)

- End with deflation/bathos (35%), dialogue punchline (30%), physical comedy (20%)
- Final sentences typically SHORT (3-15 words)
- Recurring: "Or so it would seem", "It was that simple"

See `reference/literary_analysis.md` for complete analysis and `reference/corpus_analysis_summary.md` for statistics.

## Reference Files

### Agent Prompts (Multi-Layer System)
- `prompts/orchestrator.md` - **CRITICAL** - Coordinates entire workflow with parallel agents and 3-layer review
- `prompts/bathos_architect.md` - Bathos analysis and insertion (4 patterns, corpus timing)
- `prompts/metaphor_engineer.md` - Comparison crafting (5 techniques, domain taxonomy)
- `prompts/rhythm_analyst.md` - Sentence/paragraph structure (corpus targets)
- `prompts/dialogue_transformer.md` - Dialogue tags and exchange patterns
- `prompts/layer1_fidelity_check.md` - Style deviation detection (8 checkpoints)
- `prompts/layer2_technique_refinement.md` - Surgical corrections
- `prompts/layer3_meaning_amplification.md` - **ULTRATHINK** - Ensures techniques serve message

### Core References
- `reference/literary_analysis.md` - Comprehensive literary patterns from 10-book corpus study
- `reference/corpus_analysis_summary.md` - **CRITICAL** - Real statistics from Adams corpus
- `reference/adams_style_guide.md` - Complete style breakdown with examples
- `reference/bathos_patterns.md` - 12 bathos formulas with templates
- `reference/sentence_architecture.md` - Adams-specific sentence patterns
- `reference/digression_systems.md` - Tangent insertion techniques
- `reference/vocabulary_guide.md` - Adams vocabulary, neologisms, phrase patterns

### Scripts
- `scripts/validate_adams_style.py` - Full validation suite (calibrated to corpus)
- `scripts/bathos_detector.py` - Detect and score anti-climax patterns
- `scripts/vocabulary_checker.py` - Check Adams vocabulary markers
- `scripts/analyse_corpus.py` - Analyse text for Adams style statistics

### Examples
- `examples/news_to_adams.md` - News article transformation
- `examples/academic_to_adams.md` - Academic paper transformation
- `examples/technical_to_adams.md` - Technical doc transformation

### Templates
- `templates/guide_entry.md` - Hitchhiker's Guide entry format
- `templates/chapter_opening.md` - Novel chapter opening format
- `templates/cosmic_zoom.md` - Universal-to-trivial structure

## Output Requirements

**Must include:**
- Bathos instances (vary placement - NOT at fixed intervals, range 30-2200 words to first)
- At least 1 digressive tangent per 300 words
- At least 1 inverted comparison ("not like X, but like Y") per 500 words
- 30% short sentences (≤10 words), especially at bathos moments
- ~31% single-sentence paragraphs for rhythm and punchlines
- Use "quite"/"rather" NOT "utterly" for intensification
- Use "said" for 90% of dialogue tags

**Length:** Input +30-80% expansion (digressions add content)

**Format:** Markdown (or HTML using appropriate template)

**Endings:** Short final sentence (3-15 words), deflation or dialogue punchline

---

**Invocation:** Provide source text and say "Adamise this", "Douglas Adams style", or "make this absurd" - skill auto-detects from context.

**Modes:** "plan only" for strategy preview, "validate only" to check existing text, "guide entry" for Hitchhiker's format specifically.
