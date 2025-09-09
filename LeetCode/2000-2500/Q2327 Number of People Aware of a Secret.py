class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10 ** 9 + 7
        # 1 know the message
        # The person will share the secret to one person per day
        # The person will forget the secret after FORGET days
        # The person whom discover the secret will wait DELAY days until start to share the secret

        know = 1
        share = 0
        will_share = [0] * (n + delay)
        will_forget = [0] * (n + forget)

        will_share[delay] = 1
        will_forget[forget] = 1

        for k in range(delay, n):
            share += will_share[k]
            share -= will_forget[k]

            know += share
            know -= will_forget[k]

            will_share[k + delay] = share
            will_forget[k + forget] = share

        return know % mod


s = Solution()
print(s.peopleAwareOfSecret(n=6, delay=2, forget=4))
print(s.peopleAwareOfSecret(n=4, delay=1, forget=3))
