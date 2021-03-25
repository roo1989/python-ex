"""
In this Kata, we are going to reverse a string while maintaining spaces.

For example:

solve("our code") = "edo cruo"
-- Normal reversal without spaces is "edocruo". 
-- However, there is a space after the first three characters, hence "edo cruo"

solve("your code rocks") = "skco redo cruoy"
solve("codewars") = "srawedoc"
More examples in the test cases. All input will be lower case letters and in some cases spaces.

Good luck!
"""

def solve(s):
    out = []
    for key, value in enumerate(s.split()):
        if s[key] == ' ':
            out[key] = ' '
        out.append(value[::-1])

    return out

# print(solve("codewars"),"srawedoc")
# print(solve("your code"),"edoc ruoy")
print(solve("your code rocks"),"skco redo cruoy")
# print(solve("i love codewars"),"s rawe docevoli")