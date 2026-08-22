class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)

        encoded_str = ""

        for string in strs:
            encoded_str += str(len(string)) + "#" + string
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        n = len(s)
        result = []
        if not s or not s[0].isdigit():
            return []
        
        i = 0
        while i < n:
            j = i
            while s[j].isdigit():
                j += 1
            length = int(s[i:j])
            
            i = j + 1

            string = s[i:i + length]
            i = i + length
            result.append(string)
        
        return result
