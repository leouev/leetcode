class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res = []
        compledict = {}
        for posi in range(len(nums)):
            num = nums[posi]
            comp = target - num
            compledict[comp] = posi
        
        for numpos in range(len(nums)):
            if nums[numpos] in compledict and numpos != compledict.get(nums[numpos]):
                res= [numpos,compledict.get(nums[numpos])]
                break
        return res
