class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            # 如果中间元素就是目标，直接返回
            if nums[mid] == target:
                return mid
            
            # 判断左半边是否有序
            # 注意：这里用 <= 是因为当 l==mid 时（只剩两个元素），左边也算有序
            if nums[l] <= nums[mid]:
                # 左半边 [l, mid] 是有序的
                # 检查 target 是否在这个有序区间内
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # 目标在左边
                else:
                    l = mid + 1  # 目标在右边
            else:
                # 右半边 [mid, r] 是有序的
                # 检查 target 是否在这个有序区间内
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # 目标在右边
                else:
                    r = mid - 1  # 目标在左边
                    
        # 没找到
        return -1