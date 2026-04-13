class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        open_brackets = set([
            "{",
            "(",
            "[",
        ])
        mapping = {
            "}": "{",
            ")": "(",
            "]": "[",
        }
        for ch in s:
            isOpen = ch in open_brackets
            if not st and not isOpen:
                return False
            
            if isOpen:
                st.append(ch)
                continue
            
            last = st[-1]
            
            if mapping[ch] != last:
                return False
            st.pop()
        
        return len(st) == 0