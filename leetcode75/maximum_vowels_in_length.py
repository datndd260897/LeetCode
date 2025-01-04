# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.
# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.

class Solution:
    def __init__(self):
        pass

    def maxVowels(self, s: str, k: int) -> int:
        current_vowels = 0
        vowels = ['a', 'i', 'u', 'e', 'o']
        for index in range(k):
            current_vowels += 1 if s[index] in vowels else 0
        max_vowels = current_vowels
        for j_index in range(k, len(s)):
            current_vowels += 1 if s[j_index] in vowels else 0
            current_vowels -= 1 if s[j_index - k] in vowels else 0
            max_vowels = current_vowels if current_vowels > max_vowels else max_vowels
        return max_vowels

if __name__ == "__main__":
    solution = Solution()
    s, k = "abciiidef", 3
    print(solution.maxVowels(s, k))
    pass    