class Horse:
    x_distance = 0  # пройденный путь.
    _sound = 'Frrr'  # звук, который издаёт лошадь.

    def run(self, dx):  # изменение дистанции, увеличивает x_distance на dx.
        self.x_distance += dx


class Eagle:
    y_distance = 0  # высота полета.
    sound = 'I train, eat, sleep, and repeat'  # звук, который издаёт орёл (отсылка).

    def fly(self, dy):  # где dy - изменение дистанции, увеличивает y_distance на dy.
        self.y_distance += dy


class Pegasus(Horse, Eagle):  # класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
    #  Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.
    def __init__(self):
        self.sound = super()._sound
        self.sound = super().sound

    def move(self, dx, dy):  # где dx и dy изменения дистанции
        self.run(dx)
        self.fly(dy)

    def get_pos(self):  # возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) .
        pos_pegasus = (self.x_distance, self.y_distance)
        return pos_pegasus

    def voice(self):  # печатает значение унаследованного атрибута sound.
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
