import os
from abc import ABC, abstractmethod

# Абстрактный класс, описывающий представление
class View(ABC):

    # Абстрактный метод ввода строки
    @abstractmethod
    def input_str(self, title: str, min_length: int = None, max_length: int = None) -> str:
        pass

    # Абстрактный метод ввода числа
    @abstractmethod
    def input_number(self, title: str, min: int = None, max: int = None) -> int:
        pass

    # Абстрактный метод вывода сообщения
    @abstractmethod
    def output_message(self, message: str) -> None:
        pass

    # Абстрактный метод вывода меню
    @abstractmethod
    def output_menu(self, items: list[str], title: str, back_name: str) -> int:
        pass

    # Абстрактный метод вывода словаря
    @abstractmethod
    def output_dict(self, items: dict[str: str]) -> None:
        pass

    # Абстрактный метод перехода на новый экран
    @abstractmethod
    def new_screen(self) -> None:
        pass

# Класс, описывающий консольное представление
class ConsoleView(View):

    # Метод ввода строки
    def input_str(self, title: str, min_length: int = None, max_length: int = None) -> str:
        while True:
            s = input(title)
            if (min_length != None and len(s) < min_length) or (max_length != None and len(s) > max_length):
                print('Нарушены границы допустимого колличества символов! Повторите попытку...')
                continue
            return s

    # Метод ввода числа
    def input_number(self, title: str, min: int = None, max: int = None) -> int:
        while True:
            num = input(title)
            try:
                num = int(num)
                if (min != None and num < min) or (max != None and num > max):
                    print('Нарушены границы допустимого диапазона! Повторите попытку...')
                    continue
            except ValueError:
                print('Некорректный ввод! Повторите попытку...')
                continue
            return num

    # Метод вывода сообщения в консоль
    def output_message(self, message: str) -> None:
        print(message)

    # Метод вывода меню в консоль
    def output_menu(self, items: list[str], title: str = '\nУкажите пункт меню: ', back_name: str = 'Назад') -> int:
        for i in range(len(items)):
            print(f'{i + 1}. {items[i]}')
        print(f'0. {back_name}')
        return self.input_number(title, 0, len(items)) - 1

    # Метод вывода словаря в консоль
    def output_dict(self, items: dict[str: str]) -> None:
        for i in items:
            print(f'{i}: {items[i]}')
            
    # Метод очистки консоли
    def new_screen(self) -> None:
        os.system('cls')
