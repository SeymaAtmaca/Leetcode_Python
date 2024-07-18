'''
Aşağıdaki çözüm yönteminde dinamik programlama mantığı kullanılmaktadır.
İlk olarak sol baştan elemanlar tek tek sırayla çarpılır ve left array'ine eklenir.
Daha sonra sağ baştan yani tersten çarpımları alacak yeni bir array oluşturulur ve 
bu array üzerinde gezinirken aynı zamanda left array'i de güncellenir. 
Çünkü right ve left array'lerinde karşılıklı eleman çarpımları sonuç değeri oluşturmaktadır.
En son aşamada da left array'i nihai sonucu içerdiğinden return edilir.

Örnek Kullanım:
nums = [1, 2, 3, 4]
Adım adım left ve right array'leri:
Başlangıçta:
left = [1, 1, 1, 1]

Sol baştan çarpımlarla left array'in doldurulması:
Adım 1: left = [1, 1, 1, 1] (left[1] = left[0] * nums[0] = 1 * 1)
Adım 2: left = [1, 1, 2, 1] (left[2] = left[1] * nums[1] = 1 * 2)
Adım 3: left = [1, 1, 2, 6] (left[3] = left[2] * nums[2] = 2 * 3)

Sağ baştan çarpımlarla left array'in güncellenmesi:
Başlangıçta right = nums[-1] = 4
Adım 1: left = [1, 1, 8, 6] (left[2] = left[2] * right = 2 * 4)
        right = right * nums[2] = 4 * 3 = 12
Adım 2: left = [1, 12, 8, 6] (left[1] = left[1] * right = 1 * 12)
        right = right * nums[1] = 12 * 2 = 24
Adım 3: left = [24, 12, 8, 6] (left[0] = left[0] * right = 1 * 24)
        right = right * nums[0] = 24 * 1 = 24

Sonuç:
left = [24, 12, 8, 6]


'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n

        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        
        right = nums[-1]
        for i in range(n-2, -1, -1):
            left[i] *= right
            right *= nums[i]
        
        return left
        