class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if len(stack) == 0:
                if c == ")" or c == "}" or c == "]":
                    return False
                stack.append(c)
            else:
                if c == "(" or c == "{" or c == "[":
                    stack.append(c)
                else:
                    if c == ")":
                        if stack[-1] == "(":
                            stack.pop()
                        else:
                            return False
                    elif c == "}":
                        if stack[-1] == "{":
                            stack.pop()
                        else:
                            return False
                    elif c == "]":
                        if stack[-1] == "[":
                            stack.pop()
                        else:
                            return False

        if len(stack) == 0:
            return True
        else:
            return False