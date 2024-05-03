from typing import List

class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for rigth in range(1,len(nums)):
            if nums[rigth] != nums[rigth -1]:
                nums[left] = nums[rigth]
                left += 1
        print(nums)
        return left


x = Solution()
print(x.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


#Input [0,0,1,1,1,2,2,3,3,4]
#Primo Passaggio [0,0,1,1,1,2,2,3,3,4] -> L = 1 Ossia sul secondo 0 , ed R = 1 ossia sul secondo 0 -> Num[R] != Num[R-1]: False -> Non faccio nulla ma continuo ciclo ed aumento R +1
#Input Passaggio : [0, 1, 1, 1, 1, 2, 2, 3, 3, 4] -> L = 1 Ossia sul secondo 0 , ed R = 2 ossia sul primo 1 -> Num[R] != Num[R-1] : True , quindi aumento R , aumento L  e associo Nums[L] = Nums[R] -> Output Passaggio : [0,1,1,1,1,2,2,3,3,4]
#Input [0,1,1,1,1,2,2,3,3,4] -> L = 2 Ossia sul secondo 1 , ed R = 3 ossia sul terzo 1 -> Num[R] != Num[R-1] : False , Non faccio nulla ma continuo ciclo ed aumento R +1
#Input [0,1,1,1,1,2,2,3,3,4] -> L = 2 Ossia sul secondo 1 , ed R = 4 ossia sul quarto 1 -> Num[R] != Num[R-1] : False , Non faccio nulla ma continuo ciclo ed aumento R +1
#Input [0, 1, 1, 1, 1, 2, 2, 3, 3, 4] -> L = 2 Ossia sul secondo 1 , ed R = 5 ossia sul primo 2 -> Num[R] != Num[R-1] : True , quindi quindi aumento R , associo Nums[L] = Nums[R],aumento L  -> Output Passaggio : [0, 1, 2, 1, 1, 2, 2, 3, 3, 4]
#Input [0, 1, 2, 1, 1, 2, 2, 3, 3, 4] -> L = 3 Ossia sul secondo 1, ed R = 6 ossia sul terzo 2 -> Num[R] != Num[R-1] : False aumento solo R
#Input [0, 1, 2, 1, 1, 2, 2, 3, 3, 4] -> L = 3 Ossia sul secondo 1, ed R = 7 ossia sul primo 3 -> Num[R] != Num[R-1] : True quindi aumento R e associo Nums[L] = Nums[R],aumento L  -> Output Passaggio : [0, 1, 2, 3, 1, 2, 2, 3, 3, 4]
#Input [0, 1, 2, 3, 1, 2, 2, 3, 3, 4] -> L = 4 Ossia sul secondo 1, ed R = 8 ossia sul terzo 2 -> Num[R] != Num[R-1] : False aumento solo R
#Input [0, 1, 2, 3, 1, 2, 2, 3, 3, 4] -> L = 4 Ossia sul secondo 1, ed R = 9 ossia primo 4 -> Num[R] != Num[R-1] : True quindi associo Nums[L] = Nums[R] , aumento L -> Output Passaggio : [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
#Non posso più procedere perchè la lista è terminata , quindi ritorno L che ha valore 5 e la lista è [0, 1, 2, 3, 4, 2, 2, 3, 3, 4] con i primi numeri ordinati 
