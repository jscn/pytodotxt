# pytodotxt

pytodotxt is a Python library for interacting with todo.txt formatted
todo lists.

Basic usage:

````python
>>> from pytodotxt import List
>>> # Read a todo.txt-formatted file.
>>> tasks = List('todo.txt')
>>> print tasks
>>> ['(A) Call Mom @Phone +Family',
>>>  '(A) Schedule annual checkup +Health',
>>>  '(B) Outline chapter 5 +Novel @Computer',
>>>  '(C) Add cover sheets @Office +TPSReports',
>>>  'Plan backyard herb garden @Home',
>>>  'Pick up milk @GroceryStore',
>>>  'Research self-publishing services +Novel @Computer',
>>>  'x Download Todo.txt mobile app @Phone']

>>> # Find tasks for a given project
>>> print tasks.filter(project='Family')
>>> ['(A) Call Mom @Phone +Family']

>>> # Find all tasks for a given priority
>>> print tasks.filter(priority='A')
>>> ['(A) Call Mom @Phone +Family',
>>>  '(A) Schedule annual checkup +Health']

>>> # Combine filters
>>> print tasks.filter(priority='A', project='Health')
>>> ['(A) Call Mom @Phone +Family']
````

## Features

- Parses todo.txt compliant files.
- Provides filtering by project, context and priority.


## Installation

Install pytodotxt by running:

````
$ pip install pytodotxt
````

## Contribute

- Issue Tracker: github.com/pytodotxt/pytodotxt/issues
- Source Code: github.com/pytodotxt/pytodotxt


## License

The project is licensed under the GPL v3 license.
