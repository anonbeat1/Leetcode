from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr,L,M,R):
            left = arr[L:M+1]
            rigth = arr[M+1:R+1]
            left_index = 0
            rigth_index = 0
            array_index = L

            while left_index < len(left) and rigth_index < len(rigth):
                if left[left_index] <= rigth[rigth_index]:
                    arr[array_index] = left[left_index]
                    left_index += 1
                else:
                    arr[array_index] = rigth[rigth_index]
                    rigth_index += 1
                array_index += 1
            while left_index < len(left):
                arr[array_index] = left[left_index]
                array_index += 1
                left_index += 1
            while rigth_index < len(rigth):
                arr[array_index] = rigth[rigth_index]
                array_index += 1
                rigth_index += 1


        def mergeSort(arr,left,rigth):
            if left == rigth:
                return arr
            #Split the array in 2 , left side and rigth side, for each call the mergeSort to split it, till they are length 1 
            # The middle index of the array
            m = (left + rigth) // 2
            # Sort the left half
            mergeSort(arr,left,m)
            # Sort the right half
            mergeSort(arr,m+1,rigth)

            merge(arr,left,m,rigth)
            return arr
        return mergeSort(nums,0,len(nums)-1)

x = Solution()
print(x.sortArray([6,5,4,3,2,1,0,-1,-2,-3,-4,-5]))