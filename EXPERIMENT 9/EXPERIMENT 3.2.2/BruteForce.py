
class Solution:
    def lcs(self, text1, text2, i, j):
        # If either string is empty
        if i == 0 or j == 0:
            return 0

        # If characters match
        if text1[i - 1] == text2[j - 1]:
            return 1 + self.lcs(text1, text2, i - 1, j - 1)

        # If characters do not match
        return max(
            self.lcs(text1, text2, i - 1, j),
            self.lcs(text1, text2, i, j - 1)
        )

    def longestCommonSubsequence(self, text1, text2):
        return self.lcs(text1, text2, len(text1), len(text2))


obj = Solution()

text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

print("Length of LCS:", obj.longestCommonSubsequence(text1, text2))
