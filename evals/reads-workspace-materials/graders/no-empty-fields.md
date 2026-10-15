---
type: regex
target: { source: file, path: docs/ideas.md }
pattern: '^[ \t>*-]*\**(cheapest test|stop if|kill criterion|самый дешёвый тест|самый дешевый тест|остановить, если|стоп, если|критерий остановки)\**:?\**:?[ \t]*(?=\r?\n(?![ \t]+\S)|(?![\s\S]))'
match: not_contains
flags: im
weight: 2
arm: both
---
