howManyEntered = 0
total = 0
average = 0
#this link inputs how many test scores user wants to enter
howMany = int (input("How many test scores would you like to average? "))
while howManyEntered < howMany:
    testScore = int (input("Enter test score: "))
    total = total + testScore
    howManyEntered = howManyEntered + 1

average = total/howMany
print ("The average for the test scores you entered is: " + str (average))
