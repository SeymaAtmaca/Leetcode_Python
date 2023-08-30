class Solution:
    def compress(self, chars: list[str]) -> int:
        iter_len = lambda xs: sum(1 for _ in xs)

        # burada her harf key olarak atanıyor,
        # daha sonra kaç adet varsa group kısmına tek tek ekleniyor
        # bu gruptaki harflerin sayımı da iter_len üzerinde yapılıyor.
        # key ler ch ye atılıyor ve bu ch adedi de iter_len aracılıpı ile alınıyor
        ch_counts = ((ch, iter_len(g)) for ch, g in groupby(chars)) 

        # burada da ch nin adedi alınıyor ve ch ile beraber string e çevrilerek compressed a atılıyor
        compressed = chain.from_iterable(ch + str(n) if n > 1 else ch for ch, n in ch_counts)

        i = 0
        for i, ch in enumerate(compressed): chars[i] = ch 
        return i + 1