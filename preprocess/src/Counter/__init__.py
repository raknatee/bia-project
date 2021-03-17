from __future__ import annotations
from typing import *
class CounterMod:
    meta:Dict[str,Dict[str:int]] ={}

    @classmethod
    def listen(cls,name:str,n:Optional[int]=None):
        if(n is None):
            return False
        if(isinstance(n,int)):
            if name not in cls.meta:
                cls.meta[name] = {"count":0,"n":n}
            else:
                cls.meta[name]["count"]+=1
                if(cls.meta[name]["count"]==cls.meta[name]["n"]):
                    cls.meta[name]["count"] = 0
                    return True

class CounterCountMod:
    meta:Dict[str,Dict[str:int]] ={}

    @classmethod
    def listen(cls,name:str,n:Optional[int]=None)->bool:
        if(n is None):
            return False
        if(isinstance(n,int)):
            if name not in cls.meta:
                cls.meta[name] = {"count":0,"n":n,"i":0}
            else:
                cls.meta[name]["count"]+=1
                cls.meta[name]["i"]+=1
                if(cls.meta[name]["count"]==cls.meta[name]["n"]):
                    cls.meta[name]["count"] = 0
                    return True

    @classmethod
    def get_i(cls,name:str)->int:
        return cls.meta[name]["i"]