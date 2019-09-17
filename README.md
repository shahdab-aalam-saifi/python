
# Python

## Programming Paradigm

* Structured
* Unstructured
* Object Oriented
* Event Driven etc.

## Installation

Core Python: https://www.python.org/downloads

Geany (IDE): https://www.geany.org/download/releases/

Ananconda Navigator: https://docs.anaconda.com/anaconda/install/

Style Guide: https://www.python.org/dev/peps/pep-0008/

## Basics

| A | Operator | Example |
|---|---|---|
| Comment |	`'''...'''` / `#`| `''' comments '''`/`# comments` |
| Exponentiation | `**` | `2**3` |
| Floor Division | `//` | `2//3` |
| Repetition | `*` | `"str"*2` |
| Identity | `is` | `a is int` |
| Membership | `in` | `"r" in "String"`|
| Slice | `:` | `lst[start:end-1:inc]` |

> Use `!` with expression, whereas `not` with Boolean conditions

### Data Types

- str
- int
- float
- bool
- list (mutable)
- tuple (immutable)

> First element in the list: `0`

> Last element in the list: `-1`

> `(100, )` is tuple

> `(100)` is set

### Functions

- id
- type
- print
- input
- bin

> **Object introspection**: Introspection is the ability to determine the type of an object at run-time.

### Sort

- `sorted(list)`
- `sorted(tuple, reverse=True)`

### List Comprehension

- List of squares: `[num * num for num in range(1, 11)]`
- List of squares of even numbers: `[num * num for num in range(1, 11) if num % 2 == 0]`