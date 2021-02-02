class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a={}
        for i in range(len(nums)):
            if nums[i] not in a:
                a[nums[i]]=[i]
            else:
                for j in a[nums[i]]:
                    if abs(j-i)<=k:
                        return True
                a[nums[i]].append(i)
        else:
            return False