from __future__ import annotations
from Counter import CounterMod,CounterCountMod
from datetime import datetime
from typing import get_type_hints,Union,Any,Dict,List
from merge_words import merge_words
import sys
class Data:
    end_of_period:datetime
    # loan_number:str
    region:str
    # country_code:str
    country:str
    # borrower:str
    # guarantor_country_code:str
    # guarantor:str
    # loan_type:str
    # loan_status:str
    interest_rate:float
    # currency_of_commitment:str
    project_id:str
    project_name_:str
    # original_principal_amount:float
    cancelled_amount:float
    undisbursed_amount:float
    disbursed_amount:float
    # repaid_to_ibrd:float
    # due_to_ibrd:float
    # exchange_adjustment:float
    # borrower_s_obligation:float
    # sold_3rd_party:float
    # repaid_3rd_party:float
    # due_3rd_party:float
    # loans_held:float
    # first_repayment_date:datetime
    # last_repayment_date:datetime
    # agreement_signing_date:datetime
    # board_approval_date:datetime
    # effective_date:datetime
    # closed_date:datetime
    # last_disbursement_date:datetime

    @classmethod
    def from_list(cls,obj:List[str],header_list:List[str])->Data:
        t= Data()
        
        for att,clz in get_type_hints(cls).items():
            i:str=header_list.index(att)
            clz:Union[str,float,datetime]
            if(not i<len(obj)):
                continue
            if(clz is datetime):
                clz:datetime
                try:
                    t.__setattr__(att,clz.strptime(obj[i],r'%m/%d/%Y %I:%M:%S %p'))
                except ValueError as err:
                    t.__setattr__(att,None)
                
            else:
                try:
                    value:str = obj[i]
                    if(value==""):
                        t.__setattr__(att,None)
                    else:
                        t.__setattr__(att,clz(obj[i]))
              
                except ValueError as e:
                    print(att,obj[i])
                    print(string)
                    print(obj)
                    raise e

           
        return t

    def _get_att(self)->Dict:
        return get_type_hints(self.__class__)
    def __str__(self):
        clz = self.__class__
        returned:str = ""
        
        k:str
        for k in get_type_hints(clz).keys():
            returned+=f"{k}: {getattr(self,k)} \n"
        
        return returned

    @classmethod
    def sql_create_table(cls)->str:
        _create_data:List[str] = []
        for att,clz in get_type_hints(cls).items():
            if(clz is str):
                _create_data.append(f"{att} varchar(255)")
            if(clz is float):
                _create_data.append(f"{att} float")
            if(clz is datetime):
                _create_data.append(f"{att} datetime")
        
       
        sql = f"create table loan ({','.join(_create_data)});"
        return sql

    def value_sql(self)->str:
       
        v:List[str] = []
        for att in self._get_att():
            v.append("'"+str(getattr(self,att))+"'")
        return f"({','.join(v)})"

csv_path = r"../data.csv"

def get_header_list(header_text:str)->List[str]:
    returned:List[str] = []
    cols:List[str] = header_text.split(",")
    col:str
    for col in cols:
        words:List[str] = col.split(" ")
        word:str
        words = list(filter(lambda word:"(" not in word and ")" not in word,words))
        words = list(map(lambda word:word.lower(),words))

        for i in range(len(words)):
            words[i] = words[i].replace("\n","")
            words[i] = words[i].replace("'","_")
        returned.append(f"{'_'.join(words)}")
    return returned


if __name__ == "__main__":
    with open(csv_path,"r") as f:
        header_list = get_header_list(f.readline())
        i = 0
        
        string:str
        missing_data:int=0
        while string:=f.readline():
            i+=1
            # if(i<450_000):
            #     if(CounterCountMod.listen("skip",int(1e4))):
            #         print(f"skip {i}")
            #     continue


            if(CounterMod.listen("limit",None) ):break
            if(CounterCountMod.listen("progress bar",int(1e4)) ):
                print(CounterCountMod.get_i("progress bar"))

            
       
            p:List[str]
            # case 1: need to merge
            if(len(header_list)<len(string.split(",")) ):
                p = merge_words(string.split(","))
            else:
                p = string.split(",")

            obj:Data = Data.from_list(p) 


            #### Filtering by End of periods year
            year:str
            try:
                year = obj.end_of_period.year
            except AttributeError as e:
                year = '0'
            if not(int(year) >= 2010 and int(year)<=2020):
                continue
            ####

            # print(obj.value_sql())
            

# print(get_type_hints(Data))