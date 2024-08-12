def prime_number(func):
    def wrapper(*args):
        mnb = func(*args)
        k = 0
        for i in range(2, mnb // 2 + 1):
            if mnb % i == 0:
                k = + 1
        if k <= 0:
            print("Простое")
            return mnb
        else:
            print("Составное")
            return mnb

    return wrapper


@prime_number
def sum_three(q, w, e):
    return q + w + e


result = sum_three(2, 3, 6)
print(result)
