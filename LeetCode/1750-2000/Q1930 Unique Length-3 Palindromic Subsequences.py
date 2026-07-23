from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = set()
        right = defaultdict(int)
        for c in s:
            right[c] += 1

        res = set()
        for c in s:
            right[c] -= 1
            if right[c] == 0:
                del right[c]
            for x in left:
                if x in right:
                    res.add(x + c)
            left.add(c)

        return len(res)

    def countPalindromicSubsequence2(self, s: str) -> int:
        chars = set(s)
        res = 0
        for ch in chars:
            first = s.find(ch)
            last = s.rfind(ch)

            if first != last:
                res += len(set(s[first + 1:last]))

        return res


s = Solution()
print(s.countPalindromicSubsequence(s="aabca"))
print(s.countPalindromicSubsequence(s="adc"))
print(s.countPalindromicSubsequence(s="bbcbaba"))
print(s.countPalindromicSubsequence(
    s="cmrbntqnmmijssmgkxpaffwkhxoyjodcljpmqlmkuijegqjcvnquycbaffihvrhszzttxahvukkprmntdkftmnutsluieusflojpdyavvikrkuniauxdyiqppwzfknecolxccoarmebzhgrbbnewkecnmbywdflsmpypnrhadbkunxwlothwlsshpvegxtlxeokygwhqhxssfmzozbctilgnmbstjtwkacxitmbogydvveachnkctrdjfarfsvvqsxkibautyjgckzierfwuveekcioefoydfjekiklbvqjbfhpzcnzweypzsrzsiqwiwmippjqgpzgqxittqbjhdfaypytihqtnzqhawigoxrgrspjilawbfqdfcpvygcsisgeghlqhuczkelnttvuajwtxpdsgmljpbdmeeansmyyzjmqpkbxkoflgxsnmrsqytgavqrsqglrgpyvauqxkpxnekvghzrjikwscquidtykizvabsnrtejsfeylvebetgxkqqwehjhipmrcbtapzcnapztymiljxzvyrjbjiclssxdpwhsvjqrmkezyvajbuilpkpclyyzwxthfdnownduhroweldrgftrclseyxtfgmxddnscrwytpqjstjqowvfdcctytdjwyoabnwzijrunpfknldyvmlpdruspizdzsmvmsjzivftvsbwemkzrwzoirztknhsfwkdtpuwsledshdfttasorzdylvyczebzqpzqkagmryqjruruwqhqjdcmrnaoohtuemqlocbxuevaonvmnpsudtzxepeouddfeowaznjokyahynurlpsnzjnfcvgehvypfjd"))
print(s.countPalindromicSubsequence2(s="aabca"))
print(s.countPalindromicSubsequence2(s="adc"))
print(s.countPalindromicSubsequence2(s="bbcbaba"))
print(s.countPalindromicSubsequence2(
    s="cmrbntqnmmijssmgkxpaffwkhxoyjodcljpmqlmkuijegqjcvnquycbaffihvrhszzttxahvukkprmntdkftmnutsluieusflojpdyavvikrkuniauxdyiqppwzfknecolxccoarmebzhgrbbnewkecnmbywdflsmpypnrhadbkunxwlothwlsshpvegxtlxeokygwhqhxssfmzozbctilgnmbstjtwkacxitmbogydvveachnkctrdjfarfsvvqsxkibautyjgckzierfwuveekcioefoydfjekiklbvqjbfhpzcnzweypzsrzsiqwiwmippjqgpzgqxittqbjhdfaypytihqtnzqhawigoxrgrspjilawbfqdfcpvygcsisgeghlqhuczkelnttvuajwtxpdsgmljpbdmeeansmyyzjmqpkbxkoflgxsnmrsqytgavqrsqglrgpyvauqxkpxnekvghzrjikwscquidtykizvabsnrtejsfeylvebetgxkqqwehjhipmrcbtapzcnapztymiljxzvyrjbjiclssxdpwhsvjqrmkezyvajbuilpkpclyyzwxthfdnownduhroweldrgftrclseyxtfgmxddnscrwytpqjstjqowvfdcctytdjwyoabnwzijrunpfknldyvmlpdruspizdzsmvmsjzivftvsbwemkzrwzoirztknhsfwkdtpuwsledshdfttasorzdylvyczebzqpzqkagmryqjruruwqhqjdcmrnaoohtuemqlocbxuevaonvmnpsudtzxepeouddfeowaznjokyahynurlpsnzjnfcvgehvypfjd"))
