class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        v1, v2 = 0, -prices[0]
        # v2 ' nin -prices[0] olmasının sebebi, mümkün olan en karlı alımın yapılması,
        # hisse senetleri düştüğü zaman alım işlemi gerçekleştiriliyor. Böylece en karlı alış-veriş sağlanmış oluyor
        # yani ilk etapte v2' nin 0 seçilmesi yanlış, çünkü ilk değere göre direk alım-satımı başlatmış oluyor.

        for i in range(1, len(prices)):
            temp = v1
            v1 = max(v2 + prices[i] - fee, v1)
            v2 = max(temp - prices[i], v2)

        return max(v1,v2)
    
    # aşağıdaki yöntem daha kısa ve daha hızlı, bellek kullanımı daha az !!
        # sold = 0
        # held = -prices[0]

        # for price in prices:
        #     held = max(held, sold - price)
        #     sold = max(sold, held + price - fee)
        
        # return sold