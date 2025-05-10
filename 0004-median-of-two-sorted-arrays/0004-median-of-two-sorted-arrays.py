class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        len1, len2 = len(nums1), len(nums2)

        total_len = len1 + len2
        half_len = total_len // 2

        left_1, right_1 = 0, len1 - 1

        while True:
            mid_1 = left_1 + (right_1 - left_1) // 2
            mid_2 = half_len - mid_1 - 2

            max_left_1 = nums1[mid_1] if mid_1 >= 0 else -inf
            min_right_1 = nums1[mid_1 + 1] if mid_1 + 1 < len1 else inf
            max_left_2 = nums2[mid_2] if mid_2 >= 0 else -inf
            min_right_2 = nums2[mid_2 + 1] if mid_2 + 1 < len2 else inf

            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                if total_len % 2 == 0:
                    return (
                        max(max_left_1, max_left_2) + min(min_right_1, min_right_2)
                    ) / 2
                else:
                    return min(min_right_1, min_right_2)
            elif max_left_1 > min_right_2:
                right_1 = mid_1 - 1
            else:
                left_1 = mid_1 + 1