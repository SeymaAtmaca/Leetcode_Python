# Çözümde, bir başlangıç değerinden hedef değere ulaşılmaya çalışılmaktadır.
# bu çözüm için başlangıç değeri üzerinde yalnızca eksiltme ve iki ile çarpma işlemleri yapılabilmektedir.
# Hedefe gidilebilmesi için gereken minimum adım sayısının bulunması istenmektedir.
# Problem için uygulanan çözüm aşağıda verilmiştir.
# ilk olarak hedef değerin başlangıç değerinden küçük olup olmama durumu gözlemlenir.
# eğer target < startValue ise burada sadece azaltma işlemi yapılabileceğinden return startValue - target uygulanır.
# ancak target değeri başlangıç değerinden büyükse, ilk olarak target ın çift olup olmama durumu incelenir. Çünkü çift olma durumunda /= 2 işlemi yapılabilmektedir.
# eğer target tek sayı ise 1 eklenir ve while loop ile tekrar devam edilir.
# while içinde her adımda step değeri tek tek arttırılır. Bu, - ve /= 2 için atılan adımları temsil eder.
# while bitiminde kullanılan step += startValue - target ise, ilk başta da anlatıldığı gibi artık target a ulaşmanın tek yolu azaltmak olduğu durumları ifade eder.
# tüm işlemlerin sonunda step değeri döndürülür.

class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        if target < startValue : return startValue - target
        step = 0

        while target > startValue:
            if target % 2 == 0: target /= 2
            else : target += 1
            step += 1
        step += startValue - target
        return step