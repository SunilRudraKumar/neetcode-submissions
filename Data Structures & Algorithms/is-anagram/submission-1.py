class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        bucket_array = [0]*26

        for i in range(len(s)):
            bucket_array[ord(s[i]) - ord('a')] += 1
            bucket_array[ord(t[i])- ord('a')] -= 1

        for i in range(len(bucket_array)):
            if bucket_array[i] != 0:
                return False
        return True