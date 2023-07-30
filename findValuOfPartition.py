class Solution(object):
    def findValueOfPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # soruda, verilen diziyi alt iki diziye donusturmek ve bu iki diziden birinden min sayıyı digerinden maks sayıyı alarak,
        # min seviyedeki a-b cıktısının bulunamsı istenmektedir. 
        
        # bu cozum oldukca hızlı ( 382 ms 100% beats), ancak bellek kullanımı zip() sebebiyle cok yuksek ( 33.10mb, 5.00%)
        nums.sort()
        # ikililer oluşturmak için zip(nums, nums[1:]) yapıyoruz.
        # burada donen ikililer (1,2), (2,3), (3,4)

        return min(b-a for a,b in zip(nums, nums[1:]))