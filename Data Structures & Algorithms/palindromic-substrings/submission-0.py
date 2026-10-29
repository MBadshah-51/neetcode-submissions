class Solution:
    def traverse(self, s, i, j):
        count = 0
        n = len(s)

        while 0<= i and j < n and \
            s[i] == s[j]:
            count += 1
            i -= 1
            j += 1
        
        return count

    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        for start in range(n):
            #odd length
            i = j = start
            count += self.traverse(s, i , j)

            #even length
            i = start
            j = start + 1
            count += self.traverse(s, i, j)
        
        return count