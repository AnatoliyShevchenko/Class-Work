from datetime import datetime, timedelta

def info(fn):
    def some_fn():
        print("тут выполняется какая-то функция")
        fn()

    return some_fn

@ info
def timer():
    print(f"Функция {info.__name__} выполнилась за {timedelta()}")

timer()