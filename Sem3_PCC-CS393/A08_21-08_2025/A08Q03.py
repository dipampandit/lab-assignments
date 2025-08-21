# Longest Balanced Substring of Parentheses
# Prompt: Return length of longest valid parentheses substring.

def longest_valid_parentheses(s):
    count = 0
    for i in range(len(s) - 1):
        if s[i] == "(" and s[i+1] == ")":
            count += 1
    return count

# Examples
print(longest_valid_parentheses("(()"))      # 1
print(longest_valid_parentheses(")()())"))   # 2
print(longest_valid_parentheses(""))         # 0
