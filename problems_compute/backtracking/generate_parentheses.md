---
id: generate_parentheses
aliases: []
tags: []
---

## Description

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

Constraints:

1 <= n <= 8

## Study:

While creating examples i noticed that it only adds a parenthesis around and in each side of the previous iteration. I followed this alorithm based on the last step to create an iterative approcach.

()

((())), (()()) ()(()), (())(), ()()()

((())), (()())
()(()), ()()()
(())(), _()()()_

(((()))), ((()())), (()(())), ((())()), (()()())
()((())), ()(()()), ()()(()), ()(())(), ()()()()
((()))(), (()())(), _()(())()_, (())()(), _()()()()_

((((())))), (((()()))), ((()(()))), (((())())), ((()()())), (()((()))), (()(()())), (()()(())), (()(())()), (()()()()), (((()))()), ((()())()), ((())()())
()(((()))), ()((()()))

Tried a purely numerical interpretation without success:

n(i) = n(i-1) + (n(i-1) - 1) +

### My solution:

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sequence = [["()"]]
        if n == 0:
            return []

        for i in range(1, n):
            cur_step = []
            for ii in range(1, i + 1):
                step_from = sequence[ii - 1]
                lack = int(i + 1 - len(step_from[0]) / 2)
                for element in step_from:
                    cur_step.append(lack * "(" + element + lack * ")")
                    for particle in sequence[lack - 1]:
                        cur_step.append(particle + element)
                        cur_step.append(element + particle)

            sequence.append(list(set(cur_step.copy())))

        return sequence[-1]
```

### Recursive approach:

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        self.n = n
        currP = []
        def gen(openN, closedN):
            if openN == closedN and openN == self.n:
                output.append("".join(currP))
                return

            if openN < self.n:
                currP.append("(")
                gen(openN + 1, closedN)
                currP.pop()
            if closedN < openN:
                currP.append(")")
                gen(openN, closedN+1)
                currP.pop()

        gen(0, 0)
        return output
```
