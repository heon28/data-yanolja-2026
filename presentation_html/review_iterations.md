# HTML Presentation Review Iterations

Created: 2026-06-01

Review target: `presentation_html/index.html`

Goal:

- The presentation should work for an audience with no prior context, including non-CS college students, marketers, CRM operators, and business stakeholders.
- The presentation should follow Patrick Winston's speaking principles as adapted in this project.
- Review ends only when both review tracks pass in a fresh round without requiring additional changes.

## Baseline

- Baseline commit: `f33615a Add initial HTML presentation`
- Slide count: 21
- Format: local HTML, local Pretendard font, fixed `presentation_html/format/format.png` background
- Network dependency policy: no CDN or external math renderer

## Review Tracks

1. No-context audience review
   - Reviewer: subagent `Wegener`
   - Status: in progress
   - Scope: beginner comprehension, term clarity, motivation, visual pedagogy, missing bridges

2. Patrick Winston review
   - Reviewer: subagent `Poincare`
   - Status: in progress
   - Scope: promise, fence, roadmap, sparse condiments, question design, contribution ending

## Iteration 1

### Inputs

- `presentation_html/index.html`
- `presentation_html/speaker_script.md`
- Winston review also uses:
  - `docs/how_to_speak/MIT_OpenCourseWare_Patrick_Winston.md`
  - `docs/how_to_speak/patrick_winston_analysis.md`
  - `presentation_html/presentation_principles.md`

### No-Context Audience Review

Result: FAIL.

Reviewer summary:

- The speaker script is more beginner-friendly than the screen.
- Slides 4-12 ask beginners to track notation, GP vocabulary, posterior reasoning, acquisition functions, UCB, and beta before the concrete CRM example is fully visible.
- The issue is conceptual sequencing, not visual clutter.

Blockers:

1. CRM motivation arrives too late on screen.
   - Fix: On slides 3-4, explicitly show `x = 할인율 × 발송시점`, `f(x) = incremental profit`, and `각 점 = 하나의 A/B 후보`.
2. Slide 5 introduces GP notation before the audience has a visual handle.
   - Fix: Lead with “possible response curves” / “가능한 성과 곡선” and make `f ~ GP(m,k)` secondary.
3. Slides 7-10 compress too many abstractions.
   - Fix: Add persistent legend: `mean = 지금 좋아 보이는 정도`, `uncertainty = 아직 모르는 정도`, `acquisition score = 다음 실험 후보 점수`.
4. Slide 12 BO loop is too abstract.
   - Fix: Rename boxes to practical A/B terms: `past A/B results`, `score candidate policies`, `run next A/B`, `update response map`.
5. Slides 16-20 exceed the beginner contract.
   - Fix: Make constraint captions explicit, simplify context, collapse implementation details.

Keep:

- Opening promise concept.
- Slide 2 `Compare / Choose` distinction.
- Soft positioning of BO as complementary to A/B testing.
- Incremental profit framing.
- Final uncertainty takeaway.
- Clean sparse visual style.

### Winston Review

Result: FAIL.

Reviewer summary:

- The deck has the right backbone but is not ready under a strict Winston rubric.
- Main failures: cropped visuals, weak empowerment promise, too-subtle road map, inconsistent question-before-answer structure, and contribution ending that is more takeaway than contribution.

Blockers:

1. Rendered visuals are cropped on slides 04, 05, 09 at 1280×720.
   - Fix: constrain `.two-col .viz` to its grid column and reduce panel widths.
2. Slide 01 is a topic/thesis opening, not a clean empowerment promise.
   - Fix: replace H1 with `30분 뒤, 다음 A/B 후보를 통계적으로 고를 수 있습니다`.
3. Road map / verbal punctuation is too subtle.
   - Fix: add a visible road map or section-opening landmarks.
4. Question design is inconsistent.
   - Fix: split constraint question from answer; make context question explicit.
5. Final slide is a takeaway, not a Winston contribution slide.
   - Fix: enumerate 3 contributions and keep uncertainty final line.
6. Slides 19-20 risk becoming an Ax / BoTorch API lecture.
   - Fix: collapse into concept-level implementation slide.

Keep:

- Slide 02 fence.
- Repeated next-experiment motif.
- Sparse visual-first slides.
- Policy heatmap / next-dot motif.
- Constraint surprise.
- CRM concrete story.
- No thank-you ending.

### Changes Made

Applied changes:

