class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {"}":"{","]":"[",")":"("}
        closed_parenthesis = parenthesis.keys()
        opened_parenthesis = parenthesis.values()
        for x in range(len(s)):
            # print("Stack in Entrata {}".format(stack))
            # print("analizzo {}".format(s[x]))
            if s[x] in opened_parenthesis:
                stack.append(s[x])
            else:
                if len(stack) > 0:
                    if stack[-1] == parenthesis[s[x]]:
                        stack.pop()
                    else:
                        # print("Valore Precedente {}, confronto con {}".format(s[x-1],parenthesis[s[x]]))
                        return False
                else:
                    return False
            # print("Stack in Uscita {}".format(stack))
        if len(stack) > 0:
            return False
        else:
            return True
                
x = Solution()
print(x.isValid("(([])){}([[])"))