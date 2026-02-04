
# شرط بازگشت و تعریف بازگشت و مقدار بازگشت
# def rec(n):
#     if rec_condition:
#         return rec_value
#     return rec_definition


def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n


# تابع بازگشتی حاصل ضرب دو عدد مثبت آ و ب را محاسبه کند
# تعریف بازگشتی: zarb(a,b) = zarb(a, b-1) + a
# شرط بازگشتی: if b == 1
# مقدار بازگشتی: (0)


def mult(a, b):
    if b == 0:
        return 0
    return mult(a, b - 1) + a


def div(a, b):
    remainder = a - b
    if remainder < b:
        return remainder
    return div(a - b, b) + 1


def div2(a, b):
    if a < b:
        return 0
    return div(a - b, b) + 1


print(div(22, 3))


# fibonacci n
# order(2**n) = O(2**n)
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


n = 6
print(f"fib {n}: ", fib(n))

# مساله اساسی توابع بازگشتی:
# برای محاسبه اوردر توابع بازگشتی باید T(n) را محاسبه کنیم
