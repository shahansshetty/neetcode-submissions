class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return True if len(format(n,'b').strip("0")) == 1 else False
        