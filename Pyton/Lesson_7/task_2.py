#  Реализовать проект расчета суммарного расхода ткани на производство одежды.
#  Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
#  К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
#  размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
#  для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
#  реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import abstractmethod


class Clothes:

    def __init__(self, size=0):
        self.size = size

    @abstractmethod
    def cloth_out(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        super(Coat, self).__init__(size)

    def cloth_out(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, size):
        super(Suit, self).__init__(size)

    def cloth_out(self):
        return self.size * 2 + 0.3

    @staticmethod
    def __define_size_by_value(val):
        return (val - 0.3) // 2

    @property
    def size_out(self):
        return self.size

    @size_out.setter
    def size_out(self, val):
        tmp_size = int(self.__define_size_by_value(val))
        print(f'Этого хватает на {tmp_size}-й размер.')
        if tmp_size < 1:
            print('невозможно использовать это количество ткани.')
        else:
            print('Применяем.')
            self.size = tmp_size


if __name__ == '__main__':
    c = Coat(12)
    print(c.cloth_out())

    s = Suit(12)
    print(s.cloth_out())
    print(s.size_out)
    s.size_out = 36
    print(s.cloth_out())