- Kept total slide count at 21 by adding one constraint question slide and collapsing the two code slides into one implementation slide.
- Slide 01: changed the headline into an empowerment promise: `30분 뒤, 다음 A/B 후보를 통계적으로 고를 수 있습니다`.
- Slide 03: added early concrete mapping: `x = 할인율 × 발송시점`, `f(x) = incremental profit`.
- Slide 04: added practical definitions: `x`, `f(x)`, and `각 점 = 하나의 A/B 후보`.
- Slide 05: reframed GP as `Possible response curves`; made `f ~ GP(m,k)` secondary and labeled sample curves.
- Slides 07-10: added practical legends for data, posterior, mean, uncertainty, and acquisition score.
- Slide 12: renamed the BO loop boxes to practical A/B operations:
  `past A/B results`, `score policies`, `run next A/B`, `update map`.
- Slide 16: split constraint into a question-only slide.
- Slide 17: moved constrained formula and feasible heatmap to answer slide; added explicit `f(x)`, `g(x)`, and `τ` captions.
- Slide 18: made context question explicit: `Same policy for every context?`.
- Slide 20: collapsed Ax and BoTorch code snapshots into one concept-level implementation map.
- Slide 21: replaced takeaway-only ending with a contribution slide containing three enumerated contributions plus the uncertainty final line.
- CSS: constrained `.two-col .viz` to its grid column to prevent 1280×720 overflow.

### Verification

Commands run:

- `python3` HTML parser check: passed.
- Slide structure check: 21 slides, each `slide-01` through `slide-21` appears exactly once.
- External dependency scan: no CDN / MathJax / KaTeX / external URL dependency found, except the SVG namespace string.
- Chrome headless screenshots at 1280×720 for slides 01, 03, 04, 05, 09, 10, 12, 16, 17, 18, 20, 21.

Visual spot checks:

- Slides 04, 05, and 09 no longer crop to the right.
- Slide 16 now asks before showing the constrained answer.
- Slide 20 no longer clips the BoTorch explanatory line.

Next step:

- Commit Iteration 1 changes.
- Run a fresh no-context audience review and a fresh Winston review. Review ends only if both pass in that fresh round.

## Iteration 2

### Inputs

- Commit reviewed: `e4fe1e5 Address first presentation review round`
- `presentation_html/index.html`
- `presentation_html/speaker_script.md`
- Winston review also used the Winston reference materials listed above.

### No-Context Audience Review

Result: FAIL.

Remaining blockers:

1. Slide 11 is still too insider-facing.
   - Fix: add `β = how much we value learning from uncertain areas`.
   - Replace `leans exploitation` with `mostly tests what already looks good`.
   - Replace `adds exploration pressure` with `also tests what we still do not know`.
2. Slides 16-20 are out of sync with `speaker_script.md`.
   - Fix: update the script so the constraint question, constrained answer, context answer, beyond-CRM, and implementation slides match the current HTML.
3. Slide 18 context visual needs a self-contained chart label.
   - Fix: add `Each map: discount_rate × send_timing`.
   - Add or clarify that the orange dot is the best policy for that context.

### Winston Review

Result: FAIL.

Remaining blockers:

1. Slide 18 violates question-before-answer.
   - Fix: make the context question slide question-only; move formula and maps to a separate answer slide.
2. Final contribution drops context.
   - Fix: contribution 3 should say `objective, constraint, and context`.

### Changes Made

- Slide 11: changed title to `β changes how much we learn`; added plain-language β bridge.
- Slide 11: changed beta labels to:
  - `mostly tests what already looks good`
  - `also tests what we still do not know`
- Slide 18: split context into a question-only slide.
- Slide 19: moved context formula and four maps to an answer slide titled `Context changes the optimum`.
- Slide 19: added `Each map: discount_rate × send_timing`.
- Slide 19: added legend for the orange dot: `best policy for this context`.
- Slide 22: changed contribution 3 to include context.
- `speaker_script.md`: updated scene count to 22 and rewrote scenes 16-22 to match the current HTML flow.

### Verification

- HTML parser check: passed.
- Slide structure check: 22 slides, each `slide-01` through `slide-22` appears exactly once.
- Speaker script check: `this script uses 22 scenes`; scenes 18-22 now match context question, context answer, beyond CRM, implementation structure, and contributions.
- Chrome headless spot checks at 1280×720:
  - Slide 11: beta bridge and plain-language labels fit.
  - Slide 18: question-only context slide fits.
  - Slide 19: context answer maps and labels fit.
  - Slide 21: implementation map fits.
  - Slide 22: contribution ending includes objective, constraint, and context.

