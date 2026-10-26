import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Python Exam Prep Portal",
    page_icon="🐍",
    layout="centered"
)

# Comprehensive Syllabus & Extended Question Bank (15 Questions per Chapter)
syllabus_data = {
    "Unit 1: Python Basics & Sequences": {
        "chapters": {
            "Chapter 1.1: Introduction to Python & Basics": [
                "Features, setup environment, program structure",
                "Tokens: Keywords, Identifiers, Variables, Data types, Operators",
                "Scope and lifetime of variables"
            ],
            "Chapter 1.2: Conditional Statements & Loops": [
                "Indentation, If, If-Else, Switch concepts",
                "Looping: For, While, Nested Loops",
                "Jumping statements: break, continue"
            ],
            "Chapter 1.3: Python Sequences & Dictionaries": [
                "Lists: Accessing, slicing, modifying, list comprehension",
                "Tuples, Sets, Dictionaries (working, looping, nesting)",
                "Input/Output functions: print(), input(), comments"
            ],
            "Chapter 1.4: Functions & Advanced Iterables": [
                "Passing arguments, return values, arbitrary arguments (*args, **kwargs)",
                "Recursive & nested functions, default & flexible arguments",
                "Lambda, map(), filter(), reduce() functions, built-in functions"
            ]
        },
        "questions": {
            "Chapter 1.1: Introduction to Python & Basics": [
                {
                    "q": "Which of the following is a valid variable name in Python?",
                    "options": ["123var", "_var", "var-name", "class"],
                    "answer": "_var",
                    "explanation": "Variable names cannot start with numbers and cannot use reserved keywords or hyphens."
                },
                {
                    "q": "What is the output of type(10)?",
                    "options": ["<class 'float'>", "<class 'int'>", "<class 'str'>", "<class 'number'>"],
                    "answer": "<class 'int'>",
                    "explanation": "Whole numbers without decimals are integers (`int`)."
                },
                {
                    "q": "Which operator is used for exponentiation in Python?",
                    "options": ["^", "**", "//", "exp()"],
                    "answer": "**",
                    "explanation": "`**` raises the number to the power of the exponent."
                },
                {
                    "q": "What is the correct file extension for Python source files?",
                    "options": [".pt", ".pyt", ".py", ".python"],
                    "answer": ".py",
                    "explanation": "Python source code files use the `.py` extension."
                },
                {
                    "q": "Which of the following is an explicit line continuation character in Python?",
                    "options": ["/", "\\", "#", ";"],
                    "answer": "\\",
                    "explanation": "A backslash `\\` is used to split a long logical line into multiple physical lines."
                },
                {
                    "q": "What is the output of bool(0)?",
                    "options": ["True", "False", "None", "Error"],
                    "answer": "False",
                    "explanation": "Integer `0` evaluates to `False` in Boolean contexts."
                },
                {
                    "q": "Which keyword is used to display output to the console?",
                    "options": ["echo()", "print()", "display()", "write()"],
                    "answer": "print()",
                    "explanation": "`print()` is the built-in function to output text or values."
                },
                {
                    "q": "What is the result of expression 10 // 3?",
                    "options": ["3.33", "3", "4", "3.0"],
                    "answer": "3",
                    "explanation": "`//` is the floor division operator, rounding down to the nearest integer."
                },
                {
                    "q": "Which built-in function gets the length of an object like a string or list?",
                    "options": ["size()", "length()", "len()", "count()"],
                    "answer": "len()",
                    "explanation": "`len()` returns the number of items in an object."
                },
                {
                    "q": "Are variable names case-sensitive in Python?",
                    "options": ["Yes", "No", "Only inside functions", "Only for strings"],
                    "answer": "Yes",
                    "explanation": "Python treats `Var` and `var` as two completely different identifiers."
                },
                {
                    "q": "Which of these data types represents a sequence of characters?",
                    "options": ["int", "str", "float", "bool"],
                    "answer": "str",
                    "explanation": "`str` (string) handles text data."
                },
                {
                    "q": "What is the scope of a variable declared inside a function without global keyword?",
                    "options": ["Global", "Local", "Enclosing", "Built-in"],
                    "answer": "Local",
                    "explanation": "Variables defined inside a function are local to that function scope."
                },
                {
                    "q": "Which function converts a string representation of a number into an integer?",
                    "options": ["str()", "float()", "int()", "num()"],
                    "answer": "int()",
                    "explanation": "`int('10')` converts the string into an integer `10`."
                },
                {
                    "q": "Which operator checks if two variables point to the same object in memory?",
                    "options": ["==", "is", "equals", "match"],
                    "answer": "is",
                    "explanation": "The identity operator `is` evaluates to True if operands refer to the same object."
                },
                {
                    "q": "Which type of comment is created using a hash symbol `#`?",
                    "options": ["Single-line comment", "Multi-line comment", "Docstring", "Block comment"],
                    "answer": "Single-line comment",
                    "explanation": "`#` creates a comment for a single line."
                }
            ],
            "Chapter 1.2: Conditional Statements & Loops": [
                {
                    "q": "Which keyword is used for conditional branching other than if and else?",
                    "options": ["elseif", "elif", "elsif", "case"],
                    "answer": "elif",
                    "explanation": "Python uses `elif` for multiple conditional checks."
                },
                {
                    "q": "Which loop executes a block of code as long as a condition remains true?",
                    "options": ["for loop", "while loop", "do-while loop", "foreach loop"],
                    "answer": "while loop",
                    "explanation": "`while` checks the condition before every iteration."
                },
                {
                    "q": "Which statement skips the current iteration and jumps to the next loop cycle?",
                    "options": ["break", "pass", "continue", "skip"],
                    "answer": "continue",
                    "explanation": "`continue` bypasses the rest of the current iteration block."
                },
                {
                    "q": "What does the `pass` statement do in Python?",
                    "options": ["Terminates program", "Does nothing / acts as a placeholder", "Skips loop", "Returns none"],
                    "answer": "Does nothing / acts as a placeholder",
                    "explanation": "`pass` is a null statement used when syntax requires a statement but no code needs to run."
                },
                {
                    "q": "Which function generates a sequence of numbers, commonly used in `for` loops?",
                    "options": ["sequence()", "range()", "iter()", "loop()"],
                    "answer": "range()",
                    "explanation": "`range(start, stop, step)` generates number sequences."
                },
                {
                    "q": "Can you nest a `while` loop inside a `for` loop?",
                    "options": ["Yes", "No", "Only in functions", "Only with tuples"],
                    "answer": "Yes",
                    "explanation": "Python allows complete nesting of any loops and conditional statements."
                },
                {
                    "q": "What happens if the condition in a `while` loop never evaluates to False?",
                    "options": ["Syntax error", "Infinite loop", "Zero division error", "Graceful exit"],
                    "answer": "Infinite loop",
                    "explanation": "An unchanging condition results in an endless loop execution."
                },
                {
                    "q": "How is code block indentation specified in Python?",
                    "options": ["Curly braces {}", "Parentheses ()", "Whitespace / Tabs", "Semicolons ;"],
                    "answer": "Whitespace / Tabs",
                    "explanation": "Python relies heavily on indentation to define blocks of code."
                },
                {
                    "q": "Which keyword starts an alternative block if all preceding conditions are false?",
                    "options": ["else", "otherwise", "default", "fallback"],
                    "answer": "else",
                    "explanation": "`else` catches all remaining fallback conditions."
                },
                {
                    "q": "What is the output of: `for i in range(1): print(i, end='')`?",
                    "options": ["0", "1", "01", "None"],
                    "answer": "0",
                    "explanation": "`range(1)` generates numbers starting from 0 up to, but excluding, 1."
                },
                {
                    "q": "Which operator is used to combine multiple conditions (logical AND)?",
                    "options": ["and", "&", "&&", "PLUS"],
                    "answer": "and",
                    "explanation": "The logical keyword `and` returns True if both conditions are true."
                },
                {
                    "q": "What does logical operator `not` do?",
                    "options": ["Inverts boolean value", "Deletes variable", "Multiplies value", "Adds negative sign"],
                    "answer": "Inverts boolean value",
                    "explanation": "`not True` evaluates to `False` and vice-versa."
                },
                {
                    "q": "Which loop is best suited for iterating over a known sequence or collection?",
                    "options": ["while loop", "for loop", "infinite loop", "goto loop"],
                    "answer": "for loop",
                    "explanation": "`for` loops iterate directly over items in any iterable collection."
                },
                {
                    "q": "Can a `for` loop include an `else` block?",
                    "options": ["Yes, executes when loop completes normally without break", "No", "Only in Python 2", "Causes error"],
                    "answer": "Yes, executes when loop completes normally without break",
                    "explanation": "Python `for...else` blocks run the else clause if the loop wasn't terminated by a `break`."
                },
                {
                    "q": "What is indentation error called in Python?",
                    "options": ["SyntaxError", "IndentationError", "TypeError", "BlockError"],
                    "answer": "IndentationError",
                    "explanation": "Improper spacing or mixed tabs/spaces triggers an `IndentationError`."
                }
            ],
            "Chapter 1.3: Python Sequences & Dictionaries": [
                {
                    "q": "Which collection type is mutable and ordered?",
                    "options": ["Tuple", "List", "String", "Set"],
                    "answer": "List",
                    "explanation": "Lists allow items to be modified, added, or removed after creation."
                },
                {
                    "q": "Which brackets are used to define a tuple?",
                    "options": ["[]", "{}", "()", "<>"],
                    "answer": "()",
                    "explanation": "Tuples are defined using parentheses `()`."
                },
                {
                    "q": "How do you access the last element of a list named `lst`?",
                    "options": ["lst[0]", "lst[-1]", "lst[last]", "lst.end()"],
                    "answer": "lst[-1]",
                    "explanation": "Negative indexing `-1` accesses the final element of a sequence."
                },
                {
                    "q": "Which method adds an item to the end of a list?",
                    "options": ["add()", "append()", "insert()", "push()"],
                    "answer": "append()",
                    "explanation": "`append()` adds a single element to the end of a list."
                },
                {
                    "q": "Which data structure stores unique elements with no duplicates?",
                    "options": ["List", "Tuple", "Set", "Dictionary"],
                    "answer": "Set",
                    "explanation": "Sets automatically filter out duplicate values."
                },
                {
                    "q": "How are values stored inside a dictionary?",
                    "options": ["Index positions", "Key-value pairs", "Queues", "Linked nodes"],
                    "answer": "Key-value pairs",
                    "explanation": "Dictionaries map unique keys to corresponding values."
                },
                {
                    "q": "Which method removes and returns the last item of a list by default?",
                    "options": ["remove()", "delete()", "pop()", "clear()"],
                    "answer": "pop()",
                    "explanation": "`pop()` removes an item at a given index (defaulting to the last item)."
                },
                {
                    "q": "Are tuples mutable?",
                    "options": ["Yes", "No", "Only when empty", "Only in functions"],
                    "answer": "No",
                    "explanation": "Tuples are immutable sequence objects."
                },
                {
                    "q": "What does list slicing `lst[1:4]` return?",
                    "options": ["Elements at index 1, 2, 3", "Elements at index 1, 2, 3, 4", "Only index 1 and 4", "Error"],
                    "answer": "Elements at index 1, 2, 3",
                    "explanation": "Slice upper bounds are exclusive in Python."
                },
                {
                    "q": "Which function takes user input from the console as a string?",
                    "options": ["scan()", "input()", "read()", "get()"],
                    "answer": "input()",
                    "explanation": "`input()` prompts the user and returns the entered value as a string."
                },
                {
                    "q": "How do you check if a key exists in a dictionary `d`?",
                    "options": ["key in d", "d.has(key)", "d.contains(key)", "find(key)"],
                    "answer": "key in d",
                    "explanation": "The `in` operator efficiently checks dictionary keys."
                },
                {
                    "q": "What is list comprehension syntax shortcut used for?",
                    "options": ["Creating lists concisely", "Sorting dictionaries", "Deleting tuples", "Reading files"],
                    "answer": "Creating lists concisely",
                    "explanation": "List comprehensions offer a compact way to build lists based on existing iterables."
                },
                {
                    "q": "Which method returns all keys of a dictionary?",
                    "options": ["d.values()", "d.keys()", "d.items()", "d.all()"],
                    "answer": "d.keys()",
                    "explanation": "`keys()` provides a view object of all keys."
                },
                {
                    "q": "Can sets contain mutable items like lists?",
                    "options": ["Yes", "No", "Only empty lists", "Only numbers"],
                    "answer": "No",
                    "explanation": "Set elements must be hashable (immutable)."
                },
                {
                    "q": "How do you clear all elements from a list?",
                    "options": ["lst.clear()", "lst.empty()", "delete lst", "lst.reset()"],
                    "answer": "lst.clear()",
                    "explanation": "`clear()` removes all items from the list."
                }
            ],
            "Chapter 1.4: Functions & Advanced Iterables": [
                {
                    "q": "Which keyword defines a user-defined function?",
                    "options": ["func", "define", "def", "lambda"],
                    "answer": "def",
                    "explanation": "`def` is the standard keyword for defining functions."
                },
                {
                    "q": "What does an anonymous `lambda` function return?",
                    "options": ["Nothing", "An expression result", "A list", "True/False"],
                    "answer": "An expression result",
                    "explanation": "Lambda functions evaluate and return the result of their single expression."
                },
                {
                    "q": "Which function applies a given function to all items in an iterable?",
                    "options": ["filter()", "map()", "reduce()", "apply()"],
                    "answer": "map()",
                    "explanation": "`map(func, iter)` maps the function across all iterable elements."
                },
                {
                    "q": "Which function extracts elements from an iterable where a function returns True?",
                    "options": ["filter()", "select()", "extract()", "search()"],
                    "answer": "filter()",
                    "explanation": "`filter()` filters elements based on a boolean condition function."
                },
                {
                    "q": "Which module must be imported to use `reduce()` in Python 3?",
                    "options": ["math", "functools", "itertools", "collections"],
                    "answer": "functools",
                    "explanation": "`reduce()` is housed in the `functools` module."
                },
                {
                    "q": "What do `*args` allow a function to accept?",
                    "options": ["Keyword arguments", "A variable number of positional arguments", "Only lists", "Default values"],
                    "answer": "A variable number of positional arguments",
                    "explanation": "`*args` packs extra positional arguments into a tuple."
                },
                {
                    "q": "What do `**kwargs` allow a function to accept?",
                    "options": ["Positional arguments", "Variable keyword arguments", "File streams", "Integer arrays"],
                    "answer": "Variable keyword arguments",
                    "explanation": "`**kwargs` packs extra keyword arguments into a dictionary."
                },
                {
                    "q": "What is a recursive function?",
                    "options": ["A function that calls itself", "A function with loops", "A built-in function", "An anonymous function"],
                    "answer": "A function that calls itself",
                    "explanation": "Recursion occurs when a function invokes itself to solve sub-problems."
                },
                {
                    "q": "What happens if a recursive function lacks a base case?",
                    "options": ["RecursionError / Infinite recursion", "SyntaxError", "Runs faster", "Returns None"],
                    "answer": "RecursionError / Infinite recursion",
                    "explanation": "Without a base termination condition, recursion exceeds maximum stack depth."
                },
                {
                    "q": "Can functions be nested inside other functions in Python?",
                    "options": ["Yes", "No", "Only with lambda", "Only in classes"],
                    "answer": "Yes",
                    "explanation": "Python supports inner/nested helper functions."
                },
                {
                    "q": "What is a default argument in a function definition?",
                    "options": ["An argument with a pre-assigned fallback value", "A mandatory parameter", "A keyword only arg", "None"],
                    "answer": "An argument with a pre-assigned fallback value",
                    "explanation": "Default arguments are used if no value is passed during function call."
                },
                {
                    "q": "Which statement sends a value back from a function to its caller?",
                    "options": ["send", "return", "output", "yield"],
                    "answer": "return",
                    "explanation": "`return` exits the function and passes back the result."
                },
                {
                    "q": "What is the return type of a function without a return statement?",
                    "options": ["int", "None", "False", "0"],
                    "answer": "None",
                    "explanation": "Functions without explicit return statements implicitly return `None`."
                },
                {
                    "q": "Can a function return multiple values?",
                    "options": ["Yes, as a tuple", "No", "Only using lists", "Only using dictionaries"],
                    "answer": "Yes, as a tuple",
                    "explanation": "Returning comma-separated values packs them into a tuple automatically."
                },
                {
                    "q": "Which built-in function returns an iterator of index-value pairs from a sequence?",
                    "options": ["zip()", "enumerate()", "map()", "pair()"],
                    "answer": "enumerate()",
                    "explanation": "`enumerate()` adds a counter index to an iterable."
                }
            ]
        },
        "coding_exercises": [
            {
                "title": "Twin Primes Generator (Lab Exp 1a)",
                "desc": "Write a Python program to print all twin prime pairs less than 1000. Two consecutive odd numbers that are both prime are known as twin primes (e.g., (3, 5), (5, 7), (11, 13)).",
                "solution": '''def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

print("Twin primes less than 1000:")
for i in range(2, 1000):
    if is_prime(i) and is_prime(i + 2):
        print(f"({i}, {i+2})")'''
            },
            {
                "title": "Permutations and Combinations Calculator (Lab Exp 1b)",
                "desc": "Write a Python program to implement permutation P(n,r) = n! / (n-r)! and combination C(n,r) = n! / (r!*(n-r)!) using user-defined functions.",
                "solution": '''import math

def permutation(n, r):
    return math.factorial(n) // math.factorial(n - r)

def combination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

n = int(input("Enter n: "))
r = int(input("Enter r: "))
print(f"Permutation P({n},{r}) = {permutation(n, r)}")
print(f"Combination C({n},{r}) = {combination(n, r)}")'''
            },
            {
                "title": "User Management Portal using Dictionaries (Lab Exp 2b)",
                "desc": "Write a Python script to store user details (user id as key, with dictionary value containing username and age). Allow searching user details by entered user id.",
                "solution": '''users = {
    101: {"name": "Aarav", "age": 20},
    102: {"name": "Priya", "age": 21},
    103: {"name": "Rohan", "age": 19}
}

uid = int(input("Enter User ID to search (101, 102, 103): "))
if uid in users:
    print(f"User Found -> Name: {users[uid]['name']}, Age: {users[uid]['age']}")
else:
    print("User ID not found!")'''
            }
        ]
    },
    "Unit 2: Object-Oriented Programming & Data Analytics": {
        "chapters": {
            "OOP Concepts": [
                "Creating and using classes and instances",
                "Public and private members",
                "Inheritance, types of inheritance, polymorphism",
                "Importing classes, Python Standard Library"
            ],
            "Introduction to Data Analytics & NumPy": [
                "Data analytics requirements in Python",
                "NumPy Ndarray, array creation, data types, attributes",
                "NumPy operations, mathematical and statistical functions"
            ],
            "Pandas & Matplotlib Visualization": [
                "Pandas Series & DataFrame, viewing data",
                "Finding missing values, dropping null values (dropna, fillna)",
                "Matplotlib plots: Line, Bar, Hist, Scatter, Pie, Box plot, Violin graph"
            ]
        },
        "questions": {
            "OOP Concepts": [
                {
                    "q": "Which keyword is used to create a class in Python?",
                    "options": ["object", "class", "def", "struct"],
                    "answer": "class",
                    "explanation": "`class` defines a user-defined blueprint for objects."
                },
                {
                    "q": "What is the special constructor method in Python classes?",
                    "options": ["__new__", "__init__", "__main__", "__construct__"],
                    "answer": "__init__",
                    "explanation": "`__init__` initializes attributes when an object is instantiated."
                },
                {
                    "q": "What represents the instance reference parameter inside class methods?",
                    "options": ["this", "self", "me", "instance"],
                    "answer": "self",
                    "explanation": "`self` refers to the current object instance being operated on."
                },
                {
                    "q": "How do you denote a private member attribute in Python?",
                    "options": ["_attr", "__attr", "private attr", "#attr"],
                    "answer": "__attr",
                    "explanation": "Double underscores trigger name mangling for private members."
                },
                {
                    "q": "What object-oriented pillar allows a child class to inherit parent attributes/methods?",
                    "options": ["Polymorphism", "Encapsulation", "Inheritance", "Abstraction"],
                    "answer": "Inheritance",
                    "explanation": "Inheritance enables code reuse through parent-child class hierarchies."
                },
                {
                    "q": "What feature allows methods in different classes to have the same name with different behaviors?",
                    "options": ["Polymorphism", "Overloading", "Encapsulation", "Inheritance"],
                    "answer": "Polymorphism",
                    "explanation": "Polymorphism means 'many forms', allowing uniform interface across types."
                },
                {
                    "q": "How do you import a specific class `MyClass` from a module `mod.py`?",
                    "options": ["import MyClass from mod", "from mod import MyClass", "get MyClass from mod", "include mod.MyClass"],
                    "answer": "from mod import MyClass",
                    "explanation": "`from module import name` imports specific components."
                },
                {
                    "q": "Which function checks if an object is an instance of a specific class?",
                    "options": ["isinstance()", "typecheck()", "checkclass()", "classof()"],
                    "answer": "isinstance()",
                    "explanation": "`isinstance(obj, Class)` verifies object typing."
                },
                {
                    "q": "Can a Python class inherit from multiple parent classes?",
                    "options": ["Yes (Multiple inheritance)", "No", "Only two parents max", "Only interfaces"],
                    "answer": "Yes (Multiple inheritance)",
                    "explanation": "Python supports multiple inheritance parent lists."
                },
                {
                    "q": "Which built-in function returns a string representation of an object for debugging?",
                    "options": ["__str__", "__repr__", "__display__", "__string__"],
                    "answer": "__repr__",
                    "explanation": "`__repr__` provides an official string representation."
                },
                {
                    "q": "What is encapsulation in OOP?",
                    "options": ["Hiding data and bundling methods together", "Copying classes", "Deleting instances", "Multiple inheritance"],
                    "answer": "Hiding data and bundling methods together",
                    "explanation": "Encapsulation restricts direct access and bundles data protection."
                },
                {
                    "q": "Which function gets the attributes and methods of an object?",
                    "options": ["dir()", "list()", "show()", "attrs()"],
                    "answer": "dir()",
                    "explanation": "`dir()` returns a list of valid attributes for an object."
                },
                {
                    "q": "How do you invoke a parent class method from a child class?",
                    "options": ["parent.method()", "super().method()", "base.method()", "this.parent()"],
                    "answer": "super().method()",
                    "explanation": "`super()` proxies method calls to parent classes."
                },
                {
                    "q": "Are class attributes shared across all instances of a class?",
                    "options": ["Yes", "No, unique per instance", "Only in private mode", "Only with methods"],
                    "answer": "Yes",
                    "explanation": "Class attributes belong to the class itself and are shared by all objects."
                },
                {
                    "q": "Which module is part of Python's Standard Library for math operations?",
                    "options": ["math", "numpy_std", "calc", "numeric"],
                    "answer": "math",
                    "explanation": "`math` is a built-in standard library module."
                }
            ],
            "Introduction to Data Analytics & NumPy": [
                {
                    "q": "What is the core data structure in NumPy for multi-dimensional arrays?",
                    "options": ["pd.DataFrame", "np.ndarray", "list", "matrix"],
                    "answer": "np.ndarray",
                    "explanation": "`ndarray` is NumPy's optimized N-dimensional array container."
                },
                {
                    "q": "How do you import NumPy with standard alias `np`?",
                    "options": ["import numpy", "import numpy as np", "load numpy as np", "using numpy"],
                    "answer": "import numpy as np",
                    "explanation": "`import numpy as np` is the universal community convention."
                },
                {
                    "q": "Which NumPy array attribute gives the dimensions (rows, columns) shape?",
                    "options": ["array.size", "array.shape", "array.dim", "array.length"],
                    "answer": "array.shape",
                    "explanation": "`shape` returns a tuple representing array dimensions."
                },
                {
                    "q": "What function creates an array filled entirely with zeros in NumPy?",
                    "options": ["np.empty()", "np.zeros()", "np.ones()", "np.null()"],
                    "answer": "np.zeros()",
                    "explanation": "`np.zeros(shape)` initializes an array of zeros."
                },
                {
                    "q": "Which NumPy function calculates the arithmetic mean of an array?",
                    "options": ["np.average()", "np.mean()", "np.median()", "np.sum()"],
                    "answer": "np.mean()",
                    "explanation": "`np.mean()` computes the average value."
                },
                {
                    "q": "What is vectorization in NumPy?",
                    "options": ["Looping in Python", "Executing operations on entire arrays without explicit loops in Python C-code", "Plotting vectors", "Compressing files"],
                    "answer": "Executing operations on entire arrays without explicit loops in Python C-code",
                    "explanation": "Vectorized operations run compiled C code for high performance."
                },
                {
                    "q": "Which function generates evenly spaced values within a given interval?",
                    "options": ["np.range()", "np.linspace()", "np.sequence()", "np.steps()"],
                    "answer": "np.linspace()",
                    "explanation": "`np.linspace(start, stop, num)` generates evenly spaced numbers."
                },
                {
                    "q": "What attribute returns the total number of elements in a NumPy array?",
                    "options": ["ndim", "size", "itemsize", "dtype"],
                    "answer": "size",
                    "explanation": "`size` gives total element count (`rows * columns`)."
                },
                {
                    "q": "Which function computes the square root of each element in a NumPy array?",
                    "options": ["np.power()", "np.sqrt()", "np.square()", "math.sqrt()"],
                    "answer": "np.sqrt()",
                    "explanation": "`np.sqrt()` is a universal vectorized mathematical function."
                },
                {
                    "q": "How do you transpose a NumPy matrix/array?",
                    "options": ["arr.flip()", "arr.T", "arr.reverse()", "arr.rotate()"],
                    "answer": "arr.T",
                    "explanation": "The `.T` attribute returns the transposed array."
                },
                {
                    "q": "Which function reshapes a NumPy array without changing its data?",
                    "options": ["arr.resize()", "arr.reshape()", "arr.convert()", "arr.transform()"],
                    "answer": "arr.reshape()",
                    "explanation": "`reshape(r, c)` alters dimensions while retaining data order."
                },
                {
                    "q": "What data type attribute checks the internal item type of a NumPy array?",
                    "options": ["type", "dtype", "kind", "format"],
                    "answer": "dtype",
                    "explanation": "`dtype` specifies data types like `int64` or `float64`."
                },
                {
                    "q": "What is broadcasting in NumPy?",
                    "options": ["Sending data over network", "How NumPy treats arrays with different shapes during arithmetic operations", "Printing arrays", "Matrix multiplication"],
                    "answer": "How NumPy treats arrays with different shapes during arithmetic operations",
                    "explanation": "Broadcasting allows arithmetic between arrays of differing sizes under specific rules."
                },
                {
                    "q": "Which function finds the maximum value in a NumPy array?",
                    "options": ["np.max()", "np.high()", "np.maximum_val()", "np.top()"],
                    "answer": "np.max()",
                    "explanation": "`np.max()` returns the highest element."
                },
                {
                    "q": "What NumPy function generates random values between 0 and 1?",
                    "options": ["np.random.rand()", "np.random.randint()", "np.rand()", "np.random()"],
                    "answer": "np.random.rand()",
                    "explanation": "`np.random.rand()` creates uniform random floats."
                }
            ],
            "Pandas & Matplotlib Visualization": [
                {
                    "q": "What is a 1D labeled array structure in Pandas called?",
                    "options": ["DataFrame", "Series", "Panel", "Vector"],
                    "answer": "Series",
                    "explanation": "A Pandas `Series` is a one-dimensional labeled homogeneous array."
                },
                {
                    "q": "What is a 2D tabular data structure with labeled axes in Pandas called?",
                    "options": ["Series", "DataFrame", "Matrix", "Sheet"],
                    "answer": "DataFrame",
                    "explanation": "A `DataFrame` is a 2D tabular data structure."
                },
                {
                    "q": "Which Pandas method displays the first few rows of a DataFrame?",
                    "options": ["top()", "head()", "start()", "first()"],
                    "answer": "head()",
                    "explanation": "`df.head(n)` returns the first `n` rows (default 5)."
                },
                {
                    "q": "Which function replaces missing/null values in a Pandas DataFrame?",
                    "options": ["dropna()", "fillna()", "removenull()", "clean()"],
                    "answer": "fillna()",
                    "explanation": "`fillna()` replaces `NaN` entries with specified values."
                },
                {
                    "q": "Which Pandas function removes rows containing missing values?",
                    "options": ["dropna()", "delna()", "cleanna()", "stripna()"],
                    "answer": "dropna()",
                    "explanation": "`dropna()` drops rows or columns with missing data."
                },
                {
                    "q": "Which Matplotlib plot type is best for showing trends over time?",
                    "options": ["Bar chart", "Line plot", "Pie chart", "Histogram"],
                    "answer": "Line plot",
                    "explanation": "Line plots connect sequential data points to reveal continuous trends."
                },
                {
                    "q": "What Matplotlib class represents an individual graph plot canvas area?",
                    "options": ["Figure", "Axes", "Canvas", "Plot"],
                    "answer": "Axes",
                    "explanation": "The `Axes` object contains the actual data space, labels, and ticks."
                },
                {
                    "q": "How do you add a title to a Matplotlib plot?",
                    "options": ["plt.title()", "plt.header()", "plt.name()", "plt.label()"],
                    "answer": "plt.title()",
                    "explanation": "`plt.title('Text')` sets the plot title."
                },
                {
                    "q": "Which plot displays frequency distributions of continuous numerical data?",
                    "options": ["Scatter plot", "Histogram", "Pie chart", "Bar plot"],
                    "answer": "Histogram",
                    "explanation": "Histograms group numerical data into bins to show data density."
                },
                {
                    "q": "Which plot compares proportions of categories using circular slices?",
                    "options": ["Pie chart", "Box plot", "Line plot", "Heatmap"],
                    "answer": "Pie chart",
                    "explanation": "Pie charts illustrate percentage shares of a whole."
                },
                {
                    "q": "Which Pandas function reads a CSV file into a DataFrame?",
                    "options": ["pd.open_csv()", "pd.read_csv()", "pd.load_csv()", "pd.import_csv()"],
                    "answer": "pd.read_csv()",
                    "explanation": "`pd.read_csv('file.csv')` parses comma-separated files into DataFrames."
                },
                {
                    "q": "How do you select a single column named 'Salary' from DataFrame `df`?",
                    "options": ["df.Salary or df['Salary']", "df.get('Salary')", "df(Salary)", "df[Salary]"],
                    "answer": "df.Salary or df['Salary']",
                    "explanation": "Columns can be accessed using dot notation or bracket string indexing."
                },
                {
                    "q": "Which plot displays data spread, median, and outliers using quartiles?",
                    "options": ["Box plot", "Scatter plot", "Bar chart", "Line plot"],
                    "answer": "Box plot",
                    "explanation": "Box plots summarize distributions via five-number summaries and outliers."
                },
                {
                    "q": "How do you show a created Matplotlib plot window?",
                    "options": ["plt.display()", "plt.show()", "plt.render()", "plt.open()"],
                    "answer": "plt.show()",
                    "explanation": "`plt.show()` opens the figure GUI window."
                },
                {
                    "q": "Which Matplotlib function creates multiple subplots in one figure window?",
                    "options": ["plt.subplots()", "plt.multigraph()", "plt.grid_plots()", "plt.panels()"],
                    "answer": "plt.subplots()",
                    "explanation": "`plt.subplots(nrows, ncols)` sets up grid subplots."
                }
            ]
        },
        "coding_exercises": [
            {
                "title": "Student Class Implementation (Lab Exp 3)",
                "desc": "Implement a Student class with information such as rollno, name, and class. Accept input from the user and display student details.",
                "solution": '''class Student:
    def __init__(self, rollno, name, student_class):
        self.rollno = rollno
        self.name = name
        self.student_class = student_class

    def display(self):
        print(f"Roll No: {self.rollno} | Name: {self.name} | Class: {self.student_class}")

r = input("Enter Roll No: ")
n = input("Enter Name: ")
c = input("Enter Class: ")

s = Student(r, n, c)
s.display()'''
            },
            {
                "title": "Swap Two Columns in NumPy Array (Lab Exp 4a)",
                "desc": "Write a NumPy script to create a 3x3 matrix and swap column 0 with column 2.",
                "solution": '''import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Matrix:\\n", arr)

# Swap column 0 and column 2
arr[:, [0, 2]] = arr[:, [2, 0]]
print("Matrix after swapping columns 0 and 2:\\n", arr)'''
            },
            {
                "title": "Pandas DataFrame Missing Value Handler (Lab Exp 4b)",
                "desc": "Create an employee DataFrame with Department and Salary columns (containing some missing NaN values). Filter rows where Department is 'Sales' and fill missing salaries with the median.",
                "solution": '''import pandas as pd
import numpy as np

data = {
    'Name': ['Amit', 'Pooja', 'Rahul', 'Neha'],
    'Department': ['Sales', 'HR', 'Sales', 'Sales'],
    'Salary': [50000, 60000, np.nan, 55000]
}
df = pd.DataFrame(data)

# Filter Sales department
sales_df = df[df['Department'] == 'Sales'].copy()

# Fill missing salary with median
median_sal = sales_df['Salary'].median()
sales_df['Salary'] = sales_df['Salary'].fillna(median_sal)

print(sales_df)'''
            }
        ]
    },
    "Unit 3: GUI Programming & Advanced Visualization": {
        "chapters": {
            "Chapter 3.1: GUI Programming using Tkinter": [
                "Tkinter setup, simple Tkinter window, event processing",
                "Widget classes, canvas, geometry managers (pack, grid, place)",
                "Display images, menus, popup menus, mouse & key events/bindings"
            ],
            "Chapter 3.2: Visualization with Seaborn & Plotly": [
                "Seaborn: Relational, categorical, distribution, and matrix plots",
                "Plotly: Line, bar, scatter, histogram, violin, gantt, heatmap, 3D graphs"
            ]
        },
        "questions": {
            "Chapter 3.1: GUI Programming using Tkinter": [
                {
                    "q": "What is Tkinter in Python?",
                    "options": ["A database engine", "Standard built-in GUI library", "A web framework", "A machine learning library"],
                    "answer": "Standard built-in GUI library",
                    "explanation": "Tkinter is Python's standard graphical user interface package."
                },
                {
                    "q": "How do you initialize the main application window in Tkinter?",
                    "options": ["tk.window()", "tk.Tk()", "tk.start()", "tk.gui()"],
                    "answer": "tk.Tk()",
                    "explanation": "`root = tk.Tk()` creates the main root application window."
                },
                {
                    "q": "Which Tkinter geometry manager places widgets in rows and columns like a spreadsheet table?",
                    "options": ["pack()", "grid()", "place()", "align()"],
                    "answer": "grid()",
                    "explanation": "`grid()` uses row and column indices for layout positioning."
                },
                {
                    "q": "Which Tkinter geometry manager places widgets using explicit (X, Y) pixel coordinates?",
                    "options": ["pack()", "grid()", "place()", "absolute()"],
                    "answer": "place()",
                    "explanation": "`place()` specifies exact pixel coordinates (`x`, `y`)."
                },
                {
                    "q": "Which geometry manager packs widgets sequentially (top, bottom, left, right)?",
                    "options": ["pack()", "grid()", "place()", "flow()"],
                    "answer": "pack()",
                    "explanation": "`pack()` organizes widgets in blocks before placing them in parent containers."
                },
                {
                    "q": "What method starts the Tkinter event loop to keep the window open?",
                    "options": ["root.run()", "root.mainloop()", "root.start()", "root.listen()"],
                    "answer": "root.mainloop()",
                    "explanation": "`mainloop()` runs the event listener loop handling mouse clicks and key presses."
                },
                {
                    "q": "Which widget is used to display static text or images in Tkinter?",
                    "options": ["Button", "Label", "Entry", "Canvas"],
                    "answer": "Label",
                    "explanation": "`Label` widgets display uneditable text or images."
                },
                {
                    "q": "Which widget accepts single-line text input from users?",
                    "options": ["Text", "Entry", "InputBox", "Field"],
                    "answer": "Entry",
                    "explanation": "`Entry` provides a single-line text input box."
                },
                {
                    "q": "Which widget allows multi-line text input and editing?",
                    "options": ["Entry", "Text", "Area", "Memo"],
                    "answer": "Text",
                    "explanation": "`Text` supports multi-line formatted text editing."
                },
                {
                    "q": "How do you bind mouse clicks or key events to a Tkinter widget?",
                    "options": ["widget.bind()", "widget.listen()", "widget.event()", "widget.click()"],
                    "answer": "widget.bind()",
                    "explanation": "`widget.bind('<Button-1>', handler)` attaches event handlers."
                },
                {
                    "q": "Which widget creates clickable push buttons in Tkinter?",
                    "options": ["Command", "Button", "Action", "Clicker"],
                    "answer": "Button",
                    "explanation": "`Button` triggers functions when clicked."
                },
                {
                    "q": "What option links a button click to a Python function?",
                    "options": ["action=", "command=", "function=", "call="],
                    "answer": "command=",
                    "explanation": "The `command` parameter specifies the callback function."
                },
                {
                    "q": "Which widget is used for drawing shapes, lines, and images in Tkinter?",
                    "options": ["Frame", "Canvas", "Panel", "Board"],
                    "answer": "Canvas",
                    "explanation": "Canvas provides structured graphics drawing capabilities."
                },
                {
                    "q": "How do you create drop-down menus in a Tkinter application window?",
                    "options": ["Menu widget", "Dropdown widget", "List widget", "Select widget"],
                    "answer": "Menu widget",
                    "explanation": "Tkinter `Menu` creates top menus and popup context menus."
                },
                {
                    "q": "What method closes and destroys a Tkinter window programmatically?",
                    "options": ["root.close()", "root.destroy()", "root.exit()", "root.quit_window()"],
                    "answer": "root.destroy()",
                    "explanation": "`destroy()` cleans up and terminates the Tkinter mainloop window."
                }
            ],
            "Chapter 3.2: Visualization with Seaborn & Plotly": [
                {
                    "q": "What library is Seaborn built on top of?",
                    "options": ["Plotly", "Matplotlib", "Tkinter", "NumPy"],
                    "answer": "Matplotlib",
                    "explanation": "Seaborn is built on top of Matplotlib for attractive statistical graphics."
                },
                {
                    "q": "Which Seaborn function creates relational scatter or line plots across facets?",
                    "options": ["catplot()", "relplot()", "displot()", "pairplot()"],
                    "answer": "relplot()",
                    "explanation": "`relplot()` coordinates relational plots (scatter/line) across grid facets."
                },
                {
                    "q": "Which plot library specializes in interactive browser-based web charts with hover tooltips?",
                    "options": ["Matplotlib", "Seaborn", "Plotly", "Tkinter"],
                    "answer": "Plotly",
                    "explanation": "Plotly generates interactive, dynamic HTML/JavaScript charts."
                },
                {
                    "q": "Which Seaborn plot shows correlation matrices as color-coded grid heatmaps?",
                    "options": ["heatmap()", "matrixplot()", "corrplot()", "gridplot()"],
                    "answer": "heatmap()",
                    "explanation": "`sns.heatmap()` displays matrix data values using color intensities."
                },
                {
                    "q": "Which Plotly figure type is used to display interactive 3D surface or scatter coordinates?",
                    "options": ["3D graph", "Flat chart", "Grid plot", "Static graph"],
                    "answer": "3D graph",
                    "explanation": "Plotly supports full 3D interactive rotation graphs."
                },
                {
                    "q": "What Seaborn function plots categorical distributions like box plots or bar plots across categories?",
                    "options": ["catplot()", "distplot()", "relplot()", "Matrixplot()"],
                    "answer": "catplot()",
                    "explanation": "`catplot()` handles categorical categorical factor plots."
                },
                {
                    "q": "Which Plotly chart type displays project schedules and task timelines?",
                    "options": ["Gantt chart", "Pie chart", "Scatter chart", "Histogram"],
                    "answer": "Gantt chart",
                    "explanation": "Plotly easily generates interactive Gantt schedule timelines."
                },
                {
                    "q": "Which function in Seaborn plots univariate distributions (histograms with kernel density estimates)?",
                    "options": ["displot()", "histplot()", "kdeplot()", "All of the above"],
                    "answer": "All of the above",
                    "explanation": "Seaborn provides `displot`, `histplot`, and `kdeplot` for distribution analysis."
                },
                {
                    "q": "Can Plotly graphs render interactive zoom and pan controls?",
                    "options": ["Yes", "No", "Only in static images", "Only in PDF exports"],
                    "answer": "Yes",
                    "explanation": "Plotly charts include built-in interactive toolbar controls."
                },
                {
                    "q": "Which Seaborn function plots pairwise relationships across an entire DataFrame?",
                    "options": ["pairplot()", "jointplot()", "matrix()", "grid()"],
                    "answer": "pairplot()",
                    "explanation": "`pairplot()` plots pairwise numerical relationships across columns."
                },
                {
                    "q": "What is the primary advantage of Plotly over Matplotlib?",
                    "options": ["Interactivity and web-ready hover tools", "Faster raw C compilation", "Smaller file size", "No Python required"],
                    "answer": "Interactivity and web-ready hover tools",
                    "explanation": "Plotly offers interactive web-based zooming, panning, and tooltips."
                },
                {
                    "q": "Which function creates a joint plot with bivariate scatter and univariate marginals in Seaborn?",
                    "options": ["jointplot()", "mergeplot()", "dualplot()", "bindplot()"],
                    "answer": "jointplot()",
                    "explanation": "`jointplot()` combines bivariate scatter/regression with univariate distributions."
                },
                {
                    "q": "Does Plotly support interactive violin and box plots?",
                    "options": ["Yes", "No", "Only bar charts", "Only histograms"],
                    "answer": "Yes",
                    "explanation": "Plotly supports interactive violin, box, and statistical distribution graphs."
                },
                {
                    "q": "How do you set Seaborn default themes or styles?",
                    "options": ["sns.set_theme()", "sns.style()", "sns.load()", "sns.theme_apply()"],
                    "answer": "sns.set_theme()",
                    "explanation": "`sns.set_theme()` configures background aesthetics and default formatting."
                },
                {
                    "q": "Which Plotly graph displays cumulative frequency or counts across continuous bins?",
                    "options": ["Histogram", "Line graph", "Gantt chart", "Heatmap"],
                    "answer": "Histogram",
                    "explanation": "Plotly histograms provide interactive binning and hovering counts."
                }
            ]
        },
        "coding_exercises": [
            {
                "title": "Matplotlib Function Plot y = x^2 (Lab Exp 5c)",
                "desc": "Write a Python program using Matplotlib to plot the mathematical function y = x^2 with proper labels and gridlines.",
                "solution": '''import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = x ** 2

plt.plot(x, y, color='blue', label='y = x^2')
plt.title("Plot of Function y = x^2")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.legend()
plt.show()'''
            },
            {
                "title": "Tkinter Multi-Button Geometry Managers (Lab Exp 6)",
                "desc": "Write a Tkinter Python program that creates a window containing three buttons positioned using pack(), grid(), and place() geometry managers.",
                "solution": '''import tkinter as tk

root = tk.Tk()
root.title("Geometry Managers Demo")
root.geometry("300x200")

# 1. Pack Manager
btn1 = tk.Button(root, text="Pack Button", bg="lightblue")
btn1.pack(side=tk.TOP, pady=10)

# 2. Grid Manager
btn2 = tk.Button(root, text="Grid Button", bg="lightgreen")
btn2.place(x=100, y=80) # Using place or frame grid

# 3. Place Manager
btn3 = tk.Button(root, text="Place Button", bg="orange")
btn3.place(x=100, y=130)

root.mainloop()'''
            }
        ]
    }
}

