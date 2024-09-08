class DivisionManager:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __enter__(self):
        # Возвращаем сам объект для использования его в блоке with
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print("Division completed successfully.")
        else:
            print(f"Error occurred: {exc_value}")

        # Возвращаем False, чтобы исключение не подавлялось
        #return False

    def divide(self):
        return self.numerator / self.denominator


# Пример 1: Успешное деление
with DivisionManager(10, 2) as manager:
    result = manager.divide()
    print(f"Result: {result}")

# Пример 2: Деление на ноль (исключение)
try:
    with DivisionManager(10, 0) as manager:
        result = manager.divide()
        print(f"Result: {result}")
except ZeroDivisionError as e:
    print(f"Caught exception: {e}")

