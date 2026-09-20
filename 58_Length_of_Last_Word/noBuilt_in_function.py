class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i, length = len(s) - 1, 0     # starting at the last index

        while s[i] == " ":     #stripping off the trailing spaces
            i -= 1     #getting to the last character if there is space

        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length
