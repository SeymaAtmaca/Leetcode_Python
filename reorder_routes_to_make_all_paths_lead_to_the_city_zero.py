from collections import defaultdict, deque

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        connections_dict = defaultdict(list)
        for u, v in connections:
            connections_dict[u].append((v, 1))  # Doğru yönde bir yol ekler.
            connections_dict[v].append((u, 0))  # Ters yönde bir yol ekler.

        visited = set()  # Ziyaret edilen şehirleri saklamak için bir küme kullanırız.
        change_count = 0  # Yolu değiştirmemiz gereken yolların sayısını tutarız.

        # BFS kullanarak şehir 0'a giden yolları takip ederiz.
        queue = deque([(0, -1)])  # (Şehir, Önceki Şehir)
        while queue:
            city, prev_city = queue.popleft()
            visited.add(city)
            for neighbor, direction in connections_dict[city]:
                if neighbor not in visited:
                    if direction == 1:  # Doğru yönde yol ise değiştirmemiz gerekir.
                        change_count += 1
                    queue.append((neighbor, city))

        return change_count