class BruteForceSolution:
    def findDuplicate(self, nums: list[int]) -> int:
        seen = set()
        for x in nums:
            if x in seen:
                return x
            seen.add(x)
        return -1