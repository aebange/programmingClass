## Objectives
1. Define the basics of python classes and how they can be used

### Creating Classes
-  **How to create a class:** To create a class, just state the name of the class. It's contents should be indented.
    - ``class Employee:``
- **__init__:** A method specific to python. Used to construct the attributes of a class.

### Instances
- **What are instances?** Instances are specific versions of a class that have their own inputs and outputs.
    ```
        class Employee
            def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
            self.email = first + '.' + last + '@company.com'
            
        employee_1 = Employee('Big', 'Mike', 20000) <--- This is the instance
- **How instances are represented:** Instances are called in the class as "self". When calling the attributes of an instance in a class, self is used.

### Class Variables vs Instance Variables
- **Class Variables:** Variables that are shared across all instances within the same class. Essentially just a variable defined within a class that is added on as an attribute.
- **Instance Variables:** Variables or attributes that are specific to an instance of a class. 

### Public vs Private Attributes
- **Private objects**: Python does not support "true" private attributes. Rather, the common practice is to name private attributes in a way that should warn programmers not to attempt to call them in order to avoid breaking things.
    - Private methods should not be called from outside of their class
        - ``def __displayFunction(param):`` is private       
    - Private attributes should not be called from outside their class
        - ``param.__displayType = "1920x1080"`` is private
    - Private functions prefixed and suffixed by double underscores are reserved for python and should never be used by the user
        - ``__init__`` is reserved for use by python
- **Single underscore vs double underscore ("dunder")** : Single underscores are used as "suggestions" - warning other programmers. Double underscores are more effective because they "name mangle" the object in use - forcing coder's to use workarounds to call them.
- **Getting and setting private objects**: Everything in python that is private should have a "getter" and "setter". Setters will create and define the private objects. Getters will provide a way for the private objects to be safely called without being modified.
    - Setting a private object is as easy as creating a normal object. Just add two underscores before the name
        - ```
            def __privateFunction(param)
            param.__prviateVar = 42
    - Getting a private object requires a seperate function to call and return the private object.
        - ```
            class pythonClass:
                def getPrivateFunction(param)
                    return param.__privateVar
        - ```
            import pythonClass
            item = pythonClass.item()
            print(item.getPrivateFunction)
            
    