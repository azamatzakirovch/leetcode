# class Solution:
#
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         substring = ""
#         length = len(s)
#         result = 1
#         i = 0
#
#         def is_available(word):
#             resultat = True
#             l = len(word)
#
#             for i in word:
#                 if word.count(i) > 1:
#                     resultat = False
#                     break
#
#             return resultat
#
#         while i < length - 1:
#
#             for j in range(i, length):
#                 substring += s[j]
#                 if is_available(substring):
#                     if len(substring) > result:
#                         result = len(substring)
#                 else:
#                     substring = ""
#                     break
#
#             i += 1
#
#         return result

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}  # char -> last index
        left = 0
        best = 0

        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                # ch repeats inside current window; move left past its previous spot
                left = last[ch] + 1
            last[ch] = right
            best = max(best, right - left + 1)

        return best


a = Solution()

print(a.lengthOfLongestSubstring("pwwkew"))