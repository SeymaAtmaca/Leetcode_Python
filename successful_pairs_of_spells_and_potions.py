# [-(-success // spell) for spell in spells]: 
# Bu ifade, her bir büyü (spell) için başarı 
# kriterine uygun minimum potion değerini hesaplar. 
# success'i spell'e böler ve yuvarlama yaparak minimum 
# potion değerini bulur.

# bisect_left(potions, minimum_potion): 
# bisect_left fonksiyonu, sıralı bir dizi 
# içinde belirli bir değeri arar ve bu değerin 
# dizideki pozisyonunu döner. Bu durumda, minimum 
# potion değerini (her büyü için) arar ve bu değerin 
# bulunduğu pozisyonu alır.


# [len(potions) - bisect_left(potions, -(-success // spell)) for spell in spells]: 
# Bu ifade, her bir büyü için başarı kriterine uygun minimum
# potion değerini hesaplar ve bu değerin, potions dizisindeki 
# pozisyonunu bulur. Daha sonra, potions dizisinin uzunluğundan bu 
# pozisyonu çıkartarak bu minimum değerin büyüden daha büyük veya eşit 
# kaç tane potion olduğunu bulur.


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        return potions.sort() or [len(potions) - bisect_left(potions, -(-success // spell)) for spell in spells]