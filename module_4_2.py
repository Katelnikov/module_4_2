# Создайте новую функцию test_function
# Создайте внутри test_function другую функцию - inner_function, Эта функция должна печатать значение "Я в области видимости функции test_function"
def test_function():


    def inner_function():
        name = 'Я в области видимости функции test_function'
        print(name)

    inner_function()

test_function()