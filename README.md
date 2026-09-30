# The Unofficial Guide

**Name:** Trong Phan 
**Corpus:** `campus_life`

---

# Unit 1

## What This Does

Which corpus I picked:

- The campus_life corpus contains 88 short posts about student life and campus rules.

Who would use the guide?

- A student looking for a specific answer without searching through all the posts.

What kinds of questions does the system answer?

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

A length check found that all 88 `campus_life` posts are under 550 characters.
I chose a 600-character target so each current post stays in one chunk with its
heading and facts together. I chose zero overlap because none of these posts
needs a second chunk. The target is soft for longer documents.

## Sample Chunks

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

**1.** I asked AI to inspect the lengths of the `campus_life` posts and
propose a chunking strategy. It found 88 posts, with the longest at 549
characters, and suggested a 600-character target with zero overlap so each
current post stays whole. I used that design and asked AI to update
`chunker.py`. AI then tested a made-up longer document and found that the
function could produce a heading-only chunk and a paragraph over 600
characters. Based on that result, I changed my README to describe 600 as a
soft target because a longer paragraph may produce a chunk over 600
characters.

**2.** I asked AI for ideas for my fifth acceptance criterion. It first
suggested checking citation accuracy, which I thought was too close to
criterion 2's requirement to name a source. I chose timing accuracy instead
and changed criterion 5 to check my three timing questions at a 3-of-3 target,
counting an invented date or deadline as a failure.

**3.** In Unit 2, I asked AI to pressure-test my conclusion after all five
criteria passed. It pointed out that the correct source ranked first while
several fourth and fifth results were unrelated. I used that observation to
choose one measurable change: reducing `TOP_K` from 5 to 3, then rerunning the
same evaluation instead of inventing a failure.

**4.** I asked AI to compare my Before and After write-ups with the raw result
files. It found that an early draft incorrectly said retrieval returned the
same sources. I corrected the claim to say that the best distances and
first-ranked sources stayed the same while each prompt used two fewer chunks.
I described this as 40% fewer retrieved chunks and did not claim an exact token
or cost reduction because I did not measure tokens.

---

# Unit 2

## Run Log — Before

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks preserve complete sentences | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Answers give accurate timing | 3 of 3 | 3/3 | 3/3 | 3/3 | MET |

Manually scored by comparing each answer below with the expected fact in
`questions.py`. All 15 answers contain the expected fact.

### Evidence for Criterion 1 - Retrieved chunk contains the answer

From `results/run_2026-09-23_1838_before.md`, produced by
`run_eval.py::run_once`, using `store.py::search` and chunks from
`chunker.py::split_documents`.

```text
Question: What determines the housing selection order for juniors and seniors?
Best distance: 0.3942
Sources retrieved: admin_housing_lottery.txt, dining_the_atrium_followup.txt, housing_aldridge_hall.txt, housing_old_brewhouse.txt, housing_tamsin_court.txt

[from admin_housing_lottery.txt]
The housing lottery is not random in the way most people assume. Rising
sophomores get a number drawn at random, but juniors and seniors are ordered
by accumulated credit hours first, and only tie-break randomly.
```

### Evidence for Criterion 2 - Every answer names a source

From run 1 in `results/run_2026-09-23_1838_before.md`, produced by
`run_eval.py::run_once` and `generate.py::answer_from_chunks`.

```text
Question: What determines the housing selection order for juniors and seniors?
Run: 1

For juniors and seniors, the housing selection order is determined first by
accumulated credit hours, with random tie-breaking used only when there is a
tie (admin_housing_lottery.txt).

Question: Through which week can a student drop a course?
Run: 1

A student can drop a course through the end of week six.

Source: admin_withdrawal_deadline.txt
(also mentioned in admin_add_drop_deadline.txt)

Question: Do dining dollars roll over from autumn to spring?
Run: 1

Yes, dining dollars roll over from the autumn semester to the spring semester
(admin_dining_dollars.txt).

Question: When can a student change their meal-plan tier?
Run: 1

A student can change their meal plan tier once during the first ten days of
the semester.

Source: admin_meal_plan_changes.txt

Question: When do study-abroad applications open for the following academic year?
Run: 1

Study-abroad applications open in October for the following academic year
(admin_study_abroad.txt).
```

### Evidence for Criterion 3 - Gate stops out-of-corpus questions

From `results/run_2026-09-23_1838_before.md`, produced by
`run_eval.py::check_out_of_scope` and `gate.py::check`.

```text
Produced by run_eval.py::check_out_of_scope, cutoff 0.6. Refused 5 of 5.
```

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.825 | refused |
| How do I change the oil in a diesel engine? | 0.934 | refused |
| Who won the 1994 World Cup? | 0.886 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844 | refused |
| How do I write a for loop in Rust? | 0.896 | refused |


