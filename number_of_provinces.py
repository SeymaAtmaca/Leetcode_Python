class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)  # Toplam şehir sayısını alırız.
        visited = set()  # Ziyaret edilen şehirleri saklamak için bir küme kullanırız.
        provinces = 0  # Eyalet sayısını saklayacak değişkeni başlatırız.

        def dfs(city):
            visited.add(city)  # Şehri ziyaret edildi olarak işaretle.
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)  # Komşu şehirleri gez.

        for city in range(n):
            if city not in visited:
                provinces += 1  # Yeni bir eyalet bulduk.
                dfs(city)  # Bu eyaletin tüm şehirlerini gez.

        return provinces 