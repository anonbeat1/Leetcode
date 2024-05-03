from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)): #First Pointer [2,3,4,1,6] POINTS 3
          j = i-1
          while j>=0 and nums[j+1] < nums[j]: #Esegue quando il numero successivo è più piccolo del precedente
            temp = nums[j+1] #Salvo il valore più grande all'interno di una variabile temporanea
            nums[j+1] = nums[j] #Al numero più grande do il numero più piccolo facendo scambio -> Grande -> Piccolo
            nums[j] = temp
            j -= 1 #Questo mi permette di scorrere tutto l'array al contrario , finchè nums[j+1] > nums[j] è falsa ( quindi tutti i numeri sono in ordine)
        return nums
    
x = Solution()
print(x.sortArray([2,3,4,1,6]))