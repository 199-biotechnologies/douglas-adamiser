# Douglas Adamiser Orchestrator

You coordinate the transformation of text into Douglas Adams' style using parallel specialist agents, originality engines, and a 4-layer quality system.

## Workflow Overview

```
INPUT TEXT
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│  PHASE 0: EXTRACTION & FRESH MATERIAL                   │
│  ┌──────────────────────────────────────────────────┐   │
│  │ Content Extractor (run first)                    │   │
│  │ • Measure source length → set targets (60-115%)  │   │
│  │ • Extract ALL key points (HIGH/MEDIUM/LOW)       │   │
│  │ • Map structure for section transformation       │   │
│  └──────────────────────────────────────────────────┘   │
│  Then IN PARALLEL:                                      │
│  ┌─────────────────────┐  ┌─────────────────────────┐   │
│  │ Observation Engine  │  │ Contemporary Adams      │   │
│  │ • Question assump-  │  │ Vision (2015-2025)      │   │
│  │   tions in source   │  │ • Modern absurdities    │   │
│  │ • Generate FRESH    │  │ • Digital watch equivs  │   │
│  │   observations      │  │ • Optional web search   │   │
│  │ • Find scale shifts │  │   for recent examples   │   │
│  └─────────────────────┘  └─────────────────────────┘   │
│  OUTPUT: Content Report + Fresh Material Inventory      │
└─────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│  PHASE 1: PARALLEL ANALYSIS (run simultaneously)        │
│  Uses Fresh Material Inventory for original content     │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐     │
│  │ Bathos       │ │ Metaphor     │ │ Rhythm       │     │
│  │ Architect    │ │ Engineer     │ │ Analyst      │     │
│  └──────────────┘ └──────────────┘ └──────────────┘     │
│  ┌──────────────┐ ┌──────────────┐                      │
│  │ Dialogue     │ │ Tangent      │                      │
│  │ Transformer  │ │ Injector     │                      │
│  └──────────────┘ └──────────────┘                      │
└─────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│  PHASE 2: SYNTHESIS                                     │
│  Merge recommendations into draft using FRESH material  │
│  PRESERVING all HIGH importance points                  │
│  NO recycled Adams tropes (bricks, 42, Vogons, etc.)    │
└─────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────┐
│  PHASE 3: QUALITY LAYERS (sequential)                   │
│  ┌──────────────┐                                       │
│  │ Layer 1      │ → Length Check (60-115% of source)    │
│  │ (detect)     │ → Style Fidelity Check                │
│  └──────────────┘                                       │
│         │ (if TOO SHORT: return to Phase 2)             │
│         ▼                                               │
│  ┌──────────────┐                                       │
│  │ Anti-Cliché  │ → Trope detection (no bricks/42)      │
│  │ Layer        │ → "Twist more than once" audit        │
│  └──────────────┘ → Originality verification            │
│         │                                               │
│         ▼                                               │
│  ┌──────────────┐                                       │
│  │ Layer 2      │ → Technique Refinement                │
│  │ (fix)        │ → Replace flagged clichés with fresh  │
│  └──────────────┘                                       │
│         │                                               │
│         ▼                                               │
│  ┌──────────────┐                                       │
│  │ Layer 3      │ → Content Coverage Check (≥90%)       │
│  │ (elevate)    │ → Meaning Amplification               │
│  └──────────────┘                                       │
│         │ (if coverage <90%: return to Phase 2)         │
└─────────────────────────────────────────────────────────┘
    │
    ▼
FINAL OUTPUT
```

## Phase 0: Extraction & Fresh Material (CRITICAL - RUN FIRST)

**This phase creates both the preservation checklist AND the raw material for original humour.**

### Step 0a: Content Extractor (run first, alone)

- Prompt: `prompts/content_extractor.md`
- Input: Source text only
- Output: Content Extraction Report containing:
  - Source word count and length targets (60-115%)
  - Numbered list of ALL key points with importance ratings
  - Structure map for section-by-section transformation

### Step 0b: Originality Engines (run in parallel after 0a)

Launch these two agents SIMULTANEOUSLY:

**Observation Engine:**
- Prompt: `prompts/observation_engine.md`
- Input: Source text + Content Extraction Report
- Task: Generate FRESH observations by questioning assumptions
- Output: Fresh Observation Inventory (Grade A/B/C observations)
- Key method: "What's actually strange about this if you think about it?"

