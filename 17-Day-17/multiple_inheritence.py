# Multiple inheritence in Python
class A :
    variable_a = "Welcome to variable A"

class B :
    variable_b = "Welcome to variable B"

class C (A,B):
    variable_c =  "Welcome to variable C"

c1 = C()
print(c1.variable_c)
print(c1.variable_a)
print(c1.variable_b)