# if condition

# syntax
# if condition
#       body of if:

# if else condtion
# if condtion
#   body of if
# else codtion
#   body
# 
age = 14
# if age>=18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")

# print("End of IF")

# if-else-if condition

#  if(condition)
#       body of if
#   else(condtion)
#       body
#   elif(condition)
#       body
#   _______________
#   _______________
#   _______________
#   _______________
#   else 
#       body

# Day = int(input("Enter day number : "))

# if Day == 1:
#     print("Sunday")
# elif(Day==2):
#     print("Monday")
# if Day == 3:
#     print("Tuesday")
# elif(Day==4):
#     print("Wednesday")
# if Day == 5:
#     print("Thursday")
# elif(Day==6):
#     print("Friday")
# elif(Day==7):
#     print("Saturday")
# else:
#     print("Enter valid Day number")

Age = int(input("Enter the age : "))
Mark = int(input("Enter the mark : "))
if Age>=18:
    if Mark>=50:
        print("Eligible for admission")
    else:
        print("Not eligible for admisson : Insuffcient mark")
else:
    print("Not eligible for admission : Age is below 18")
