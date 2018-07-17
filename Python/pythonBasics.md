## Objectives
1. Define the basics of understanding and using the Python (3) programming language

### How and why Python works
-  **The interpreter:**  takes the text from a Python program file (.py) and decodes the contained Python statements (from the top of the file to the bottom) into commands that it then executes. 
-  **Byte code:** is created when a Python program file is executed. The commands contained inside of the file are compiled into this lower level platform-independent representation by decomposing them into individual steps. This is done to increase the speed of the program's execution as Byte code can be read and executed faster than raw Python source code.
    - Byte code can be generally found in a subdirectory called ``__pycache__`` located within the same directory as their source files. 
    - Whenever the Python program file is updated, it's corresponding Byte code file(s) are also rewritten to contain the new changes.
    - Because python uses Byte code, **there is no need to build or make a program before it's execution.**
    - If the system fails to compile a Byte code file, the program will still successfully execute, however the process will take place at a slower pace since a new Byte code file will need to be created each time the program is run. 
-  **Python Virtual Machine (PVM)**: The massive loop of code that makes up the runtime engine of python. The PVM is the "final step" of the Python interpreter.

### General concepts to understand
-  **Methods:** Functions that are attached to and act upon a specific object and are called with an expression
    - `S = 'Spam'`, `S.find(pa) >> 1 `('find' is the method and it works on strings)
-  **Getting help:** Whenever curious about a function or method, simply type help(x.function) to see the syntax in the interpreter. Results will vary depending on the object type of the variable used.
    - `S = [1,2,3,"four]`, `help(S.insert)`
-  **Nesting:** Objects of any type can be nested within eachother. So lists can be nested in lists can be nested in dictionaries can be nested in lists. 
    - `L = [1,2,3,4]`, `X = ["A","B","C"]`, `L.append(X) >>> L >>> [1,2,3,4,["A","B","C"]]`

### Python Data Types
-  **Numbers:**
    - **Integer (int(x)): Whole numbers that have no decimals.
        - `1234, 5, -666, 13`
    - **Long (long(x)): An integer that is infinite in size
        - `51924361L`
    - **Float (float(x)): Numbers that do have decimals.
        - `3.1415, 100.5, -237.0145`
    - **Complex (complex(x,y)): All numbers are expressed as a sum of a real part and an imaginary part.
        - `(3+1j)`, `(2+4j)`
-  **Strings:** Text used to contain information as well as arbitrary collections of bytes.
    - Immutability: Strings are immutable and cannot be overwritten. 
        - `S = 'Spam'`, `S[0] = 'z' >>> ...error text omitted...`
    - Sequence Operations: A word contained in a string acts as though each character is a separate string.
        - `S = 'Spam'`, `len(S) >>> 4`, `S[0] >>> 'S'`, `S[3] >>> 'm'`
    - Single vs Double Quotes: Single quotes should be used to contain the string, double quotes should be used as normal quotes inside of the string.
        - `S = 'And now for something "completely" different.'`
-  **Lists:** Positionally ordered collections of arbitrarily typed objects.
    - Sequence Operations: Items contained in a list act as though each whole item is separate. 
        - `S = [1, 2, 3, 'pie']`, `S[3] >>> 'pie'`, `len(S) >>> 4`
    - Common Methods:
        - x.append("text"): Adds a single object to the end of a list.
        - x.pop(#): Deletes an object in the specified list offset. 
        - x.insert(#,"text"): Adds a single object to a specified list offset.
        - x.remove("text"): Removes a single specified object.
        - x.sort(): Sorts list items based on alphabetic and numeric order.
        - x.reverse(): Sorts list items in reverse of the format used in list.sort.
    - Bounds checking: Python requires modifications to lists to be made using methods. 
    - Matrix: A two dimensional set of lists contained in a list.
        - `M = [[1,2,3], [4,5,6], [7,8,9]]`
    - Matrix Comprehensions: Ways of retrieving information from a Matrix.
        - `col2 = [row[1] for row in M]`, `col2 >>> [2,5,8]` (creates a "for" loop that collects items from row[1] in M)
        - `row2 = M[1]`, `row2 >>> [1,2,3]`
        - `G = (sum(row))`, `next(G) >>> 6`, `next(G) >>> 15`, `next(G) >>> 24`, `next(G) >>> error` (out of rows)
        - `list(range(4)) >>> [0,1,2,3]`, `list(range{-7,7,2)) >>> [-6,-4,-2,0,2,4,6]`
        - `list(map(sum, M)) >> [6, 15, 24]`
        - `(sum(row) for row in M) >>> {24, 6, 15}`
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

