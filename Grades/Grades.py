def grader():
    for i in range(0,10):
        print "Please enter a grade:"
        grade = input()
        if grade<=100 and grade>=90:
            print "Score: {}; Your grade is A".format(grade)
        elif grade<=89 and grade >=80:
            print "Score: {}; Your grade is B".format(grade)
        elif grade<=79 and grade >=70:
            print "Score: {}; Your grade is C".format(grade)
        elif grade <=69 and grade >=60:
            print "Score: {}; Your grade is D".format(grade)

    print "You're done. Goodbye"
grader()
