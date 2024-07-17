import matplotlib.pyplot as plt

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Initialize plot
        fig, ax = plt.subplots()
        ax.set_title('gcdOfStrings Algorithm Visualization')
        
        # Check if concatenated strings are equal or not
        if str1 + str2 != str2 + str1:
            ax.text(0.5, 0.6, "Concatenations are not equal,\nreturning empty string", ha='center', va='center', fontsize=12)
            ax.annotate('', xy=(0.4, 0.5), xytext=(0.6, 0.7),
                        arrowprops=dict(facecolor='black', shrink=0.05))
            ax.text(0.4, 0.45, "Return ''", ha='center', va='center', fontsize=10)
            plt.axis('off')
            plt.show()
            return ""
        
        # Define a custom gcd function using the Euclidean algorithm
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        # Calculate the GCD of the lengths of str1 and str2
        gcd_len = gcd(len(str1), len(str2))
        
        # Plot GCD calculation step
        ax.annotate(f'GCD of lengths:\n{len(str1)}, {len(str2)}', xy=(0.5, 0.8), xycoords='axes fraction',
                    xytext=(0.2, 0.9), textcoords='axes fraction',
                    arrowprops=dict(facecolor='black', shrink=0.05),
                    fontsize=10, ha='center', va='center')
        
        # Plot substring extraction step
        ax.annotate(f'Return substring\n"{str1[:gcd_len]}"', xy=(0.5, 0.4), xycoords='axes fraction',
                    xytext=(0.7, 0.3), textcoords='axes fraction',
                    arrowprops=dict(facecolor='black', shrink=0.05),
                    fontsize=10, ha='center', va='center')

        plt.axis('off')
        plt.show()
        
        return str1[:gcd_len]

# Example usage:
sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