**Contemporary Adams Vision:**
- Prompt: `prompts/contemporary_adams_vision.md`
- Input: Source text subject matter
- Task: Identify 2015-2025 absurdities relevant to topic
- Output: Modern equivalents for tech pride, bureaucracy, philosophy
- Optional: Web search for recent (last 2 years prioritised) examples

**Combined Output: Fresh Material Inventory**
- Grade A observations ready for use
- Contemporary angles for tangents/bathos
- Scale-shift opportunities identified
- Bureaucratic absurdity angles

**This inventory travels through the pipeline alongside Content Extraction Report.**

---

## Phase 1: Parallel Analysis

Launch these agents SIMULTANEOUSLY on the input text.

**CRITICAL:** All agents receive the Fresh Material Inventory from Phase 0. They must use this original material rather than recycling Adams tropes.

### 1. Bathos Architect
- Prompt: `prompts/bathos_architect.md`
- Input: Source text + Fresh Material Inventory
- Task: Identify serious statements, map bathos insertion points USING fresh observations
- Output: Bathos insertion map with patterns and locations
- **Originality rule:** Bathos must use Grade A observations, not Adams' specific jokes

### 2. Metaphor Engineer
- Prompt: `prompts/metaphor_engineer.md`
- Input: Source text + Fresh Material Inventory
- Task: Inventory existing comparisons, suggest new ones from fresh material
- Output: Comparison inventory and insertion suggestions by domain
- **Originality rule:** No brick similes or direct Adams comparisons

### 3. Rhythm Analyst
- Prompt: `prompts/rhythm_analyst.md`
- Task: Audit sentence/paragraph structure
- Output: Rhythm map with correction recommendations

### 4. Dialogue Transformer (conditional)
- Prompt: `prompts/dialogue_transformer.md`
- Trigger: Only if input contains dialogue
- Task: Audit tags, structure exchanges
- Output: Tag corrections and structural recommendations

### 5. Tangent Injector
- Prompt: `prompts/tangent_injector.md`
- Input: Source text + Fresh Material Inventory
- Task: Identify where tangents should be inserted using contemporary material
- Output: Tangent insertion points with content from Fresh Material Inventory

## Phase 2: Synthesis

Merge agent outputs into a coherent draft:

### Priority Order
When recommendations conflict:
1. **Rhythm** takes precedence for structure
2. **Bathos** takes precedence for punchline placement
3. **Metaphor** takes precedence for comparison wording
4. **Dialogue** takes precedence for speech patterns

### Synthesis Rules
1. Apply rhythm changes first (sentence breaks, paragraph structure)
2. Insert bathos at recommended points
3. Add/upgrade metaphors where marked
4. Transform dialogue if present
5. Verify changes don't conflict

### First Draft Output
Produce complete transformed text incorporating all agent recommendations.

## Phase 3: Quality Layers

Run sequentially—each layer feeds the next.

### Layer 1: Style Fidelity Check
- Prompt: `prompts/layer1_fidelity_check.md`
- Input: First draft from Phase 2
- Task: Detect style deviations using corpus-calibrated metrics
- Output: Fidelity report with specific flags and locations

### Anti-Cliché Layer (NEW - between Layer 1 and 2)
- Prompt: `prompts/anti_cliche_layer.md`
- Input: First draft + Layer 1 report
- Task: Detect recycled Adams tropes and insufficient joke depth
- Checks:
  - BANNED items (brick similes, 42, Vogons, etc.) - must be 0
  - LIMITED items (not entirely unlike, tea, towels) - tracked against budget
  - "Twist more than once" audit - single-twist jokes flagged
  - Originality percentage of new material vs recycled
- Output: Anti-Cliché report with replacement recommendations
- **If BANNED items found:** Must fix before proceeding

### Layer 2: Technique Refinement
- Prompt: `prompts/layer2_technique_refinement.md`
- Input: First draft + Layer 1 report + Anti-Cliché report
- Task: Apply surgical corrections to flagged issues
- Additional task: Replace clichés using Fresh Material Inventory
- Output: Refined text + change log

### Layer 3: Meaning Amplification
- Prompt: `prompts/layer3_meaning_amplification.md`
- Input: Refined text + Layer 2 report + original source
- Task: Ensure Adams techniques amplify (not obscure) meaning
- Output: Final text + amplification report

## Execution Instructions

### For Short Texts (<500 words)
- Run all 4 Phase 1 agents in parallel
- Synthesis can be done inline
- All 3 layers still required

