from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the maximum number of candies any kid currently has
        maxCandies = max(candies)
        
        # Initialize the result list
        result = []
        
        # Iterate through each kid's candies
        for i in range(len(candies)):
            # Check if the current kid's candies plus the extra candies is at least the maximum number of candies
            if candies[i] + extraCandies >= maxCandies:
                # If true, append True to the result list
                result.append(True)
            else:
                # Otherwise, append False to the result list
                result.append(False)
        
        # Return the result list
        return result

# Example 1
candies1 = [2, 3, 5, 1, 3]  # List of candies each kid has
extraCandies1 = 3  # Number of extra candies available
solution = Solution()
# Print the result of the method for example 1
print(solution.kidsWithCandies(candies1, extraCandies1))  # Output: [True, True, True, False, True]

# Example 2
candies2 = [4, 2, 1, 1, 2]  # List of candies each kid has
extraCandies2 = 1  # Number of extra candies available
# Print the result of the method for example 2
print(solution.kidsWithCandies(candies2, extraCandies2))  # Output: [True, False, False, False, False]

# Example 3
candies3 = [12, 1, 12]  # List of candies each kid has
extraCandies3 = 10  # Number of extra candies available
# Print the result of the method for example 3
print(solution.kidsWithCandies(candies3, extraCandies3))  # Output: [True, False, True]
