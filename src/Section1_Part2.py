def is_balanced(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack: return False
            stack.pop()
    return not stack

def is_anbn(s):
    stack = []
    for c in s:
        if c == 'a':
            stack.append(c)
        elif c == 'b':
            if not stack or stack[-1] != 'a': return False
            stack.pop()
    return not stack


tests = [
    ("(())", is_balanced),
    ("()()", is_balanced),
    ("(()", is_balanced),
    ("aabb", is_anbn),
    ("aaabbb", is_anbn),
    ("aab", is_anbn)
]

for s, checker in tests:
    print(f"'{s}': {'Accepted' if checker(s) else 'Rejected'}")