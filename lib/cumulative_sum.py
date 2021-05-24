class CumulativeSum():
    def __init__(self, array, key=lambda a: a, operation=lambda a,b: a+b):
        n = len(array)
        self.array = [0] * (n+1)
        for i,a in enumerate(array):
            self.array[i+1] = operation(self.array[i],key(a))

    def get(self, l, r):
        """指定した区間(半開区間)の合計を計算します。"""
        return self.array[r] - self.array[l]
