a = "a"
b = ["b"]

print(f"{a} is {id(a)}")
print(f"{b} is {id(b)}")

a += "b"
b += "c"
# Not same as b = b+a

print(f"{a} is {id(a)}")
print(f"{b} is {id(b)}")
