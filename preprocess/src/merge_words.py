from typing import List
def merge_words(words:List[str])->List[str]:
    stack:List[str] = []
    returned:List[str] = []
    flat = False
    for word in words:
        if('"' in word):
        # if('"' in word or "'" in word):
            word = word.replace("'","").replace('"',"")
            if(len(stack)==0):
                flat=True
                stack.append(word)
            else:
                flat=False
                stack.append(word)
                merged_word = ",".join(stack)
                returned.append(merged_word)
                stack = []
        else:
            if(flat):
                stack.append(word)
            else:
                returned.append(word)
    
    if(len(stack)!=0):
        raise RuntimeError(f" single ' or double ' error {stack}")
    return returned

def list_eq(obj1:List[str],obj2:List[str])->bool:
    for e1,e2 in zip(obj1,obj2):
        if(e1!=e2):
            return False
    return True      

if __name__=="__main__":
    test = ['ff','"aa','bb"']
    output = merge_words(test)
    print(output)
    assert list_eq(output,['ff','aa,bb'])

    test = ['ff','"aa','mmmm','bb"']
    output = merge_words(test)
    assert list_eq(output,['ff','aa,mmmm,bb'])
