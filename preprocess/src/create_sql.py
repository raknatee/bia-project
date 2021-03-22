from TableModel import Data,get_header_list,NoneValue
from Counter import CounterMod,CounterCountMod
from merge_words import merge_words
from typing import Union,List,Dict
from sql import insert
import mysql
import random
print("""
0 => create table
1 => insert data (sample data)
2 => insert data (all)
3 => dump to database (smaple data)
4 => dump to database (all)
""")

cmd = int(input(">>"))

sampling:bool = bool(input("Sampling ? True/False:"))
csv_path = r"../data.csv"

if(cmd==0):
    with open("../sql/create_table.sql","w") as f:
        f.write(Data.sql_create_table())

if(cmd in [i for i in range(1,5+1)]):
    values:List[str] = []
    with open(csv_path,"r") as f:
        header_list = get_header_list(f.readline())
        i = 0
        
        string:str
        insert_err:int=0
        while string:=f.readline():
            i+=1
            # if(i<450_000):
            #     if(CounterCountMod.listen("skip",int(1e4))):
            #         print(f"skip {i}")
            #     continue

            _limit:Union[int,None]
            if(cmd in [1,3]):
                _limit = 1000
            else:
                _limit = None
            if(CounterMod.listen("limit",_limit) ):break
            if(CounterCountMod.listen("progress bar",int(1e4)) ):
                print(CounterCountMod.get_i("progress bar"))

            if(sampling):
                if(random.random()>0.02):
                    continue
            
       
            p:List[str]
            # case 1: need to merge
            if(len(header_list)<len(string.split(",")) ):
                p = merge_words(string.split(","))
            else:
                p = string.split(",")

            obj:Data = Data.from_list(p,header_list) 


            #### Filtering by End of periods year
            year:str
            try:
                year = obj.end_of_period.year
            except AttributeError as e:
                year = '0'
            if not(int(year) >= 2010 and int(year)<=2020):
                continue
            ####

            #### Filter only Thailand
            # country:str = obj.country
            # if(country != "Thailand"):
            #     continue
            try:
             
                if(cmd in [3,4]):
                    insert(f"insert into loan values {obj.value_sql()};")
                else:
                    values.append(obj.value_sql())

             
            except AttributeError:
                continue
            except mysql.connector.errors.ProgrammingError:
                insert_err+=1
            except mysql.connector.errors.DatabaseError:
                # mean some fields is missing
                continue
            except NoneValue:
                continue
               

    if(cmd in [1,2]):
        filename:str 
        if(cmd==1):
            filename="insert_data_sample.sql"
        if(cmd==2):
            filename="insert_data.sql"

        with open(f"../sql/{filename}","w") as f:
            f.write(f"insert into loan values {','.join(values)};")
    
    if(cmd in [3,4]):
        print("insert error",insert_err)
    
        


   
