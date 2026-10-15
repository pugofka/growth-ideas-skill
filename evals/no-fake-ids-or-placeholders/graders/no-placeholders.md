---
type: regex
target: { source: file, path: docs/ideas.md }
pattern: '\bTBD\b|\bTODO\b|\?\?\?'
match: not_contains
weight: 1
arm: both
---
