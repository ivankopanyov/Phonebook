from datetime import datetime

# Класс, описывающий логгер
class Logger:

    # Имя файла для записи логов
    __file_name: str = None

    # Инициализация объекта логгера
    def __init__(self, file_name: str) -> None:
        self.__file_name = file_name

    # Метод записи лога в файл
    def write_log(self, message: str) -> None:
        log = f'{datetime.now():%d.%m.%Y %H:%M:%S} {message}\n'
        with open(self.__file_name, 'a', encoding='utf8') as file:
            file.write(log)