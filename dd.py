import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Python Exam Prep Portal",
    page_icon="🐍",
    layout="centered"
)

# Comprehensive Syllabus, MCQ Bank, and Coding Practice Exercises
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
                }
            ],
            "Introduction to Data Analytics & NumPy": [
                {
                    "q": "What is the core data structure in NumPy for multi-dimensional arrays?",
                    "options": ["pd.DataFrame", "np.ndarray", "list", "matrix"],
                    "answer": "np.ndarray",
                    "explanation": "`ndarray` is NumPy's optimized N-dimensional array container."
                }
            ],
            "Pandas & Matplotlib Visualization": [
                {
                    "q": "What is a 1D labeled array structure in Pandas called?",
                    "options": ["DataFrame", "Series", "Panel", "Vector"],
                    "answer": "Series",
                    "explanation": "A Pandas `Series` is a one-dimensional labeled homogeneous array."
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
                }
            ],
            "Chapter 3.2: Visualization with Seaborn & Plotly": [
                {
                    "q": "What library is Seaborn built on top of?",
                    "options": ["Plotly", "Matplotlib", "Tkinter", "NumPy"],
                    "answer": "Matplotlib",
                    "explanation": "Seaborn is built on top of Matplotlib for attractive statistical graphics."
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
st.write("Master your Semester 1 syllabus with theory quizzes and hands-on coding practice exercises.")

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