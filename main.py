import operator

class Avtopark():
    def __init__(self, model, price, raskhod_topliva, max_speed):
        self.model = model
        self.price = price
        self.raskhod_topliva = raskhod_topliva
        self.max_speed = max_speed

    def show(self):
        print('Модель: {}'
              ' Цена: {}'
              ' Расход топлива: {}'
              ' Максимальная скорость: {}'.format(self.model, self.price, self.raskhod_topliva, self.max_speed))


def sort_choice(Data, choice):
    result = sorted(Data, key=operator.attrgetter(choice))
    for i in result:
        i.show()


class Avto(Avtopark):

    def __init__(self, model, price, raskhod_topliva, max_speed):
        super().__init__(model, price, raskhod_topliva, max_speed)


car1 = Avto('mercedes', 20000000, 3.5, 325)
car2 = Avto('bmw', 19500000, 3.0, 320)
car3 = Avto('audi', 15000000, 2.5, 300)

e = [car1, car2, car3]

while True:

    print('1. Подсчитать стоимость автопарка')
    print('2. Провести сортировку автомобилей парка по расходу топлива')
    print('3. Найти автомобиль в компании, соответствующий заданному диапазону параметров скорости')
    print('4. exit')

    n = int(input())

    if n == 1:
        sum = 0
        for i in range(len(e)):
            sum += e[i].price
        print('Общая сумма автопарка', sum)

    if n == 2:
        sort_choice(e, 'raskhod_topliva')

    if n == 3:
        diapozon1 = int(input())
        diapozon2 = int(input())
        for i in e:
            if i.max_speed <= diapozon2 and i.max_speed >= diapozon1:
                i.show()

    if n == 4:
        break