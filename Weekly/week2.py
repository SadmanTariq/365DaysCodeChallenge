def get_pivot(nums):
    left = 0
    right = len(nums)
    mid = int((right - left) / 2)

    while left != right:
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid - 1
        mid = int((right - left) / 2)

    return mid

print(get_pivot([4,5,6,7,0,1,2]))