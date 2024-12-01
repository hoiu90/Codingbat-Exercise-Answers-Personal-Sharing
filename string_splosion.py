def string_splosion(s):
    result = ""
    for i in range(len(s)):
        result += s[:i+1]
    return result

print(string_splosion("Code")) # Output: "CodeCoDeCoDeCoDe"
print(string_splosion("abc")) # Output: "aababcabc"
print(string_splosion("ab")) # Output: "aab"