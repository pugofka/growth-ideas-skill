---
type: llm
focus: { source: file, path: docs/ideas.md }
weight: 2
arm: both
---
PASS if every fact reference used in the document (labels such as F1, F2 or Ф1, Ф2) points to an entry that exists in the document's own list of facts, and the document has such a list whenever it uses such labels. FAIL if any label is cited but missing from the list. If the document uses no such labels, PASS.
