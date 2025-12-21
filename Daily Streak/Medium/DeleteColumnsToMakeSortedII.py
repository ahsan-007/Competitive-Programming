# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/description/?envType=daily-question&envId=2025-12-21

from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def minDeletionSizeUtil(indicesList, i):
            if i == len(strs[0]):
                return set()

            newIndices = {}
            for ind, indices in enumerate(indicesList):
                prev = indices[0]
                for j, curr in enumerate(indices):
                    if j != 0:
                        if strs[curr][i] < strs[prev][i]:
                            return minDeletionSizeUtil(indicesList, i + 1).union({i})

                        elif strs[curr][i] == strs[prev][i]:
                            key = str(ind) + strs[prev][i]
                            if key not in newIndices:
                                newIndices[key] = [prev]
                            newIndices[key].append(curr)
                        prev = curr
            return minDeletionSizeUtil(list(newIndices.values()), i + 1)

        return len(minDeletionSizeUtil(indicesList=[list(range(len(strs)))], i=0))


print(Solution().minDeletionSize(strs=["ca", "bb", "ac"]))
print(Solution().minDeletionSize(strs=["xc", "yb", "za"]))
print(Solution().minDeletionSize(strs=["zyx", "wvu", "tsr"]))
print(Solution().minDeletionSize(strs=["xga", "xfb", "yfa"]))
print(Solution().minDeletionSize(strs=["phpaajubqf", "rhvacwugqw", "abcajijvtf", "bluaezyszu", "gmrbbvfviz", "nembvwxrqd", "hwwdinzrih", "ybwdrxqwsb", "zpmdmbykwx", "osiepcimqf", "zyoeowsuwj", "dekesgloyy", "kyxffyfjhf", "rhpfgcifqt", "zpkfnhjrsv", "rfrgvrpjaj", "kzugskjfue", "aktgrqouur", "ijihcgokrw", "vvwhluuytu", "yxmhqvylyp", "fajjpmmuui", "nqrkjpfmie", "fyzkvqlszh", "fmplsygefa", "holleodgnm", "wcgmwozkmn", "frwmbkwdzj", "kmcnkjznix", "kgvnfxuwzj", "mdxooewtei", "cbhqxmwbhl", "ykpszopyda", "mzhsqhsciv", "myetjllmhp", "gjdthdgpoa", "dcyulyxvah", "lwdueykggs", "bhturgdcxo", "oycvmeynar", "qsxwasalck", "rdxwfpasqk", "fkqwyoyvqv", "anewamiyry", "rnmwvxpzus", "qvkwghuaut", "rstyvhkahy", "deayxjdxre", "drgypdopvm", "dcwzxlspcl"]
                                 ))