### Evidence for Criterion 4 - Chunks preserve complete sentences

From `python app.py --corpus campus_life chunks -n 5`, produced by
`app.py::cmd_chunks` and `chunker.py::split_documents`.

```text
Chunk 1 | source: admin_add_drop_deadline.txt#0
produced by: chunker.py::split_documents

On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer
window — through the end of week six — but a drop after week two shows as a W
on your transcript. Nothing anywhere on the registrar's site says this plainly,
and students find out from each other.
```

### Evidence for Criterion 5 - Answers give accurate timing

From run 1 in `results/run_2026-09-23_1838_before.md`, produced by
`run_eval.py::run_once` and `generate.py::answer_from_chunks`.

```text
Question: Through which week can a student drop a course?
Run: 1

A student can drop a course through the end of week six.

Source: admin_withdrawal_deadline.txt
(also mentioned in admin_add_drop_deadline.txt)

Question: When can a student change their meal-plan tier?
Run: 1

A student can change their meal plan tier once during the first ten days of
the semester.

Source: admin_meal_plan_changes.txt

Question: When do study-abroad applications open for the following academic year?
Run: 1

Study-abroad applications open in October for the following academic year
(admin_study_abroad.txt).
```

## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | The retrieved chunks contained the expected fact for all 5 questions in every run, exceeding the 4-of-5 target. |
| 2 | Every answer names a source | MET | All 5 answers named at least one source file in each of the three runs, meeting the 5-of-5 target. |
| 3 | Gate stops out-of-corpus questions | MET | The relevance gate refused all 5 out-of-scope questions at the 0.60 cutoff, exceeding the 4-of-5 target. Retrieval and the gate are deterministic, so this result applies to all three columns. |
| 4 | Chunks preserve complete sentences | MET | All 5 sampled chunks read as complete thoughts without a sentence cut off at either boundary, meeting the 5-of-5 target. |
| 5 | Answers give accurate timing | MET | All 3 timing answers reported the time stated in the source without inventing a date or deadline in every run, meeting the 3-of-3 target. |

## Diagnoses

All five criteria were met in every run, so I did not identify a failed
pipeline stage. The test set was relatively straightforward because each
question asks for a fact stated directly in one short `campus_life` post.
Criteria 1 and 3 were also conservative: both required 4 of 5, while the
system achieved 5 of 5. I would tighten criterion 1 to require the
answer-containing source to rank first for all 5 questions, because merely
appearing somewhere in five retrieved chunks allows unrelated material into
the prompt.

## The Improvement

**What I changed:**
Since the correct source ranked first in all five cases, and the extra chunks
make the prompt longer and could distract the generator on a harder question,
I reduced top-K from 5 to 3 so the prompt contains less unrelated material. I
did not measure a token or cost reduction in these historical runs.

**Why I picked it:**

Again, the correct source ranked first for all 5 test questions, but several
4th and 5th results were unrelated. Reducing top-k should remove distracting
context without losing the answer-containing chunk. The measured outcome for
this run was the number of retrieved chunks, not token cost.


### Run Log — After

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks preserve complete sentences | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Answers give accurate timing | 3 of 3 | 3/3 | 3/3 | 3/3 | MET |

Manually scored from `results/run_2026-09-27_0045_after.md`. Each answer was
compared with the expected fact in `questions.py`.

### After Evidence for Criterion 1 - Retrieved chunk contains the answer

From run 1 in `results/run_2026-09-27_0045_after.md`, produced by
`run_eval.py::run_once`, using `store.py::search` and chunks from
`chunker.py::split_documents`.

```text
Question: What determines the housing selection order for juniors and seniors?
Run: 1
Best distance: 0.3942 (passed the gate)
Sources retrieved: admin_housing_lottery.txt, housing_old_brewhouse.txt,
housing_tamsin_court.txt

For juniors and seniors, the housing selection order is determined first by accumulated credit hours, with random tie-breaking used only when necessary (admin_housing_lottery.txt).
```

### After Evidence for Criterion 2 - Every answer names a source

From run 1 in `results/run_2026-09-27_0045_after.md`, produced by
`run_eval.py::run_once` and `generate.py::answer_from_chunks`.

