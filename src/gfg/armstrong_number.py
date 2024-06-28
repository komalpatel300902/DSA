class Solution:
    def armstrongNumber (self, n):
        a = (n % 10)**3
        b = ((n//10)%10)**3
        c = (n//100)**3
        if n == (a+b+c):
            return "true"
        return "false"
        