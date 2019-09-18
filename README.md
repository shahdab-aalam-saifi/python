
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
- iter
- next

> **Object introspection**: Introspection is the ability to determine the type of an object at run-time.

### Sort

- `sorted(list)`
- `sorted(tuple, reverse=True)`

### List Comprehension

- List of squares: `[num * num for num in range(1, 11)]`
- List of squares of even numbers: `[num * num for num in range(1, 11) if num % 2 == 0]`

### Sets

- Ways to create sets: `({})` and `{}`
- Functions: `add`, `discard`
- `|` - Union
- `&` - Intersection
- `-` - Minus

## Functions

### Syntax

```python
def func_name(param_name="default_value"):
    # perform action
    return
```

> Add two blank lines after defining a function

> `pass` is used to pass/return the control to calling function or if no action is require to be done by function

> `param=default_value` to define optional parameter with default value

> To pass arguments in any sequence use keyword parameters. e.g. `fun_name(param_name=value)` 

## Lamda (Anonymous function)

### Syntax

```python
lambda param: () # expression 
```

### Example

```python
lambda x,y: x + y
```

## Map
It maps the function to every object of the iterable.

### Syntax

```python
map("<function>", "<iterable>")
```

### Example

```python
map(lambda x: x*x, [x for x in range(10, 20)])
```

## Module

Define functions in a file and use in other files as logical group

- math
- sys

## File IO

```python
with open("<file_name>", "<mode>") as handle:
    # processing
    pass
```

## Exception

It is an event raise when an abnormal condition in a program resulting in the disruption in the flow of the program.

### Example

```python
try:
    # code
    pass
except IOError as err:
    # failure
    pass
else:
    # success
    pass
finally:
    # final block
    pass
```

## OOP

- `__init__`: initialize to variable or constructor
- `__str__`: use to define string representation on object
- `self`: current object
- `@static`: static property
- `@classmethod`: static method 

## Regular Expression

- `^` - start
- `$` - end
- `.` - single character
- `[]` - class
- `match` - match if string starts with pattern
- `search` - find anywhere
- `findall` - search all
- `split` - split
- `sub` - substitute
- `compile` - compile regular expression
- `r'pattern'`

## Generator

- `yield`

## Closure (Nested function)

## Decorators

- `@decorater_method`

## Filter

## Reduce

```python
from functools import reduce
```
## Frozenset

## Copy

```python
import copy
```

- `copy.copy()` - Shallow copy
- `copy.deepcopy()` - Deep copy