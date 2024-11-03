class Solution(object):
    def containsDuplicate(self, nums):
        # should use a set because they cant have repeat values, unlike traditional lists
        seen = set()
        for num in nums:
            # if we have seen the number before, return true
            if num in seen:
                return True
            # if not, then add this iteration to the set
            seen.add(num)
        # if no dupes, then false
        return False
