# Style
Many of the styles below are from the [PEP 8 Style Guide for Python Code](http://www.python.org/dev/peps/pep-0008/#whitespace-in-expressions-and-statements).

## Code Layout
Indentation: 4 Spaces (do not use tabs).   
Maximum Line Length: Should be 80 (don't worry about this too much).   

### Blank Lines
* Two blank lines between functions (except methods - use one blank line between methods).   
        
        def foo():
            # Some Code.
        
        
        def bar():
            # Some Code.

* One blank line between a function and a class.   
        
        class className():
        
            def functionName():
                # Some Code.

* One blank line between logical blocks of code.
        
        # This does this.
        x = foo()
        y = bar()
        add(x, y)

        # This does something else.
        a = someFunkyFunc(x)

### Imports
* Imports should always go at the top of the file.
* Use imports on separate lines.   
        
        import this
        import that


## White Space
    dict["key"]  # Not dict[ "key" ]
    lst[index]  # Not lst[ index ]
    func(arg1, arg2)  # Not func( arg1, arg2 )
    def funcName(arg1, arg2):  # Not def funcName ( arg1, arg2 )

    # For Assignments use...
    someVar = 10
    otherVar = 12

    # Not...
    someVar     = 10
    otherVar    = 12

    # Always surround operators with a space on either side.
    x + 10 # Not x+10
    y and x


## Comments
### Block Comments
Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code. Each line of a block comment starts with a # and a single space (unless it is indented text inside the comment).

### Inline Comments
Use inline comments sparingly.

An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.

Inline comments are unnecessary and in fact distracting if they state the obvious.

### Documentation Strings
Write docstrings for public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does. This comment should appear after the def line.


## Naming
    variableIdentifier  # Should be a noun.
    functionIdentifier  # Should be a verb followed by a noun.
    ClassName  # Should be a noun.
