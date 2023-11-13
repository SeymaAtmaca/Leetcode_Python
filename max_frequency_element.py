# https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/

# kayan pencere mantığı ile çözüm elde edilmiştir.
# pencere boyutunu i ve j değerleri belirtir.
# pencerenin büyüklüğünü kontrol etmek için total ve k değişkenleri kullanılır.
# eğer pencere boyutu beklenenden büyükse pencere alt sınırını belirten i değeri bir arttırılır ve total değişkeni nums[i] kadar azaltılır.
# burada pencerenin en son beklenen değeri nums[j] * pencere boyutu kadar olduğu için j-i+1 işlemine göre kontrol yapılır.
# en son güncellemelerle elde edilen pencere boyutunu yenilemek için maxlen değişkeni önceki pencere boyutu ile mevcut boyut karşılaştırılarak elde edilir. 
# maxlen değişkeni return edilir. 

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, total, maxlen = 0,0,1

        for j in range(len(nums)):
            total += nums[j]

            while nums[j] * (j - i + 1) > total + k :
                total -= nums[i]
                i += 1

            maxlen = max(maxlen, j-i+1)

        return maxlen 