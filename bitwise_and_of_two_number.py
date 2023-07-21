# verilen left ve right degerleri [left, right] seklinde bir aralik olarak dusunulur,
# bu araliga dahil olan butun sayilarin and lenmesi sonucu elde edilen sayi bulunmaya calisilir.
# cozumde, shift islemleri kullanilmistir.
# her adimda bir basamak saga shift edilir. Eger dongu sonucu elde edilen left ve right degeri esitlenirse,
# yani farkli basamaklarin shiftlenmesi islemi biterse, left degeri ile elde edilen sonuc shift degiskeni kadar sola tekrar shiftlenir. Elde edilen deger dondurulur.
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
     
        shift = 0
        while(left < right):
            left >>=1 # bit degeri bir bit saga shift edilir. orn ilk adimda 0101 iken 0010 olur
            right >>=1 # bit degeri bir bit saga shift edilir. orn ilk adimda 0111 iken 0011 olur
            shift += 1 # shift degeri bir arttirilir. bu sayede sola kaydirmada kullanilacak deger guncellenir.
        return left << shift # left ve right degerleri esitlendiginde, kac adet shift yapildiysa o kadar sola shift islemi uygulanir.