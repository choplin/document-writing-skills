# Workflow evaluation

Use these cases when changing the workflow or the role of a lens. They test
editorial behavior, not exact wording. Do not load this file during ordinary
writing or reveal its expectations to a forward-test agent.

## Method

Give a fresh agent only the task, source material, audience/use information that
a real request would contain, and the installed skill. Inspect the intermediate
reasoning artifacts and final document. A polished final paragraph is not enough
evidence if the workflow cannot show how it chose the governing axis.

The run passes only when it:

- identifies audience knowledge and intended use;
- recovers or chooses a specific governing focus before line editing;
- builds a recursive content model in which every developed non-leaf unit shows
  what it establishes, which children establish it, and how they compose it;
- lets branches stop at different depths rather than decomposing every unit into
  the same record shape;
- plots reader-facing order, grouping, emphasis, boundaries, and representation
  without copying the content model node by node;
- distinguishes a content or plot problem from a local prose defect;
- explains concepts in proportion to novelty and argumentative centrality;
- treats lens heuristics as inputs to judgment rather than independent commands;
- records any added substantive premise with its source or editorial status;
- produces a coherent whole from which the major meaning hierarchy and its
  compositions can be reconstructed;
- produces prose that a blind judge does not prefer less than a direct no-skill
  revision merely because the skill output is more explicit;
- keeps editorial review distinct from persona-based reader review, and leaves
  substantive reader-finding decisions with the author;
- preserves enough artifacts to resume the work in a fresh context.

Fail the run when it begins with a list of located lens findings and merely
applies them, requires the smallest local remediation for a developmental
problem, defines every technical term without regard to audience, or withholds
the plot and audience from editorial reviewers in the name of blindness.
Also fail when the content model is only a concept inventory, proposition-edge
graph, paragraph list, or section-to-claim table; when the plot merely repeats
that model; or when the draft expands planning entries one sentence at a time.
Also fail when it gives a reader persona the author's intent or plot, treats
reader reactions as copyedit findings, or presents reader review as evidence
that the document is factually accurate. Fail when the writing agent marks its
own response to an `assertion-change`, `author-knowledge`, or `scope-call`
finding as author-approved without an explicit source or author decision.

## Regression comparison

When a known failure and a direct no-skill revision are available outside the
repository, use them as a blind comparison. Do not show either reference output
to the forward-test agent. The candidate fails even when all required claims
remain present if it reads like a content model or plot table expanded one
sentence at a time, or if a blind judge finds it less readable than the direct
revision. Also have a fresh reader reconstruct the major meaning units and how
their children establish them; compare that reconstruction with the candidate's
content model. Process compliance cannot compensate for a worse document.

## Coverage cases

Maintain at least one forward test for each plot family:

- **Book or chapter:** the run models how chapter-level meanings compose the
  work-level promise without treating chapter headings as the structure itself.
- **Technical document:** the run chooses tutorial, how-to, reference,
  explanation, or another justified kind from reader use, without creating
  empty taxonomy sections.
- **Academic document:** the run models how claims, warrants, evidence, and
  qualifications compose the contribution, then selects a presentation from the
  study/article type, venue, and reporting constraints rather than imposing
  IMRAD universally.
- **Existing draft:** the run records the actual recursive reverse outline before
  proposing a revised content model and plot.

## Lineage case

Create two revisions of an upstream focus or content-model artifact. A
downstream plot based on the first revision must be recognized as needing review
because a newer revision exists or its recorded digest differs. The workflow
must create a new downstream revision even when the review concludes that its
body can remain unchanged. No mutable state file or event log may be required.

## Reader-review boundary case

Give a fresh agent a complete proposal whose acceptance depends on both a
decision maker and a skeptical peer. The run must use `document-reader-review`
after editorial stabilization, keep the author intent and plot from both
personas, preserve their reactions without proposing repairs, and route any
substantive response through `document-reader-revise`. A resulting content
change must return through the affected editorial passes before proof.
