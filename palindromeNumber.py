class Solution:
    def isPalindrome(self, number: int) -> bool:
        if number < 0:
            return False
        inputString = str(number)
        n = len(inputString)
        i,j = 0,n-1
        while i < j:
            if inputString[i] != inputString[j]:
                return False
            i += 1
            j -= 1
        return True