# App Header
st.title("🐍 Python Exam Preparation Portal")
st.write("Master your Semester 1 syllabus with 15+ questions per chapter, theory quizzes, and hands-on coding practice exercises.")

# Sidebar Navigation
menu = st.sidebar.selectbox("Navigation", ["Syllabus Viewer", "Chapter Preparation Quiz", "Coding Practice Lab"])

if menu == "Syllabus Viewer":
    st.header("📖 Semester 1 Syllabus")
    selected_unit = st.selectbox("Select Unit", list(syllabus_data.keys()))
    
    st.subheader(selected_unit)
    chapters = syllabus_data[selected_unit]["chapters"]
    
    for ch_name, topics in chapters.items():
        with st.expander(ch_name):
            for topic in topics:
                st.write(f"- {topic}")

elif menu == "Chapter Preparation Quiz":
    st.header("📝 Chapter-wise Assessment Quiz")
    selected_unit = st.selectbox("Choose Unit", list(syllabus_data.keys()))
    
    chapters_list = list(syllabus_data[selected_unit]["questions"].keys())
    selected_chapter = st.selectbox("Choose Chapter", chapters_list)
    
    questions = syllabus_data[selected_unit]["questions"][selected_chapter]
    
    st.info(f"Loaded {len(questions)} preparation questions for **{selected_chapter}**.")
    
    with st.form("exam_quiz_form"):
        user_answers = {}
        for i, q_data in enumerate(questions):
            st.markdown(f"### Q{i+1}: {q_data['q']}")
            user_answers[i] = st.radio(
                "Select your answer:",
                q_data["options"],
                key=f"{selected_unit}_{selected_chapter}_q_{i}"
            )
            st.divider()
            
        submitted = st.form_submit_button("Submit & Check Results")
        
    if submitted:
        score = 0
        total = len(questions)
        st.subheader("📊 Performance & Detailed Feedback")
        
        for i, q_data in enumerate(questions):
            selected = user_answers[i]
            correct = q_data["answer"]
            
            if selected == correct:
                score += 1
                st.success(f"**Q{i+1}: Correct!** (Your answer: {selected})")
            else:
                st.error(f"**Q{i+1}: Incorrect!**")
                st.write(f"- **Your Answer:** {selected}")
                st.write(f"- **Correct Answer:** {correct}")
                st.info(f"💡 **Explanation:** {q_data['explanation']}")
            st.divider()
            
        percentage = round((score / total) * 100, 1)
        st.metric(label="Overall Chapter Score", value=f"{score} / {total}", delta=f"{percentage}%")
        
        if score == total:
            st.balloons()

elif menu == "Coding Practice Lab":
    st.header("💻 Programming & Lab Coding Exercises")
    selected_unit = st.selectbox("Select Unit for Coding", list(syllabus_data.keys()))
    
    exercises = syllabus_data[selected_unit]["coding_exercises"]
    
    st.write(f"Practice these implementation problems for **{selected_unit}**:")
    st.divider()
    
    for idx, ex in enumerate(exercises, 1):
        st.subheader(f"Exercise {idx}: {ex['title']}")
        st.write(ex['desc'])
        
        with st.expander(f"✨ View Python Code Solution for Exercise {idx}"):
            st.code(ex['solution'], language='python')
            
        st.divider()
