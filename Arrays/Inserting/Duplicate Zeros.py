class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        checkNext = True
        for n in range(len(arr)):
            if(checkNext):
                if(arr[n] == 0):
                    if(n + 1 < len(arr)):
                        arr.insert(n + 1, 0) 
                        arr.pop()
                        checkNext = False
            else:
                checkNext = True

        return arr