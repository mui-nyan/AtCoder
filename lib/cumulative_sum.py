class CumulativeSum():
    def __init__(self, array, key=lambda a: a, operation=lambda a,b: a+b):
        n = len(array)
        self.array = [0] * (n+1)
        for i,a in enumerate(array):
            self.array[i+1] = operation(self.array[i],key(a))

    def get(self, l, r):
        """
        指定した区間の合計を計算します。
        区間は、元の配列に対する半開区間になります。
        [l:r)
        """
        return self.array[r] - self.array[l]
