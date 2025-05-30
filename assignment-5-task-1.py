data={'mnr':100,'anita':90,'mukesh':99,'Mrudula':80}
name=input("Enter the student's name: ")

if(name in data):
    print(name+"'s marks:",data[name])
else:
    print("Student not found")