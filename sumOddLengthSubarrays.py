class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        n = len(arr)
        total = 0

        for i in range(n):
            left = i + 1
            right = n - i

            odd_left = (left + 1) // 2
            even_left = left // 2
            odd_right = (right + 1) // 2
            even_right = right // 2

            total += arr[i] * (odd_left * odd_right + even_left * even_right)

        return total
