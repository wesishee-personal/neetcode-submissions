class Solution:
    parenMap = {
        "(": ")",
        "[": "]",
        "{": "}",
    }


    def isValid(self, s: str) -> bool:
        parenStack = []
        for char in s:
            if char in self.parenMap:
                parenStack.append(char)
                continue
            if not parenStack:
                return False
            openParen = parenStack.pop()
            if self.parenMap[openParen] != char:
                return False

        if parenStack:
            return False
        return True