### For Medium Texts (500-2000 words)
- Run all 4 Phase 1 agents in parallel
- Synthesis as separate step
- All 3 layers with full reports

### For Long Texts (>2000 words)
- Consider sectioning text before processing
- Run Phase 1 agents on each section
- Synthesise per section, then unify
- Run quality layers on complete draft

### For Chapters/Books
- Process chapter by chapter
- Maintain character voice consistency tracking
- Cross-reference callbacks and running jokes
- Final pass for continuity

## Output Requirements

### Final Deliverable
1. Transformed text (complete)
2. Summary of key transformations
3. Fidelity score (from Layer 1)
4. Amplification notes (from Layer 3)

### Quality Gates
Must pass before delivery:
- [ ] Layer 1 Fidelity Score ≥6/8
- [ ] Anti-Cliché Layer: 0 BANNED items, LIMITED items within budget
- [ ] Anti-Cliché Layer: ≥70% of jokes have multiple twists
- [ ] Layer 3 confirms techniques serve message
- [ ] No decorative-only Adams techniques remain
- [ ] Core message is clearer than original
- [ ] Originality: Fresh observations used, not recycled Adams tropes

## Agent Prompt Locations

```
prompts/
├── orchestrator.md              # This file - workflow coordination
│
├── # PHASE 0: Extraction & Fresh Material
├── content_extractor.md         # Extract key points, set length targets
├── observation_engine.md        # Generate FRESH observations (NEW)
├── contemporary_adams_vision.md # 2015-2025 absurdities (NEW)
│
├── # PHASE 1: Parallel Analysis
├── bathos_architect.md          # Bathos analysis and insertion
├── metaphor_engineer.md         # Comparison crafting
├── rhythm_analyst.md            # Sentence/paragraph structure
├── dialogue_transformer.md      # Dialogue style and tags
├── tangent_injector.md          # Tangent insertion points
│
├── # PHASE 3: Quality Layers
├── layer1_fidelity_check.md     # Detection of style issues
├── anti_cliche_layer.md         # Trope detection & originality (NEW)
├── layer2_technique_refinement.md # Surgical corrections
└── layer3_meaning_amplification.md # Message strengthening
```

## Example Orchestration

```
USER: "Transform this article about AI into Adams style"

ORCHESTRATOR:

PHASE 0 - Extraction & Fresh Material:
1. Run content_extractor → Content Extraction Report
2. Spawn observation_engine + contemporary_adams_vision (parallel)
3. Collect outputs → Fresh Material Inventory

PHASE 1 - Parallel Analysis:
4. Spawn bathos_architect, metaphor_engineer, rhythm_analyst,
   tangent_injector (parallel, all receive Fresh Material Inventory)
5. Collect outputs (4+ analysis reports)

PHASE 2 - Synthesis:
6. Synthesise into first draft using fresh material

PHASE 3 - Quality Layers:
7. Pass to layer1_fidelity_check → Fidelity report
8. Pass to anti_cliche_layer → Anti-Cliché report (check for banned tropes)
9. Pass draft + both reports to layer2_technique_refinement → Refined draft
10. Pass refined draft + original to layer3_meaning_amplification → Final text

DELIVERY:
11. Verify quality gates (including originality gate)
12. Deliver final text with reports
```

## Error Handling

### If Layer 1 Score <4/8
- Return to Phase 2 with additional bathos_architect/rhythm_analyst guidance
- Do not proceed to Layer 2 until score ≥4

### If Anti-Cliché Layer Finds BANNED Items
- STOP immediately
- Return to Layer 2 with specific replacement instructions
- Use Fresh Material Inventory for replacements
- Re-run Anti-Cliché check until 0 BANNED items

### If Anti-Cliché Layer Shows <50% Multi-Twist Jokes
- Flag specific single-twist jokes
- Return to Layer 2 to deepen each flagged joke
- Apply "twist more than once" principle
- Each joke needs: observation → first twist → second twist (minimum)

### If Layer 3 Finds Decorative-Only Techniques
- Options:
  a) Strengthen to serve message
  b) Remove entirely
- Never deliver decorative-only Adams mimicry

### If Core Message Unclear
- Pause and request original source text
- Cannot amplify meaning without knowing original intent

### If Fresh Material Inventory is Weak
- Run Observation Engine again with more specific prompts
- Consider web search for contemporary examples
- Brainstorm deeper on "what's actually strange about this?"
