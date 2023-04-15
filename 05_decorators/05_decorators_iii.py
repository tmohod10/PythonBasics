from time import time


def performance(fn_name):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn_name(*args, **kwargs)
        t2 = time()
        print(f"It took {t2 - t1} time")
        return result

    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 5

    return 12


ans = long_time()
print(ans)
