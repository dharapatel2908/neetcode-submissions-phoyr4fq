class Solution:
    def checkValidString(self, s: str) -> bool:
        counter1 = counter2 =0
        for i in s:
            if i == "(":
                counter1 +=1
                counter2 +=1
            if i == ")":
                counter1 -=1
                counter2 -=1
            if i == "*":
                counter1 -=1
                counter2 +=1
                
            if counter2<0:
                return False
            counter1 = max(counter1,0)

        return counter1 == 0
            
       