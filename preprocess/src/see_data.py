from typing import List
print("""
0 => get Object att header
1 => let see sample raw data
""")

csv_path = r"../data.csv"

while True:
    a = int(input("enter: "))
 
    print("-"*10)
    if(a==0):
        with open(csv_path) as f:
            cols:List[str] = f.readline().split(",")
            col:str
            for col in cols:
                words:List[str] = col.split(" ")
                word:str
                words = list(filter(lambda word:"(" not in word and ")" not in word,words))
                words = list(map(lambda word:word.lower(),words))

                for i in range(len(words)):
                    words[i] = words[i].replace("\n","")
                    words[i] = words[i].replace("'","_")
                print(f"{'_'.join(words)}:str")

    if(a==1):
        with open(csv_path) as f:
            for i in range(0,5):
                print(f.readline())