```text
Question: What determines the housing selection order for juniors and seniors?
Run: 1

For juniors and seniors, the housing selection order is determined first by accumulated credit hours, with random tie-breaking used only when necessary (admin_housing_lottery.txt).

Question: Through which week can a student drop a course?
Run: 1

A student can drop a course through the end of week six. This comes from the document `admin_add_drop_deadline.txt` (and is also mentioned in `admin_withdrawal_deadline.txt`).

Question: Do dining dollars roll over from autumn to spring?
Run: 1

Yes, dining dollars roll over from the autumn semester to the spring semester.

Source: `admin_dining_dollars.txt`

Question: When can a student change their meal-plan tier?
Run: 1

A student can change their meal plan tier once, during the first ten days of the semester.

Source: `admin_meal_plan_changes.txt`

Question: When do study-abroad applications open for the following academic year?
Run: 1

Study-abroad applications open in October for the following academic year (Source: admin_study_abroad.txt).
```

### After Evidence for Criterion 3 - Gate stops out-of-corpus questions

From `results/run_2026-09-27_0045_after.md`, produced by
`run_eval.py::check_out_of_scope` and `gate.py::check`.

```text
Produced by run_eval.py::check_out_of_scope, cutoff 0.6. Refused 5 of 5.
```

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.825 | refused |
| How do I change the oil in a diesel engine? | 0.934 | refused |
| Who won the 1994 World Cup? | 0.886 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844 | refused |
| How do I write a for loop in Rust? | 0.896 | refused |

### After Evidence for Criterion 4 - Chunks preserve complete sentences

Chunking is deterministic and was unchanged for the after run. This sample was
produced by `app.py::cmd_chunks` and `chunker.py::split_documents`.

```text
Chunk 1 | source: admin_add_drop_deadline.txt#0
produced by: chunker.py::split_documents

On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer
window — through the end of week six — but a drop after week two shows as a W
on your transcript. Nothing anywhere on the registrar's site says this plainly,
and students find out from each other.
```

The other four complete samples remain in the Unit 1 Sample Chunks section.

### After Evidence for Criterion 5 - Answers give accurate timing

From run 1 in `results/run_2026-09-27_0045_after.md`, produced by
`run_eval.py::run_once` and `generate.py::answer_from_chunks`.

```text
Question: Through which week can a student drop a course?
Run: 1

A student can drop a course through the end of week six. This comes from the document `admin_add_drop_deadline.txt` (and is also mentioned in `admin_withdrawal_deadline.txt`).

Question: When can a student change their meal-plan tier?
Run: 1

A student can change their meal plan tier once, during the first ten days of the semester.

Source: `admin_meal_plan_changes.txt`

Question: When do study-abroad applications open for the following academic year?
Run: 1

Study-abroad applications open in October for the following academic year (Source: admin_study_abroad.txt).
```

**Did it help?**

I reduced `TOP_K` from 5 to 3. This reduced the retrieved context from five
chunks to three chunks per question, a 40% reduction in the number of chunks
sent to the model, while all five acceptance criteria remained MET. The
smaller context should reduce prompt token usage and cost, although I did not
measure the exact token count. The correct source remained ranked first with
the same best distance for every test question, the gate again refused 5 of 5
out-of-scope questions, and the answers preserved the expected facts and
source citations across all three runs.

## What's Still Broken

No acceptance criterion remained missed after the change. However, reducing
`TOP_K` removed the fourth and fifth results without guaranteeing that all
three remaining chunks support the question. For example, the study-abroad
question still retrieved add/drop and advising documents in addition to the
correct study-abroad source. These extra chunks make the prompt longer and
could distract generation on a harder question.

The historical evaluation also covers only five direct fact questions from
short posts. It does not show how the system handles paraphrased questions,
conflicting sources, or questions that require combining multiple documents.
I stopped at `TOP_K = 3` because all current criteria still passed; choosing a
smaller value responsibly would require a broader retrieval test set.

After review, I added `scorer.py`, which checks each answer against the expected
fact already stored in `questions.py`. New runs therefore score factual answers
the same way every time. I also changed `run_eval.py::write_report` to save the
model-call count and service-reported input/output token totals in each run log,
instead of printing those measurements only to the terminal. The committed
historical logs predate that instrumentation, so I do not claim a measured
token saving from them.


## What I'd Do Differently

I would make criterion 1 stricter: for all 5 test questions, the first-ranked
chunk must contain the answer. The original 4-of-5 criterion only required the
answer to appear somewhere in the retrieved set, so it did not measure ranking
quality or penalize unrelated chunks below the correct result.

I would also strengthen criterion 2 to require every answer to name a source
that directly supports its claim. Requiring any filename is too loose because
an answer could cite an unrelated retrieved document and still pass. This
revised criterion would measure citation correctness as well as citation
presence.

I would change the order of the experiment as well. First I would define and
score the stricter metric, then record a `TOP_K = 5` baseline, change only
`TOP_K`, and repeat the same evaluation at `TOP_K = 3`. For the context-size
change, the useful comparison is service-reported input tokens per run; the
original five criteria were already passing and could not show whether the
smaller prompt helped.

