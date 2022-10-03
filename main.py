import time

def info(fn):
    def some_fn():
        print("тут выполняется какая-то функция")
        fn()

    return some_fn

@ info
def timer():
    start = time.time()
    print(f"Функция {info.__name__} выполнилась за {time.time() - start} секунд.")

timer()