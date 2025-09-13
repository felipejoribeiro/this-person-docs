class Solution:
    def isValid(self, s: str) -> bool:
        op = "({["
        map = {")": "(", "]": "[", "}": "{"}
        ac = []
        for c in s:
            if c in op:
                ac.append(c)
            elif map[c] in ac:
                for i in range(len(ac)):
                    if ac[len(ac) - 1 - i] == map[c]:
                        ac.pop(len(ac) - 1 - i)
                        break
                    else:
                        return False
            else:
                return False

        if len(ac) > 0:
            return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("([)]"))
    print(s.isValid("{[]}"))
    print(s.isValid("]"))
    print(s.isValid("([)]"))
    print(s.isValid("{([]{})[{}]}"))
