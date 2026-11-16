"""

primes = 2, 3, 5, 7

even  = 0, 2, 4, 6, 8



c(1) = 5 = 5
c(2) = 5 * 4 = 20
c(3) = 5 * 4 * 5 = 100
c(4) = 5 * 4 * 4 * 4 = 400


c(n) = 5**((n + 1)//2) * 4**((n)// 2)


"""

class Solution:
    def countGoodNumbers(self, n: int) -> int:

        def exp(num, pow):
            if pow == 0:
                return 1
            
            if pow == 1:
                return num

            mod = 10**9 + 7

            if pow % 2 == 1:
                return (num * exp(num, pow - 1)) % mod

            sqrt = exp(num, pow // 2)

            return (sqrt * sqrt) % mod          

        mod = 10**9 + 7

        return (exp(5, (n + 1)// 2) * exp(4, n//2)) % mod
        
        