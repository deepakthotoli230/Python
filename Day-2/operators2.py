# comparison operators

a=38
b=38

print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
print (a==b)
print(a!=b)


# logical operators

# "and" operator

age = 18
has_voter_id = False
eligible_for_voting = age>=18 and has_voter_id
print(eligible_for_voting)

# "or" operator

has_adhaar_card = False
has_pan_card = False
can_mark_vote = has_voter_id or has_adhaar_card or has_pan_card
print(can_mark_vote)


# input data

# n1 = int(input("Enter the 1st no"))
# n2 = int(input("Enter the 2nd no"))

# print(n1>n2)
# print(n2)



print(bool(False))
print(bool(True))
print(bool(1))
print(bool(10000))
print(bool(0))
print(bool(-9))
print(bool("heelloooo"))
print(bool(""))
print(bool([1,2,3,4,5]))
print(bool([]))
print("hello" and "ajith")
print(0 and "ajith")
print([1] and "HELLO")


# membership operators,identity operators
print("hello" in "hello world")
print ("hello" in "how are you")
print ("hello" not in "old money")
print("hello" not in "hello world")


a=[1,2,3,4,5]
b=[1,2,3,4,5]
print (a == b)
print(a is b)
n=1
m=4
print(m is n)
print(id(m))
print(id(n))
print(id(a))
print(id(b))


