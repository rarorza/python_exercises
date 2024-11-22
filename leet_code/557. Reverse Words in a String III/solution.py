"""
Given a string s, reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"

Constraints:

    1 <= s.length <= 5 * 104
    s contains printable ASCII characters.
    s does not contain any leading or trailing spaces.
    There is at least one word in s.
    All the words in s are separated by a single space.
"""

import re


class Solution:
    def reverseWords(self, s: str):
        new_string = ""
        for word in re.split(r"(\s+)", s):
            # regular expression to split string keeping spaces
            new_string += "".join([word[::-1]])
        return new_string


s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
