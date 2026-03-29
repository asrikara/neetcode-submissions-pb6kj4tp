class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ""  # Initialize as empty string
        for word in strs:
            s += str(len(word)) + "#" + word  # Concatenate, don't overwrite
        return s

    def decode(self, s: str) -> List[str]:
        result, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # Fixed: s instead of str
            result.append(s[j+1: j+1+length])  # Fixed: s instead of str
            i = j + 1 + length

        return result