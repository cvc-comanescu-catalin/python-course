"""
if statements allow you to execute a block of code only if a certain condition is true.
This is fundamental for making decisions in your code and for controlling the flow of execution based on different conditions.
The basic syntax of an if statement is:
if condition:
    # code to execute if condition is true

You can also use else to specify a block of code that will run if the condition is false:
if condition:
    # code to execute if condition is true
else:
    # code to execute if condition is false

Additionally, you can use elif (short for "else if") to check multiple conditions in sequence:
if condition1:
    # code to execute if condition1 is true
elif condition2:
    # code to execute if condition2 is true
else:
    # code to execute if neither condition1 nor condition2 is true
"""

x = 5
print('Before 5')
if  x == 5 :
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
print('Afterwards 5')
print('Before 6')
if x == 6 :
    print('Is 6')
    print('Is Still 6')
    print('Third 6')
print('Afterwards 6')


x = 4
if x > 2 :
    print('Bigger')
else :
    print('Smaller')
print('All done')



if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
elif x < 20 : 
    print('Big')
elif x < 40 : 
    print('Large')
elif x < 100:
    print('Huge')
else :
    print('Ginormous')


# Grade classifier
score = int(input("Enter your score: "))
 
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
 
print(f"Your grade is: {grade}")


"""
You can also nest if statements inside each other to check multiple conditions in a more complex way.
For example, you might want to check if a number is positive, negative, or zero, and then further classify positive numbers as even or odd:
"""

number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
elif number < 0:
    print("Negative")
else:
    print("Zero")

"""
This allows you to create more detailed and specific logic in your programs, but be careful not to over-nest if statements, as it can make your code harder to read and maintain.
Always strive for clarity and simplicity in your code, and consider using functions to break down complex logic into more manageable pieces when necessary.
"""

x = 5
if x > 2 :
    print('Bigger than 2')
    print('Still bigger')
print('Done with 2')

for i in range(5) :
    print(i)
    if i > 2 : 
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')
