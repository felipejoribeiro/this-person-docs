---
id: valid_parentheses
aliases: []
tags: []
---

## Description:

Given a string s containing just the characters '(', ')', '{', '}', '\[' and '\]', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

#### Example 1:

Input: s = "()"

Output: true

#### Example 2:

Input: s = "()[]{}"

Output: true

#### Example 3:

Input: s = "(]"

Output: false

#### Example 4:

Input: s = "([])"

Output: true

#### Example 5:

Input: s = "([)]"

Output: false

### Constraints:

- 1 <= s.length <= 104
- s consists of parentheses only '()[]{}'.

### Authoral response:

```python
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
                    if ac[-1] == map[c]:
                        ac.pop(-1)
                        break
                    else:
                        return False
            else:
                return False

        if len(ac) > 0:
            return False

        return True
```

By observing other responses i found out that we don't need to iterate through all characters to check opening entries, we can check only the last element. Maybe that can make things faster, as this algorithm didn't perform well in the speed department. Memorywise its ok. After only checking the last character it made this algorithm the faster among then all.

### Best solution memory wise:

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"}": "{", ")": "(", "]": "["}
        for c in s:
            if c in pairs.values():
                stack.append(c)
            elif c in pairs.keys():
                if len(stack) > 0 and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False
```

The difference from the best memory solution is only that it used more dict operations to not use an additional variable.
