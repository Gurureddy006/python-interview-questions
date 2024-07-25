# Write a Python code to swap two variables
# Swapping here mean initial value of a is stored in b and viceversa after performing swapping

# swapping with using a third variable
a = 2
b = 20
print("Before swapping ", "a:", a, "b:", b)
temp = a
a = b
b = temp
print("After swapping ", "a:", a, "b:", b)


# swapping without using a third variable(There are many ways here are few)

# Way 1
x = 10
y = 20
print("Before swapping ", "x:", x, "y:", y)
x,y = y,x
print("After swapping ", "x:", x, "y:", y)


# Way 2
c,d = 42,60
c = c + d
d = c-d
c = c-d
print(c, d)


# Way 3
i,j = 123, 1355
i = i^j  # xor operator
j = i^j
i = i^j

print(i,j)
