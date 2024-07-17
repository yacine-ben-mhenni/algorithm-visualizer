class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if concatenated strings are equal or not, if not return ""
        print(f"Step 1: str1 + str2 = {str1 + str2}, str2 + str1 = {str2 + str1}")
        if str1 + str2 != str2 + str1:
            print("Step 1: The concatenations are not equal, returning an empty string.")
            return ""
        
        # Define a custom gcd function using the Euclidean algorithm
        def gcd(a, b):
            print(f"Calculating GCD of {a} and {b}")
            while b != 0:
                print(f"  a = {a}, b = {b}")
                a, b = b, a % b
                print(f"  New a = {a}, New b = {b}")
            print(f"GCD is {a}")
            return a
        
        # Calculate the GCD of the lengths of str1 and str2
        len1, len2 = len(str1), len(str2)
        print(f"Step 2: len(str1) = {len1}, len(str2) = {len2}")
        gcd_len = gcd(len1, len2)
        print(f"Step 3: gcd_len = {gcd_len}")
        
        # Return the substring from the beginning to the gcd length
        result = str1[:gcd_len]
        print(f"Step 4: The result substring is {result}")
        return result

# Example usage:
sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
print(sol.gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
print(sol.gcdOfStrings("LEET", "CODE"))    # Output: ""