Next step:

- Commit Iteration 2 changes.
- Run a fresh round 3 no-context audience review and Winston review. Review ends only if both pass in that same fresh round.

## Iteration 3

### Inputs

- Commit reviewed: `eacc85c Address second presentation review round`
- `presentation_html/index.html`
- `presentation_html/speaker_script.md`
- `presentation_html/review_iterations.md`

### No-Context Audience Review

Result: PASS.

Residual risks noted:

- Slides 5-12 are still concept-dense, but the script now provides enough verbal scaffolding.
- Some `On screen:` cue blocks are not exact copies of rendered slide text, but the spoken script aligns with the deck.
- English/Korean mix is acceptable if the speaker delivers the plain-language bridges.

### Winston Review

Result: FAIL.

Remaining blocker:

- Slide 16 still answers its own question because the supporting visual says `optimal? / not always`.
- Fix: make slide 16 question-only by removing `not always`; answer stays on slide 17.

### Changes Made

- Slide 16 visual no longer answers the question.
- Removed `not always` from the `optimal?` card.
- Kept the answer on slide 17 only.

### Verification

- Chrome headless 1280×720 screenshot for slide 16 confirms the slide is now question-only:
  `highest profit + highest opt-out -> optimal?`
- No answer text appears on slide 16.

Next step:

- Commit Iteration 3 change.
- Run a fresh round 4 no-context audience review and Winston review. Review ends only if both pass in that same fresh round.

## Iteration 4

### Inputs

- Commit reviewed: `c8478a4 Make constraint prompt question-only`
- `presentation_html/index.html`
- `presentation_html/speaker_script.md`
- `presentation_html/review_iterations.md`

### No-Context Audience Review

Reviewer: subagent `Planck`

Result: PASS.

Evidence reported by reviewer:

- Inspected `presentation_html/index.html`, `presentation_html/speaker_script.md`, and the review log.
- Rendered all 22 slides at 1280×720.
- Confirmed the current version is ready for a no-context audience if delivered with the provided script.

Residual risks, not blockers:

- Slides 5-12 remain the densest conceptual stretch, but now have enough plain-language anchors.
- Some script `On screen:` cue blocks are not exact copies of rendered slide text, but the spoken script aligns with the slide intent and sequence.
- Slide 21 introduces Ax and BoTorch, but the script keeps this structural rather than API-focused.

Keep unchanged:

- Slide 1 promise.
- Slide 2 A/B-vs-BO fence.
- Comparison → search → belief → decision → CRM progression.
- Practical legends on slides 7-11.
- Question-only slides 16 and 18.
- Final contribution structure, especially objective, constraint, context, and uncertainty takeaway.

### Winston Review

Reviewer: subagent `Kuhn`

Result: PASS.

Evidence reported by reviewer:

- Inspected the current HTML and Winston reference materials.
- Confirmed the previous slide 16 blocker was fixed.
- Rendered slide 16 at 1280×720 and verified that it supports the question without answering it.

Residual risks, not blockers:

- Slides 7, 10, and 17 are dense but acceptable as condiments.
- Roadmap lines skip the `EXTEND` label, but section markers and spoken bridge are sufficient.
- Slide 21 names Ax and BoTorch; it must remain concept-level, not an API walkthrough.

Satisfied Winston principles:

- Empowerment promise.
- Fence.
- Road map / sectioning.
- Slides as condiments.
- One message per slide.
- Question-before-answer on slides 9→10, 16→17, and 18→19.
- Contribution ending without a thank-you slide.
- Visuals reinforce the argument rather than decorate it.

### Changes Made

No further changes after round 4. Both review tracks passed in the same fresh round.

### Verification

Local verification after round 4:

- `presentation_html/index.html` parses as HTML.
- Slide count is 22.
- `slide-01` through `slide-22` each appear exactly once.
- `not always` no longer appears in the HTML.
- Pretendard local font exists at `fonts/Pretendard-1.3.9/web/variable/woff2/PretendardVariable.woff2`.
- Fixed background exists at `presentation_html/format/format.png`.
- Local server returns `200 text/html`.
- External dependency scan found no CDN / MathJax / KaTeX / external URL dependency, except the SVG namespace string.

Conclusion:

- Review loop is complete.
- The requested no-context audience review passed.
- The requested Winston subagent review passed.
