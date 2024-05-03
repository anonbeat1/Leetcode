from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def quickSort(arr,left,rigth):
            #Controllo che la len dell'array composto tra left e rigth sia > 1
            if rigth - left +1 <=1:
                return arr
            
            #Troviamo il valore di appoggio , ES: ultimo valore dell'array
            pivot = arr[rigth]
            #Prendiamo un puntatore (lo start dell'array, in questo caso LEFT che è il primo valore)
            pointer = left

            #Per ogni valore dall'indice left all'indice rigth  #SWAPPO se arr[idx] è minore del valore preso del pivot
            for idx in range(left,rigth):
                if arr[idx] < pivot:
                    tmp = arr[pointer]
                    arr[pointer] = arr[idx]
                    arr[idx] = tmp
                    pointer += 1

            arr[rigth] = arr[pointer]
            arr[pointer] = pivot

            quickSort(arr,left,pointer-1)
            quickSort(arr,pointer +1 ,rigth)

            return arr
        return quickSort(nums,0,len(nums)-1)
x = Solution()
print(x.sortArray([6,5,4,3,2,1,0,-1,-2,-3,-4,-5]))