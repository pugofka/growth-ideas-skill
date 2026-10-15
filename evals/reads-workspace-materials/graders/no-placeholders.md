---
type: regex
target: { source: file, path: docs/ideas.md }
pattern: '\bTBD\b|\bTODO\b|\?\?\?|<[a-z ]+>'
match: not_contains
flags: i
weight: 1
arm: both
---
