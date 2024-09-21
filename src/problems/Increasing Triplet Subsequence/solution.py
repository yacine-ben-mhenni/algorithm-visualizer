class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num  # update first if num is smaller than or equal to first
            elif num <= second:
                second = num  # update second if num is smaller than or equal to second
            else:
                # num is greater than both first and second
                return True

        return False
