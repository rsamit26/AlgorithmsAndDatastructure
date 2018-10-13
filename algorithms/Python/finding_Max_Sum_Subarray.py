class Solution:

    def find_max_crossing_subarray(self, arr, low, mid, high):

        left_sum = -100000000000000
        sm = 0
        max_left = 0
        max_right = 0
        for i in range(mid, low - 1, -1):
            sm += arr[i]
            if sm > left_sum:
                left_sum = sm
                max_left = i

        right_sum = -100000000000
        sm = 0
        for i in range(mid + 1, high):
            sm += arr[i]
            if sm > right_sum:
                right_sum = sm
                max_right = i

        return max_left, max_right, left_sum + right_sum

    def find_max_subarray(self, arr, low, high):

        if low == high:
            return low, high, arr[low]
        else:
            mid = (low + high) // 2
            left_low, left_high, left_sum = self.find_max_subarray(arr, low, mid)
            right_low, right_high, right_sum = self.find_max_subarray(arr, mid + 1, high)
            cross_low, cross_high, cross_sum = self.find_max_crossing_subarray(arr, low, mid, high)

            if right_sum >= left_sum and right_sum >= cross_sum:
                return right_low, right_high, right_sum
            elif left_sum >= right_sum and left_sum >= cross_sum:
                return left_low, left_high, left_sum
            else:
                return cross_low, cross_high, cross_sum
