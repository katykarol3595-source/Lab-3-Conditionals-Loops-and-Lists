#Demonstrates the use of logical operators: for example, ask the user for two boolean inputs (True/False or 1/0) and show the results of and, or, and not on those inputs.
val1 = True
val2 = False
print("Logical operators demo:")
print(f"val1 and val2: {val1 and val2}")
print(f"val1 or val2: {val1 or val2}")
print(f"not val1: {not val1}")
#Demonstrates bitwise operators (&, |, ^, ~, <<, >>)
a = 5
b = 3

print("Bitwise operators demo:")
print("a =", a, "binary:", bin(a), ", b =", b, "binary:", bin(b))
print("Bitwise AND (a & b):", a & b, "binary:", bin(a & b))
print("Bitwise OR (a | b):", a | b, "binary:", bin(a | b))
print("Bitwise XOR (a ^ b):", a ^ b, "binary:", bin(a ^ b))
print("Bitwise NOT (~a):", ~a, "binary:", bin(~a))
print("Left shift (a << 1):", a << 1, "binary:", bin(a << 1))
print("Right shift (a >> 1):", a >> 1, "binary:", bin(a >> 1))
