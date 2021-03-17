with open("./test.txt","r") as f:
    value:str
    while value:= f.readline():
        print(value)

print("-----------------------------------------")

with open("./test.txt","r") as f:
    value:str
    while True:
        value= f.readline()
        if(not value): break
        print(value)
