"""
165 比较版本号
比较两个版本号 version1 和 version2。
如果 version1 > version2 返回 1，如果 version1 < version2 返回 -1， 除此之外返回 0。

你可以假设版本字符串非空，并且只包含数字和 . 字符。

 . 字符不代表小数点，而是用于分隔数字序列。

例如，2.5 不是“两个半”，也不是“差一半到三”，而是第二版中的第五个小版本。

你可以假设版本号的每一级的默认修订版号为 0。例如，版本号 3.4 的第一级（大版本）和第二级（小版本）修订号分别为 3 和 4。其第三级和第四级修订号均为 0。
 

示例 1:

输入: version1 = "0.1", version2 = "1.1"
输出: -1


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/compare-version-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        split，转数字，0补齐，
        """
        version1 = version1.split('.')
        version2 = version2.split('.')
        version1 = [int(x) for x in version1]
        version2 = [int(x) for x in version2]
        lens1, lens2 = len(version1), len(version2)
        if lens1 > lens2:
            version2.extend([0 for _ in range(lens1 - lens2)])
        else:
            version1 = version1 + [0 for _ in range(lens2 - lens1)]
        for i in range(max(lens1, lens2)):
            if version1[i] > version2[i]:
                return 1
            if version1[i] < version2[i]:
                return -1
        return 0
