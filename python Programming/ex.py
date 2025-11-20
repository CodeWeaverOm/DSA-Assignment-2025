print("Jayesh Chaware")
def is_balanced(expr):
    stack = []
    for ch in expr:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack:
                return False
            top = stack.pop()
            if(ch==')' and top!='(')or\
              (ch==']' and top!='[')or\
              (ch=='}' and top!='{'):
               return False
        return not stack
expr = input("Enter expression: ")
if is_balanced(expr):
    print("Parentheses are Balanced")
else:
    print("Parentheses are Not Balanced")