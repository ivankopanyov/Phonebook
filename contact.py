# Класс, описывающий контакт телефонного справочника
class Contact:

    # Имя контакта
    __name: str = None

    # Фамилия контакта
    __surname: str = None

    # Телефонный номер контакта
    __phone_number: str = None

    # Адрес контакта
    __address: str = None

    # Инициализация объкта контакта
    def __init__(self, name: str, surname: str, phone_number: str, address: str) -> None:
        self.__name = name
        self.__surname = surname
        self.__phone_number = phone_number
        self.__address = address

    # Метод, возвращающий имя контакта
    def get_name(self) -> str:
        return self.__name

    # Метод, возвращающий фамилию контакта
    def get_surname(self) -> str:
        return self.__surname

    # Метод, возвращающий телефонный номер контакта
    def get_phone_number(self) -> str:
        return self.__phone_number

    # Метод, возвращающий адрес контакта
    def get_address(self) -> str:
        return self.__address

    # Метод, преобразующий контакт в строку
    def to_str(self) -> str:
        return ' '.join([self.__name, self.__surname, self.__phone_number, self.__address])