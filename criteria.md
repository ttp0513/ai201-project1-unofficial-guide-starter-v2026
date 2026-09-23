# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

> **Unit 2 completion note:** I noticed after the initial baseline run that the
> explanations for criteria 1–3 were blank. I added the explanations below
> without changing any of the original targets.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:** Each test question asks for a specific fact from one short
`campus_life` post, so the correct evidence should normally appear in the
retrieved chunks. I required 4 of 5 because related posts about housing,
courses, and dining can compete with the exact source in semantic search, while a lower target would allow too many questions to lack usable evidence.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:** The pipeline keeps each chunk's source filename and the
grounding instruction tells the model to name the file it used, so requiring a
source in all 5 answers is achievable. Allowing even one answer without a
source would prevent a student from checking that answer against the original
post.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:** During cutoff tuning, the covered questions had best
distances from 0.1782 to 0.3942, while the out-of-scope questions ranged from
0.8246 to 0.9340. The 0.60 cutoff sits in that gap. I required at least 4 of 5
refusals because an accidental semantic match may let one unrelated question
through, while allowing two or more would make the gate unreliable.

---

## 4. Chunks preserve complete sentences

<!-- YOU WRITE THIS ONE.

     How would you know if your chunks were the right size? Name something
     countable or observable.

     Examples of the right shape — don't copy these, they should come from
     what you actually saw in Milestone 3:
       - "At least 4 of 5 sampled chunks read as a complete thought, with no
          sentence cut in half at either end."
       - "No chunk is shorter than 200 characters, since anything below that
          in my corpus turned out to be a heading with no content under it." -->

The posts are short, so a sentence-aware chunker should preserve boundaries in all five samples. Allowing one cut sentence would accept a problem the chunker can prevent.

**Why this target:** The `campus_life` documents are short posts, and their useful facts are usually contained in complete sentences. Keeping sentence boundaries intact should be achievable for all five samples and helps prevent a retrieved chunk from leaving out part of a fact.


---

## 5. Answers give accurate timing

<!-- YOU WRITE THIS ONE TOO.

     Pick something you actually care about getting right. It could be about
     speed, about refusals, about a particular kind of question your corpus
     handles badly, about source attribution being correct rather than merely
     present — anything, as long as it names a number or an observable
     outcome. -->
     
In each evaluation run, all timing questions must give the time stated in their source and must not add an unsupported date or deadline.

**Why this target:** 3 of my five test questions ask about timing, and each source gives a clear time window. I require all three answers to report that timing correctly (3 of 3), because even one wrong time could mislead a student.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
