# Write a program to input an integer N then print the sum of all its even digits and sum of all its odd digits separately.

# Digits mean numbers, not the places! That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.

num = input("Enter number:")
even_sum = 0
odd_sum = 0
for i in num:
    i = int(i)
    if i%2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Even sum :",even_sum)
print("Odd sum :", odd_sum)