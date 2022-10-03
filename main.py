from datetime import datetime

def info(fn):
    def some_fn():
        print("тут выполняется какая-то функция")
        fn()

    return some_fn

@ info
def timer():
    print(f"Функция {info.__name__} выполнилась в {datetime.now()}")

timer()