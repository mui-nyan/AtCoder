class cumulative_sum():
    def __init__(self, array, key=lambda a: a):
        n = len(array)
        self.array = [0] * (n+1)
        for i,a in enumerate(array):
            self.array[i+1] = self.array[i] + key(a)

    def get(self, l, r):
        """指定した区間(半開区間)の合計を計算します。"""
        return self.array[r] - self.array[l]
