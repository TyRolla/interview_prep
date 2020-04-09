class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        i = 0
        for number in nums:
            count[number] += 1

        for value in range(len(count)):
            for num in range(count[value]):
                nums[i] = value
                i += 1
