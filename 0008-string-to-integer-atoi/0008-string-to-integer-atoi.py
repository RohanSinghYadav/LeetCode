class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        n = len(s)
        if n == 0:
            return 0

        i = 0
        sign = 1

        if s[0] == '-':
            sign = -1
            i = 1
        elif s[0] == '+':
            i = 1

        num = 0
        limit = 2147483648 if sign < 0 else 2147483647
        cutoff, last = divmod(limit, 10)

        while i < n:
            c = s[i]
            if c < '0' or c > '9':
                break

            d = ord(c) - 48
            if num > cutoff or (num == cutoff and d > last):
                return -limit if sign < 0 else limit

            num = num * 10 + d
            i += 1

        return sign * num