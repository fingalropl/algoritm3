#
def broken_search(nums, searchable):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if searchable == nums[mid]:
            return mid
        elif nums[mid] <= nums[right]:
            if nums[mid] < searchable <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[left] <= searchable < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1
