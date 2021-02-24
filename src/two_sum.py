class Solution:
    def twoSum(self, nums, target):
        map = {}
        for (index, value) in enumerate(nums):
            if target - value in map:
                return [map[target - value], index]
            map[value] = index
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], target=9))