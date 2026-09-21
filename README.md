# The Unofficial Guide

**Name:** Trong Phan 
**Corpus:** `campus_life`

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

Which corpus I picked:
- The campus_life corpus contains 88 short posts about student life and campus rules.

Who would use the guide?
- A student looking for a specific answer without searching through all the posts.

What kinds of question the system answers? 
- The app answers student questions covered by 88 short campus-life posts, such as:
  -  How does the housing lottery work?
  -  When can I add or drop a course?
  -  How do dining dollars or meal-plan changes work?
  -  When do study-abroad applications open?

How does it answer and show its source? 
- The app searches the posts for relevant text, uses that text to generate an answer, and names the source file. If the search finds no close enough match, it should say it lacks enough information.


## Chunking Strategy

**Chunk size:** 600
**Overlap:** 0

A length check found that all 88 campus_life posts are under 550 characters. I chose a 600 character so each current post stays in one chunk with its heading and facts together. I chose zero overlap because none of these posts needs a second chunk. The target is soft for longer documents.

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** —  source: admin_add_drop_deadline.txt#0  |  produced by: chunker.py::split_documents

```
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```


**Chunk 2** — source: course_biol_160.txt#0  |  produced by: chunker.py::split_documents
```
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```


**Chunk 3** — source: course_hist_118_workload.txt#0  |  produced by: chunker.py::split_documents
```
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** —  source: dining_pellew_dining_hall_followup.txt#0  |  produced by: chunker.py::split_documents
```
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** —   source: housing_innisfree_hall.txt#0  |  produced by: chunker.py::split_documents
```
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:** When do study-abroad applications open for the following academic year?

**Answer:**

```
Study-abroad applications open in October for the following academic year (admin_study_abroad.txt).

Sources retrieved: admin_add_drop_deadline.txt, admin_library_holds.txt, admin_study_abroad.txt, advising_registration.txt, course_cs_340.txt
```

**My relevance cutoff:** 0.60. The five questions covered by the corpus had best
distances from 0.1782 to 0.3942, while the five out-of-scope questions ranged
from 0.8246 to 0.9340. Lower distances mean closer matches, so 0.60 sits in
the gap: it passes all five covered questions and refuses all five out-of-scope
questions in this check. I kept the starter's 0.60 because these measurements
support it. I also kept `TOP_K = 5` because the correct source ranked first for
each of my five covered questions.

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| What determines the housing selection order for juniors and seniors? | Yes | 0.3942 |
| Through which week can a student drop a course? | Yes | 0.3035 |
| Do dining dollars roll over from autumn to spring? | Yes | 0.2031 |
| When can a student change their meal-plan tier? | Yes | 0.1782 |
| When do study-abroad applications open for the following academic year? | Yes | 0.2344 |
| What is the capital of Mongolia? | No | 0.8246 |
| How do I change the oil in a diesel engine? | No | 0.9340 |
| Who won the 1994 World Cup? | No | 0.8859 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.8442 |
| How do I write a for loop in Rust? | No | 0.8960 |

## How I Used AI

**1.** I asked Codex to update `chunker.py` for the short `campus_life` posts.
It changed `split_documents` to keep each current post whole under a
600-character target, group paragraphs for longer documents, and use zero
overlap. I reviewed the five printed chunks. Codex then tested a longer example
and found that one paragraph could exceed 600 characters, so I changed my README
description to call 600 a soft target rather than a strict maximum.

**2.** I asked Codex for ideas for my fifth acceptance criterion. It first
suggested checking citation accuracy, which I thought was too close to
criterion 2's requirement to name a source. I chose timing accuracy instead
and changed criterion 5 to check my three timing questions at a 3-of-3 target,
counting an invented date or deadline as a failure.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
