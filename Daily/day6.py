# Day 6 • Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.
# - Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Constraints:
# •    1 <= s.length <= 104
# •    s consists of parentheses only '()[]{}'.

def parentheses_valid(s: str) -> bool:
    depth = { '(': 0, '{': 0, '[': 0 }
    paren_pairs = { ')': '(', ']': '[', '}': '{'}
    
    for c in s:
            if c in depth.keys():
                depth[c] += 1
            else:
                depth[paren_pairs[c]] -= 1
                if depth[paren_pairs[c]] < 0:
                    return False

    for v in depth.values():
        if v != 0:
            return False

    return True
    

def main():
    print(parentheses_valid(input()))


if __name__ == '__main__':
    main()