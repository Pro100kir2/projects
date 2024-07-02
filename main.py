from typing import List, Tuple
import random

class BoardOutException(Exception):
    pass


class Dot:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Dot):
            return self.x == other.x and self.y == other.y
        return False


class Ship:
    def __init__(self, length: int, position: Tuple[int, int], direction: str):
        self.length = length
        self.position = position
        self.direction = direction
        self.life = length

    def dots(self):
        if self.direction == 'v':
            return [Dot(self.position[0] + i, self.position[1]) for i in range(self.length)]
        else:
            return [Dot(self.position[0], self.position[1] + i) for i in range(self.length)]


class Board:
    def __init__(self, size=6):
        self.size = size
        self.field = [['O' for _ in range(size)] for _ in range(size)]
        self.ships = []
        self.hid = False
        self.alive_ships = len(self.ships)

    def add_ship(self, ship):
        if not any(dot.x >= ship.position[0] or dot.x < ship.position[0] - ship.length or dot.y >= ship.position[
            1] or dot.y < ship.position[1] - ship.length for dot in self.ships):
            self.ships.append(ship)
            self.alive_ships += 1
            for dot in ship.dots():
                self.field[dot.x][dot.y] = '■' if self.hid else 'X'

    def contour(self, ship):
        for dot in ship.dots():
            if self.field[dot.x][dot.y] == 'O':
                self.field[dot.x][dot.y] = 'T'

    def display(self):
        for row in self.field:
            print(' '.join(row))

    def out(self, dot):
        return dot.x < 0 or dot.x >= self.size or dot.y < 0 or dot.y >= self.size


    @staticmethod
    def shot(dot):
        if dot.x < 0 or dot.x >= Board.size or dot.y < 0 or dot.y >= Board.size:
            raise BoardOutException("Выстрел за пределами поля")
        if Board.field[dot.x][dot.y] == 'X':
            raise BoardOutException("Выстрел по подбитому кораблю")
        if Board.field[dot.x][dot.y] == 'T':
            raise BoardOutException("Выстрел по промаху")
        if Board.field[dot.x][dot.y] == '■':
            Board.field[dot.x][dot.y] = 'X'
            Board.alive_ships -= 1
            return True
        return False

class Player:
    def init(self, board):
        self.board = board
        self.enemy_board = None


def ask(self):
    raise NotImplementedError("Метод ask должен быть реализован в потомках")

def move(self):
    dot = self.ask()
    if self.board.shot(dot):
        return True
    return False
class AI(Player):
    def ask(self):
        while True:
            dot = Dot(random.randint(0, self.board.size - 1), random.randint(0, self.board.size - 1))
            if not self.board.shot(dot):
                return dot

class User(Player):
    def ask(self):
        while True:
            try:
                dot_x = int(input("Введите координату X: "))
                dot_y = int(input("Введите координату Y: "))
                return Dot(dot_x, dot_y)
            except ValueError:
                print("Некорректный ввод. Попробуйте снова.")

class Game:
    def init(self):
        self.board_size = 6
        self.user_board = Board(self.board_size)
        self.ai_board = Board(self.board_size)
        self.user = User(self.user_board)
        self.ai = AI(self.ai_board)


def greet(self):
    print("Добро пожаловать в игру морской бой!")
    print("Введите координаты точки для выстрела (например, A1):")

def loop(self):
    while self.user_board.alive_ships > 0 and self.ai_board.alive_ships > 0:
        if self.user.move():
            print("Вы попали в корабль!")
        else:
            print("Вы промахнулись.")
        if self.ai.move():
            print("Компьютер попал в корабль!")
        else:
            print("Компьютер промахнулся.")
    if self.user_board.alive_ships == 0:
        print("Победил компьютер!")
    else:
        print("Победил игрок!")

def start(self):
    self.greet()
    self.loop()
if __name__ == "main":
    game = Game()
    game.start()