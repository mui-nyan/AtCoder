def find_divisors(n, need_sort=True, reverse=False):
    """
    nの約数を列挙します。
    """
    a = [1]
    if n != 1:
        a.append(n)
    f = 2
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            if f != n//f:
                a.append(n//f)
        f += 1

    if need_sort:
        a.sort(reverse=reverse)

    return a

def generate_divisors_from_prime_factors(prime_factors, need_sort=True, reverse=False):
    """
    素因数分解から約数リストを生成します。(1とその数自身を含む)

    Parameters
    ---
    prime_factors
        素因数分解を表現した、タプルのリスト。
        p1^a1 * p2^a2 であれば、 [(p1,a1),(p2,a2)] 。
    need_sort
        Trueの場合、約数リストをソートして返します。
    """
    # 既知の約数リスト
    div = [1]
    for p,a in prime_factors:
        # 既知の約数それぞれに対して、
        # p^1倍, p^2倍, ... p^a倍 したものを計算して約数リストに追加する
        m = len(div)
        for i in range(m):
            for j in range(1, a+1):
                div.append(div[i] * p**j)
    if need_sort:
        div.sort(reverse=reverse)
    return div
