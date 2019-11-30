"""9. n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому
школьнику? Сколько яблок останется в корзинке? Программа получает на вход числа `n` и `k` и должна вывести искомое
количество яблок (два числа)."""


"""apples"""
n = int(1)
"""child"""
k = int(3)
a = n // k


if n >= k:
    print('\nApples for each child:')
    print(a)
else:
    print('\nChild received apple(s)')
    print(n)

    print("\nChild hungry!")
    print(k - n)



print('\nApples rest:')

if a == 0:
    print('0')
else:
    print(n - a * k)






