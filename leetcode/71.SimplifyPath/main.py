# coding=utf-8

class Solution(object):
    """
    给定一个文档 (Unix-style) 的完全路径，请进行路径简化。

    例如，
    path = "/home/", => "/home"
    path = "/a/./b/../../c/", => "/c"

    边界情况:

    你是否考虑了 路径 = "/../" 的情况？
    在这种情况下，你需返回 "/" 。
    此外，路径中也可能包含多个斜杠 '/' ，如 "/home//foo/" 。
    在这种情况下，你可忽略多余的斜杠，返回 "/home/foo" 。
    """
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        st = []
        i = 0
        while i < len(path):

            # 忽略重复的/，跳转到重复的/的最后一个
            while i + 1 < len(path) and path[i + 1] == '/':
                i += 1

            # 找到两个/之间分隔的内容
            j = i + 1
            while j < len(path) and path[j] != '/':
                j += 1
            p = path[i:j]
            if p == "/..":
                if st: st.pop()
            elif p == "/." or p == "/":
                pass
            else:
                st.append(p)

            i = j
        if not st:
            st.append("/")
        return "".join(st)

    def simplifyPath2(self, path):
        """
        :type path: str
        :rtype: str
        """
        # 采用分隔方式，先通过/分割成一个个字符数组，然后判断
        li = path.split('/')
        stack = []
        for s in li:
            if s == '' or s == '.':
                continue
            elif s == '..':
                if stack: stack.pop()
            else:
                stack.append(s)
        return '/' + '/'.join(stack)


if __name__ == '__main__':
    print Solution().simplifyPath("/home//foo/../../../")
