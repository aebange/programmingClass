### Objectives
1. Define the basics of understanding and using the Python (3) programming language

#### How and why Python works
-  **The interpreter:**  takes the text from a Python program file (.py) and decodes the contained Python statements (from the top of the file to the bottom) into commands that it then executes. 
-  **Byte code:** is created when a Python program file is executed. The commands contained inside of the file are compiled into this lower level platform-independent representation by decomposing them into individual steps. This is done to increase the speed of the program's execution as Byte code can be read and executed faster than raw Python source code.
    - Byte code can be generally found in a subdirectory called ``__pycache__`` located within the same directory as their source files. 
    - Whenever the Python program file is updated, it's corresponding Byte code file(s) are also rewritten to contain the new changes.
    - Because python uses Byte code, **there is no need to build or make a program before it's execution.**
    - If the system fails to compile a Byte code file, the program will still successfully execute, however the process will take place at a slower pace since a new Byte code file will need to be created each time the program is run. 
-  **Python Virtual Machine (PVM)**: The massive loop of code that makes up the runtime engine of python. The PVM is the "final step" of the Python interpreter.

#### General concepts to understand
-  **Methods:** Functions that are attached to and act upon a specific object and are called with an expression
    - `S = 'Spam'`, `S.find(pa) >> 1 `('find' is the method and it works on strings)

#### Python Data Types
-  **Numbers:**
    - Integer (int(x)): Whole numbers that have no decimals.
        - `1234, 5, -666, 13`
    - Long (long(x)): An integer that is infinite in size
        - `51924361L`
    - Float (float(x)): Numbers that do have decimals.
        - `3.1415, 100.5, -237.0145`
    - Complex (complex(x,y)): All numbers are expressed as a sum of a real part and an imaginary part.
        - `(3+1j)`, `(2+4j)`
-  **Strings:** Text used to contain information as well as arbitrary collections of bytes.
    - Immutability: Strings are immutable and cannot be overwritten. 
        - `S = 'Spam'`, `S[0] = 'z' >>> ...error text omitted...`
    - Sequence Operations: A word contained in a string acts as though each character is a separate string.
        - `S = 'Spam'`, `len(S) >>> 4`, `S[0] >>> 'S'`, `S[3] >>> 'm'`
    - Single vs Double Quotes: Single quotes should be used to contain the string, double quotes should be used as normal quotes inside of the string.
        - `S = 'And now for something "completely" different.'`
-  **Lists:** Positionally ordered collections of arbitrarily typed objects.
    - Sequence Operations: Items contained in a list act as though each item is separate. 
    - [1, [2, 'three'], 4.5],list(range(10))
-  **Dictionaries:**
    - {'food': 'spam', 'taste': 'yum'},dict(hours=10)
-  **Tuples:**
    - (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
-  **Files:**
    - open('eggs.txt'),open(r'C:\ham.bin', 'wb')
-  **Sets:**
    - set('abc'),{'a', 'b', 'c'}
-  **Booleans:**
    - True, False
-  **Types:**
