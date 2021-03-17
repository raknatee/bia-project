from __future__ import annotations
from Counter import CounterMod,CounterCountMod
from datetime import datetime
from typing import get_type_hints,Union,Any,Dict
import sys
class Data:
    end_of_period:datetime
    loan_number:str
    region:str
    country_code:str
    country:str
    borrower:str
    guarantor_country_code:str
    guarantor:str
    loan_type:str
    loan_status:str
    interest_rate:float
    currency_of_commitment:str
    project_id:str
    project_name_:str
    original_principal_amount:float
    cancelled_amount:float
    undisbursed_amount:float
    disbursed_amount:float
    repaid_to_ibrd:float
    due_to_ibrd:float
    exchange_adjustment:float
    borrower_s_obligation:float
    sold_3rd_party:float
    repaid_3rd_party:float
    due_3rd_party:float
    loans_held:float
    first_repayment_date:datetime
    last_repayment_date:datetime
    agreement_signing_date:datetime
    board_approval_date:datetime
    effective_date:datetime
    closed_date:datetime
    last_disbursement_date:datetime

    @classmethod
    def from_list(cls,obj:List[str])->Data:
        t= Data()
        
        for att,clz in get_type_hints(cls).items():
            i:str=header_list.index(att)
            clz:Union[str,float,datetime]
            if(clz is datetime):
                clz:datetime
                try:
                    t.__setattr__(att,clz.strptime(obj[i],r'%m/%d/%Y %I:%M:%S %p'))
                except ValueError as err:
                    t.__setattr__(att,None)
                
            else:
                try:
                    t.__setattr__(att,clz(obj[i]))
                except ValueError as err:
                    # TODO: check!!!! interest_rate is "Fully Repaid"
                    # print(att,clz,obj[i])
                    # sys.exit()
                    pass

           
        return t

    def __str__(self):
        clz = self.__class__
        returned:str = ""
        
        k:str
        for k in get_type_hints(clz).keys():
            returned+=f"{k}: {getattr(self,k)} \n"
        
        return returned



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
        years:Dict[str,int]={}
        string:str
        while string:=f.readline():
            if(CounterMod.listen("limit",None) ):break
            if(CounterCountMod.listen("how many",int(1e4)) ):
                print(f"done at {CounterCountMod.get_i('how many')}\n {years}\n")

           
            
            obj:Data = Data.from_list(string.split(",")) 
            year:int = obj.end_of_period.year
            if year in years:
                years[year]+=1
            else:
                years[year] = 1

            i+=1
        print(years)

# print(get_type_hints(Data))