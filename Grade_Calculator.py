#                             Ideas I want to put in

#a person can insert an array for the things above for each of these caegories

# i want to put an array to make this more complex but i'll stick to basics rn

#Maybe input a loop that determines the week you're in and the amount of points for that week in each section and it considers whether or not to ask for certain exams in the final calculation

# We need to consider grades where the percentage of categories doesn't add up to 100 so we need to figure that out before implementing that into code

#Once I get the basic functions down along with the math then I can implement procedures for if something is inputted incorrectly

       # class calcGrade:
        #    def __init__(grade,rurt,participation,hw,workshop,q1,q2,q3,q4,q5,final):
         #       grade.rurt = rurt
          #      grade.participation = participation
           #     grade.hw = hw
            #    grade.workshop = workshop
             #   grade.q1 = q1
              #  grade.q2 = q2
        #        grade.q3 = q3
         #       grade.q4 = q4
          #      grade.q5 = q5
           #     grade.final = final

        #calcClass = calcGrade(rurt,participation,hw,workshop,q1,q2,q3,q4,q5,final)


#Definitions of functions
def calculusGrade(tf,week):
    if tf == 1:
    #    def introweek():
    #        rurt = int(input('What is your rurt grade: '))
    #        participation = int(input('What is your participation grade: '))
    #        hw = int(input('What is your hw grade: '))
    #        workshop = int(input('What is your workshop grade: '))
    #    end

        
        if week <= 2 and week>0:
            print("week 2")
            
        #consider only week one and 2 function
        
        elif week > 2 and week<14:
            print("week 2+")
            for i in range(week):
                print("hi")

        else:
            print("invalid time")


        #Getting grades
        rurt = int(input('What is your rurt grade: '))
        participation = int(input('What is your participation grade: '))
        hw = int(input('What is your hw grade: '))
        workshop = int(input('What is your workshop grade: '))
        q1 = int(input('What is your q1 grade: '))
        q2 = int(input('What is your q2 grade: '))
        q3 = int(input('What is your q3 grade: '))
        q4 = int(input('What is your q4 grade: '))
        q5 = int(input('What is your q5 grade: '))
        final = int(input('What is your final grade: '))

        grade = (rurt * .05)+(participation*.05)+(hw*.05)+(workshop*.1)+(q1*.05)+(q2*.125)+(q3*.125)+(q4*.125)+(q5*.125)+(final*.2)
        
        print(grade)

    else:
        print("c u m")

def chemistryGrade(tf,week):
    if tf == 1:
        q1 = int(input('What is your q1 grade: '))
        q2 = int(input('What is your q2 grade: '))
        quiz = int(input('What is your quiz grade: '))
        final = int(input('What is your final grade: '))

        grade = (q1 * .18)+(q2*.18)+(quiz*.4)+(final*.24)
                
        print(grade)
    else:
        print("c u m")

def physicsGrade(tf,week):
    if tf == 1:
        participation = int(input('What is your participation grade: '))
        prelecture = int(input('What is your prelecture grade: '))
        hw = int(input('What is your hw grade: '))
        recitation = int(input('What is your recitation grade: '))
        fridayquiz = int(input('What is your fridayquiz grade: '))
        labs = int(input('What is your labs grade: '))
        q1 = int(input('What is your q1 grade: '))
        q2 = int(input('What is your q2 grade: '))
        final = int(input('What is your final grade: '))

        grade = (participation * .05)+(prelecture*.05)+(hw*.15)+(recitation*.1)+(fridayquiz*.1)+(labs*.1)+(q1*.15)+(q2*.15)+(final*.15)
        
        print(grade)
    else:
        print("c u m")

def computersGrade(tf,week):
    if tf == 1:
        print("Hello World Computers")
    else:
        print("c u m")

def globalGrade(tf,week):
    if tf == 1:
        print("Hello World Global")
    else:
        print("c u m")

def gradeCalculator(classes):
    print("What class is this for?")
    Class = input("Class: ")
    print("What week are you in?")
    week = int(input("Week: "))
    
    if  Class.title() == str("Calculus"): 
        tf = 1
        calculusGrade(tf,week)

    elif Class.title() == str("Chemistry"):
        tf = 1
        chemistryGrade(tf,week)

    elif Class.title() == str("Physics"):
        tf = 1
        physicsGrade(tf,week)

    elif Class.title() == str("Computers"):
        tf = 1
        computersGrade(tf,week)

    elif Class.title() == str("Global"):
        tf = 1
        globalGrade(tf,week)

    elif Class.title() == str("None"):
        print("Good luck out there")
        tf = 1

    else:
        print("invalid input")


#init phase
print("How many classes do you want to know your grade for?")
classes = int(input("Classes: "))

for i in range(classes):
    gradeCalculator(classes)
print("Good luck out there")