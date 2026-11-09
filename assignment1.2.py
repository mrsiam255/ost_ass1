name=(input("name: "))
print(name )


marks=int(input("1st: "))
print(marks)
marks2=int(input("2nd: "))
print(marks2)
marks3=int(input("3rd: "))
print(marks3)

avg=(marks + marks2 + marks3)/3
print(avg)

if(avg>=80 and avg<101):
    print("A+")
elif (avg>=70 and avg<80):
    print("A")
elif (avg>=60 and avg<70):
    print("A-")
elif (avg>=50 and avg<60):
    print("B")
elif (avg>=40 and avg<50):
    print("C")
elif (avg<40 and avg>=0):
    print("F")
else:
    print("invalid marks ")


