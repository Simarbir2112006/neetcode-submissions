class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def merge(arr, arrRef, l, m, r):
            left = arr[l:m+1]
            leftRef = arrRef[l:m+1]

            right = arr[m+1: r+1]
            rightRef = arrRef[m+1: r+1]

            i, j, k = l, 0, 0

            while j < len(left) and k < len(right):
                if left[j] >= right[k]:
                    arr[i] = left[j]
                    arrRef[i] = leftRef[j]
                    j+=1
                
                else:
                    arr[i] = right[k]
                    arrRef[i] = rightRef[k]
                    k+=1
                
                i+=1
            
            while j < len(left):
                arr[i] = left[j]
                arrRef[i] = leftRef[j]
                j+=1
                i+=1

            while k < len(right):
                arr[i] = right[k]
                arrRef[i] = rightRef[k]
                k+=1
                i+=1
            

        def mergeSort(arr, arrRef, l, r):
            if l == r:
                return arr, arrRef

            m = (l + r) // 2

            mergeSort(arr, arrRef, l, m)
            mergeSort(arr, arrRef, m + 1, r)
            merge(arr, arrRef, l, m, r)
            
            return arr, arrRef
        
# ------------------------------------------------------------------

        n = len(position)
        position, speed = mergeSort(position, speed, 0, n-1)

        s = []

        for i in range(n):
            time = (target - position[i]) / speed[i]

            if s and time <= s[-1]:
                pass
            else:
                s.append(time)
            
        return len(s)
        

