f = 101
g = 123
print(f)


# Global vs.local variables in functions
def someFunction():
    global f
    g = 23
    print("gh")
    f = u"changing global variable"


someFunction()
print(f, g)

# To use global declare the variable with global
