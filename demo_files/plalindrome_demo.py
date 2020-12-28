# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         is_palindromic_string = lambda s: s == s[::-1]
#
#         str_length = len(s)
#         cur_length = 0
#         start_index = 0
#         for i in range(str_length):
#
#             cur_start_index = i - cur_length - 1                                # 向左扩展一个字符
#             cur_substr = s[cur_start_index: cur_start_index+cur_length+2]       # 向右扩展一个字符，获得子串
#
#             if cur_start_index >= 0 and is_palindromic_string(cur_substr):      # 判断扩展后的子串是否回文
#                 start_index = cur_start_index                                   # 更新子串起始下标
#                 cur_length += 2                                                 # 更新当前最长子串长度
#
#             else:
#                 cur_start_index = i - cur_length                                # 向左不扩展
#                 cur_substr = s[cur_start_index: cur_start_index+cur_length+1]   # 向右扩展一个字符，获得子串
#                 if cur_start_index >= 0 and is_palindromic_string(cur_substr):  # 判断扩展后的子串是否回文
#                     start_index = cur_start_index                               # 更新子串起始下标
#                     cur_length += 1                                             # 更新当前最长子串长度
#
#         return s[start_index: start_index + cur_length]

class Solution:
    def longestPalindrome(self, s):
        def extend(start_idx, end_idx, max_start, max_len):
            """
            扩展函数，用于得到向左向右同步扩展后的最长回文子串
            :param start_idx: 向左扩展的起始位置
            :param end_idx: 向右扩展的起始位置
            :param max_start: 当前最长回文子串的左指针
            :param max_len: 当前最大长度
            :return: 当前最长回文子串的起始位置和长度
            """

            while 0 <= start_idx <= end_idx < len(s):   # 子串起止下标合法时
                if s[start_idx] == s[end_idx]:          # 如果新增的两端字符相等
                    # cur_str = s[start_idx:end_idx]      # 当前子串是回文串
                    cur_len = end_idx + 1 - start_idx   # 当前子串长度
                    if max_len < cur_len:
                        max_len = cur_len
                        max_start = start_idx
                    start_idx -= 1                      # 左指针向左移动一位
                    end_idx += 1                        # 右指针向右移动一位
                else:
                    break
            return max_start, max_len

        max_start, max_len = 0, 0                       # 初始化最长回文子串开始位置及长度

        for i in range(len(s)):                         # 进行一次遍历
            left = right = i                            # 判断长度为奇数的回文子串开始和结束位置
            # 从i位置向两边扩展，搜寻可以得到的最大回文子串
            max_start, max_len = extend(left, right, max_start, max_len)

            left, right = i, i+1                        # 判断长度为偶数的回文子串开始和结束位置
            # 从i位置向左扩展，从i+1位置向右扩展，搜寻可以得到的最大回文子串
            max_start, max_len = extend(left, right, max_start, max_len)

        return s[max_start:max_start + max_len]


s = Solution()
print(s.longestPalindrome('abcdef'))