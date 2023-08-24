# https://leetcode.com/problems/text-justification/

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        j = 0
        length = 0
        justifiedWords = []
        while j < len(words) or length:
            if j < len(words) and length + len(words[j]) + (j - i - 1) < maxWidth:
                length = length + len(words[j])
                j = j + 1
            else:
                noOfSpaces = maxWidth - length
                if j == len(words):
                    justifiedWords.append(
                        " ".join(words[i:j]) + (" " * (noOfSpaces - (j - i - 1))))
                else:
                    slots = j - i - 1
                    if slots == 0:
                        justifiedWords.append(words[i] + " " * noOfSpaces)

                    elif noOfSpaces % slots == 0:
                        justifiedWords.append(
                            (" " * (noOfSpaces // slots)).join(words[i: j]))

                    else:
                        spaces = noOfSpaces // slots
                        firstHalf = noOfSpaces % slots
                        justifiedWords.append(
                            (" " * (spaces + 1)).join(words[i:i+firstHalf]) + " " * (spaces+1) + (" " * spaces).join(words[i+firstHalf:j]))
                i = j
                length = 0
        return justifiedWords


def display(arr):
    for row in arr:
        print('|', row, '|', sep="")
    print()


display(Solution().fullJustify(words=[
    "This", "is", "an", "example", "of", "text", "justification."], maxWidth=16))

display(Solution().fullJustify(
    words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16))

display(Solution().fullJustify(words=["Science", "is", "what", "we", "understand", "well", "enough",
                                      "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], maxWidth=20))

display(Solution().fullJustify(words=["Science", "is", "what", "we", "understand", "well", "enough",
                                      "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], maxWidth=29))

display(Solution().fullJustify(words=["Science", "is", "what", "we", "understand", "well", "enough",
                                      "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], maxWidth=30))

display(Solution().fullJustify(words=[
        "a", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]*30, maxWidth=100))
