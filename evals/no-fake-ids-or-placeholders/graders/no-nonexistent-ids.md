---
type: regex
target: { source: file, path: docs/ideas.md }
pattern: '\bF([1-9][0-9]+|0)\b'
match: not_contains
weight: 2
arm: both
---
