from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        strs = []
        nums = []

        for log in logs:
            first_token = log.split()[1]
            if first_token.isdigit():
                nums.append(log)
            else:
                strs.append(log)

        return sorted(strs, key=lambda x: (x.split()[1:], x.split()[0])) + nums


if __name__ == '__main__':
    s = Solution()

    actual1 = s.reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])
    expected1 = ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
    assert actual1 == expected1

    actual2 = s.reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"])
    expected2 = ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
    assert actual2 == expected2
