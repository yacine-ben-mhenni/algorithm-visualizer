class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenated strings are equal or not, if not return an empty string
        if str1 + str2 != str2 + str1:
            return ""

        # Define a custom gcd function using the Euclidean algorithm
        def gcd(a, b):
            while b != 0:        # Loop until b becomes 0
                a, b = b, a % b  # Replace a with b, and b with the remainder of a divided by b
            return a             # Return the GCD, which is now stored in a

        # Calculate the GCD of the lengths of str1 and str2
        gcd_len = gcd(len(str1), len(str2))
        
        # Return the substring of str1 from the beginning to the length of the GCD
        return str1[:gcd_len]