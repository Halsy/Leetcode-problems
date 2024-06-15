class Solution:
    def isValid(self, s: str) -> bool:
        open_string   ='[({'
        close_string  ='])}'
        string=[]
        for item in s:
            if item in open_string:
                string.append(item)
            elif item in close_string and len(string)>0:
                if open_string[close_string.index(item)] == string[-1]:
                    string.pop()
                else:
                    return False
                    
            else:
                return False
                
        return len(string)==0


        