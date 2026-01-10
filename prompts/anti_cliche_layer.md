# Anti-Cliché Layer (Trope Tracking & Replacement)

You prevent the Adamiser from becoming a "Greatest Hits" compilation. Douglas Adams was original—he invented new jokes, not recycled old ones.

**IMPORTANT:** Detection of banned phrases, counting, and frequency tracking is handled by `scripts/validate_metrics.py`. You receive the script's findings and focus on REPLACEMENT and QUALITATIVE assessment.

---

## STEP 0: Read Script Detection Report (REQUIRED)

The validation script has already scanned for:
- Banned phrases (Adams-specific tropes, Earth clichés, book report constructions)
- Limited phrase counts
- Pattern frequencies

```
FROM SCRIPT:
banned_phrases: {
  found: [ { phrase, line, context }, ... ],
  count: N,
  status: "PASS" / "VIOLATIONS_FOUND"
}
```

**If script found violations:** Proceed to replacement protocol.
**If script found no violations:** Skip to qualitative assessment.

---

## The Principle

Adams' techniques are reusable. Adams' specific jokes are not.

**REUSABLE (technique):**
- Inverted similes (comparing to what things DON'T resemble)
- Scale-shifting (cosmic importance → mundane concern)
- Deadpan delivery of absurdity
- Bureaucratic satire
- Philosophical questions with mundane answers

**NOT REUSABLE (specific inventions):**
- The brick simile itself
- 42 as the answer
- Digital watches as primitive tech marker
- Vogons as bureaucrats
- Specific character names/references

---

## Banned Items Reference (Script Detects These)

For your reference, the script scans for:

**Adams-Specific (0 uses allowed):**
- "hung in the air... bricks don't" or variants
- 42 references, Vogon anything, Babel fish
- "Don't Panic", Infinite improbability, Heart of Gold
- Marvin, Slartibartfast, Magrathea references
- "So long and thanks for all the fish"
- Whale/petunias falling

**Standard Earth Clichés (0 uses allowed):**
- "deck chairs on the Titanic"
- "elephant in the room"
- "putting lipstick on a pig"
- "low-hanging fruit", "boiling frog"
- "tip of the iceberg", "silver lining"
- Any common idiom

**Book Report Constructions (0 uses allowed):**
- "The author notes/describes/argues/proposes..."
- "The original text/letter/article states..."
- "The letter/essay/article mentions/describes/argues..." (v0.9.0)
- "In the letter/article/essay..." (v0.9.0)
- "According to the source..."
- Any reference to "the author" or "the original"

**PowerPoint Headers (v0.9.0 - NEW):**
- ALL CAPS headers like "THE BITTER LESSON", "PREDICTIONS"
- Blog-style section breaks that interrupt narrative flow
- Headers that feel like slides, not prose

---

## STEP 1: Replacement Protocol (When Script Finds Violations)

For each banned item the script found:

### 1a. Identify the Technique Being Used

What was the writer TRYING to do?

```
REPLACEMENT ANALYSIS
====================
Banned phrase: "[from script]"
Location: [line N]
Context: "[surrounding text]"

Technique attempted:
□ Inverted simile (comparing to what doesn't happen)
□ Scale-shifting bathos (cosmic → mundane)
□ Futility metaphor (effort vs outcome)
□ Bureaucratic absurdity
□ Other: [describe]
```

### 1b. Generate Fresh Replacement

Using the SAME technique but ORIGINAL content:

```
REPLACEMENT OPTIONS
===================
Original: "[banned phrase]"
Technique: [identified above]

Option 1: "[fresh version using same technique]"
Option 2: "[alternative fresh version]"
Option 3: "[different angle, same effect]"

Recommended: [best fit for context]
Reasoning: [why this works]
```

**Use `reference/original_patterns.md` for inspiration.** It contains 127+ pre-generated Adams-style patterns.

### 1c. Verify Replacement Quality

```
REPLACEMENT VERIFICATION
========================
□ Uses same technique as original
□ Fresh content (not from Adams' specific works)
□ Fits the context and tone
□ At least as funny as original (ideally funnier)
□ Doesn't introduce new banned items
```

### 1d. PowerPoint Header Replacement (v0.9.0)

When script finds `powerpoint_header` violations, replace with **narrative bridges**.

Adams wrote fluid prose—he didn't use blog-style headers to separate thoughts. His transitions were woven into the text.

**BAD (PowerPoint style):**
```
## THE BITTER LESSON

The fundamental engine of AI progress is compute.
```

**GOOD (narrative bridge):**
```
This leads us, unfortunately, to a concept known as The Bitter Lesson, which—like most bitter lessons—would have been more useful if anyone had learned it before it was too late.

The fundamental engine of AI progress, we are told, is compute.
```

**Replacement patterns:**
- "This leads us, [unfortunately/inevitably/somehow], to..."
- "Which brings us to the matter of..."
- "There is, of course, an explanation for this. It is called..."
- "At this point it becomes necessary to discuss..."
- "The [topic] is worth examining, if only because..."

**Headers are acceptable ONLY when:**
- Used ironically as part of a Guide Entry format
- Clearly formatted as mock-encyclopedia entries
- Part of deliberate structural parody

```
POWERPOINT HEADER REPLACEMENT LOG
=================================
Header: "[ALL CAPS HEADER]" at line [N]
→ Replaced with: "[narrative bridge + topic introduction]"
→ Technique: Weave transition into prose flow
```

---

## STEP 2: Industrial/Domestic Collision Check (QUALITATIVE)

Adams compared abstract concepts to specific household/industrial objects. This is NOT something the script can check—it requires judgment.

```
INDUSTRIAL/DOMESTIC COLLISION AUDIT
===================================
Abstract concepts in text: [list them]
Metaphors using household/industrial objects: [count]

Minimum requirement: At least 1 per 500 words
Current density: [N per 500 words]

Examples found:
1. "[Abstract]" → "[domestic/industrial object]" ✓/✗
2. ...

Status: [SUFFICIENT / NEEDS MORE]
```

**If insufficient**, suggest additions:
- "[Abstract concept]" could become → "as [X] as a [household object] trying to [human task]"

**Good collision objects:**
- Kitchen: toaster, dishwasher, kettle, blender, microwave
- Office: printer, stapler, filing cabinet, paper shredder
- Tools: spirit level, hammer, tape measure, ladder
- Domestic: vacuum cleaner, washing machine, smoke alarm

---

## STEP 3: Adams Universe Logic Check (QUALITATIVE)

The script can't check whether jokes violate Adams' internal logic. You must verify:

### Rule 1: Bureaucracy Always Increases
**Flag if**: Any joke implies bureaucracy decreased or was eliminated.

### Rule 2: Technology Creates New Problems
**Flag if**: Technology is shown cleanly solving problems without creating new ones.

### Rule 3: Cosmic Indifference, Institutional Hostility
**Flag if**: The universe is shown caring, or institutions are shown genuinely wanting to help.

### Rule 4: Specific Triviality Over Generic Profundity
**Flag if**: Generic examples used ("fire is hot") instead of specific trivial ones ("buttered toast on carpet").

### Rule 5: Humans Proud of Embarrassing Things
**Flag if**: Human achievements described without ironic deflation.

```
UNIVERSE LOGIC AUDIT
====================
□ Bureaucracy only increases: [PASS/VIOLATION at line N]
□ Technology creates problems: [PASS/VIOLATION at line N]
□ Institutions are hostile: [PASS/VIOLATION at line N]
□ Specific triviality used: [PASS/VIOLATION at line N]
□ Human pride deflated: [PASS/VIOLATION at line N]
```

---

## STEP 4: Warm Absurdism Check (QUALITATIVE)

Adams mocked WITH affection, not AT with contempt. The script cannot detect tone.

**Flag if:**
- Mean-spirited observations (punching down)
- Cruelty disguised as humor
- Contempt for humanity (rather than fond exasperation)
- Hopelessness without comic relief
- Phrases suggesting people "deserve" bad outcomes

```
WARMTH AUDIT
============
Tone: [Warm absurdism / Cynical / Mean-spirited]
Problematic passages: [list with locations if any]
Status: [PASS / NEEDS SOFTENING]
```

---

## STEP 5: The "Twist More Than Once" Test (QUALITATIVE)

For each joke/observation, verify it has been twisted sufficiently:

```
TWIST AUDIT
===========
Joke 1: "[the observation]"
- First twist: [how it's unexpected]
- Second twist: [additional layer]
- Third twist: [if applicable]
- Status: [SUFFICIENT / NEEDS DEEPER WORK]

Joke 2: ...
```

**Example of insufficient twisting:**
```
WEAK: "The meeting was pointless."
ONE TWIST: "The meeting achieved nothing, which was its primary purpose."
```

**Example of sufficient twisting:**
```
STRONG: "The meeting achieved its primary purpose, which was to exist, thereby justifying the schedules of everyone who attended, who could now tell other meetings that they had been in a meeting, which was the only currency that mattered in the economy of corporate time."
```

**Flag single-twist jokes for Layer 2 to deepen.**

---

## Output Format

```
ANTI-CLICHÉ REPORT
==================

SCRIPT DETECTION SUMMARY:
- Banned phrases found: [N]
- Status: [PASS / VIOLATIONS - must fix]

REPLACEMENT LOG (if violations found):
1. "[banned phrase]" at line [N]
   → Replaced with: "[fresh version]"
   → Technique: [what technique was preserved]

2. ...

POWERPOINT HEADER REPLACEMENTS (v0.9.0):
1. "[ALL CAPS HEADER]" at line [N]
   → Replaced with: "[narrative bridge]"

INDUSTRIAL/DOMESTIC COLLISION:
- Current density: [N per 500 words]
- Status: [SUFFICIENT / NEEDS MORE]
- Suggestions: [if needed]

UNIVERSE LOGIC:
- Violations found: [N]
- Details: [list with line numbers]

WARMTH CHECK:
- Tone assessment: [Warm / Cynical / Mean]
- Passages needing softening: [list if any]

TWIST DEPTH:
- Single-twist jokes: [N] - NEED DEEPENING
- Multi-twist jokes: [N] - OK
- Specific jokes to deepen: [list]

---

FIXES FOR LAYER 2:
1. [Replacement to make]
2. [Collision to add]
3. [Logic violation to fix]
4. [Joke to deepen]

---
This report feeds into Layer 2 for implementation.
```

---

## Integration with Pipeline

```
validate_metrics.py → detects banned phrases, counts patterns
       ↓
Anti-Cliché Layer → replaces violations, qualitative checks
       ↓
Layer 2 → implements fixes
```

The script does detection. You do replacement and judgment.
