# English Lenses

Language: **English**. Follow each lens's role in the catalog. Mechanics can be
checked locally; diction also requires domain, audience, and house-style
judgment and must not be reduced to a blacklist.

These two lenses cover mechanical usage and diction. English composition rules
live beside them in [composition.md](composition.md), rather than being treated
as language-common.

---

## `en.mechanics`

### Purpose

Detect grammatical failures, punctuation that makes the intended relation
ambiguous, and departures from an explicit English house style. Usage that is
merely conventional belongs to editorial judgment unless the assignment fixes
one form.

### Consider

- Possessive or series punctuation inconsistent with the supplied convention.
- Parenthetic expressions whose boundary or restrictive meaning is ambiguous.
- Co-ordinate clauses whose boundary is not recoverable from their punctuation.
- Independent clauses joined by a comma.
- Sentences broken in two where one is required.
- Opening participial phrases that do not refer to the grammatical subject.

### Checks and conventions

- Apply a possessive convention consistently when the assignment, publisher,
  or existing document establishes one. *The service's owner* is uncontroversial;
  forms such as *Charles' request* and *Charles's request* are house-style
  choices unless the document mixes them.
- Apply a serial comma only when an explicit convention requires it, the
  document has already established it, or omitting it creates a real grouping
  ambiguity. Both *read, transform and write* and *read, transform, and write*
  are otherwise valid.
- Enclose a parenthetic expression on both sides when punctuation marks it as
  parenthetic. A restrictive clause takes no commas; changing restrictive
  status changes meaning and is not a style cleanup.
- Use the configured punctuation before a conjunction introducing a
  co-ordinate clause. Without such a convention, intervene only when the clause
  boundary is hard to recover.
- **No comma splice.** Two independent clauses take a semicolon, a period, or a
  conjunction — never a bare comma.
- A dependent fragment is a defect when it cannot stand as an intentional
  rhetorical fragment and its grammatical attachment is clear.
- **An opening participial phrase must refer to the grammatical subject.**
  *Having rebuilt the index, the query returned in 20ms* attributes the rebuild
  to the query. (A dangling opener whose referent cannot be recovered at all is
  also a `reference.antecedent` finding.)

### Reader impact

A house-style inconsistency has local impact. A comma splice that obscures the
clause boundary or a dangling participle that misattributes an action can
change the reader's understanding.

---

## `en.diction`

### Purpose

Find word choices and register inconsistencies that break the
conventions of English technical prose.

### Consider

- Words used in a sense their established usage does not carry.
- A summary that shifts tense without a change in time or viewpoint.
- Mixed American and British spelling.
- Contractions and register shifting within one document.
- Person and number shifting between sections.

### Boundaries

- Choosing between competing terms for one concept is
  terminology.consistency. This lens covers the word's register and form.
- Cutting an empty intensifier is prose.plain-expression.

### Rules

- **Use words in their established sense.** The recurring offenders in technical
  prose:
  - *all right* is two words.
  - *comprise* — prefer “the whole comprises the parts” or “the whole consists
    of the parts.” Treat “is comprised of” as a style choice unless the document
    uses the forms inconsistently or the relation becomes ambiguous.
  - *less* / *fewer* — prefer *fewer* for individually counted items and *less*
    for amounts. Keep established amount readings such as time, money, distance,
    measurements, and constructions such as “10 items or less.”
  - *which* / *that* — in American technical prose, prefer *that* for a
    restrictive clause and *which* with commas for a non-restrictive one. In
    British prose, restrictive *which* is established usage; preserve the
    document's chosen convention.
  - *effect* / *affect*, *principal* / *principle*, *complement* /
    *compliment*, *discreet* / *discrete*.
  - *literally* for emphasis, *utilize* where *use* is meant, *methodology*
    where *method* is meant.
  - *can* / *may* where capability and permission must be distinguished.
  - *divided into* / *composed of* where division and composition differ.
  - *fact* for a judgment that cannot be directly verified.
  - *phase* where *aspect* or *topic* is meant.
  - *while* where the reader cannot tell whether the relation is temporal,
    contrastive, or concessive.
  - *etc.* where omitted items are material and the reader cannot recover them.
  - *e.g.* / *i.e.* used interchangeably.
- **Keep one tense in a summary.** Shift tense only when the summarized sequence
  itself changes time or the document deliberately changes viewpoint.
- **Follow an explicit spelling convention.** When the assignment or existing
  document establishes American or British spelling, do not mix *behavior* and
  *behaviour* or *-ize* and *-ise*. Without that signal, a single valid form is
  not a defect.
- **Keep register coherent where a shift distracts the reader.** Contractions
  are acceptable in an informal register; a deliberate quoted voice or audience
  shift may justify local variation.
- **Keep person and number stable across one speaking position.** A shift among
  *we*, *you*, and impersonal form is a defect only when it obscures who acts or
  changes the reader relationship. `prose.voice` judges which position fits.

### Reader impact

Mixed register or spelling conventions can distract across a whole document.
An individual word choice usually has local impact unless it changes meaning.
