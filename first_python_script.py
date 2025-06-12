#week1day1
# print('Hello World!')
# a=10
# print(a)

#Week1day2
# a=10
# b=0
# c=20
# print(f'a+b = { a+b }')

#if condition
x=5

if x > 1:
    print("X is positive")
    
#if else condition    
grade = 48
courses_passed = 2
courses_failed = 5

# Is grade >= 50?
if grade >= 50:
    # Increase courses_passed
    courses_passed += 3
else:
    # Increase courses_failed
    courses_failed += 1

print("Passed:", courses_passed)
print("Failed:", courses_failed)

grade=60
coursesPassed=1
coursesFailed=0

if grade >= 50:
    coursesPassed += 1
    letter_grade = "P"
else:
    coursesFailed += 1
    letter_grade = "F"
    
print("Letter Grade:", letter_grade)
print("Courses Passed:", coursesPassed)
print("Courses Failed:", coursesFailed)





def add (x,y):
    result = x + y
    return result
print (add(3,4))