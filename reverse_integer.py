# ===================== Turkish ==========================
# Bu çözüm, dizi işlemleri ve int to string - string to integer işlevlerini kullanır. 
# İlk olarak, x'in işaretini buluruz. Eğer x 0'dan küçükse, işaret -1'e eşit olur veya x 0'dan büyükse, işaret 1'e eşit olur. 
# İşaret değeri sonuç işareti için oluşturulur. Bu nedenle, ret değerini işaret değeri ile çarpıyoruz. 
# Son kısımda, ret değeri -2^31 -1'den küçükse veya 2^31'den büyükse, 0 döndürüyoruz. Çünkü bu değer, tam sayı aralığında değildir.

# Karmaşıklık
# Zaman karmaşıklığı:
# O(n)

# Alan karmaşıklığı:
# O(n)



# ================== English ============================
# Approach
# Easy to understand solution with Python. This solution is use array operations and int to string - string to integer functions. 
# At first, we find x sign. If x smaller than 0, sign equal to -1 or x bigger than 0, sign equal to 1. Sign value is 
# creating for results sign. Because of this, we multiply ret value with sign value. At the final part, if ret value smaller than -2^31 -1 or 
# bigger than 2^31, we return 0. Because this value is not between integer range.

# Complexity
# Time complexity:
# O(n)

# Space complexity:
# O(n)




class Solution:
    def reverse(self, x: int) -> int:
        sign =1 if x >= 0 else -1
        ret =  int(str(abs(x))[::-1]) * sign
        return 0 if ret <= (-1)*pow(2,31) or ret >= pow(2,31)-1 else ret