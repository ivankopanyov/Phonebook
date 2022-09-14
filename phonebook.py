# Класс, описывающий контакт телефонного справочника
from operator import contains

#Класс, описывающий контакт
class Contact:

    # Имя контакта
    __name: str

    # Фамилия контакта
    __surname: str

    # Телефонный номер контакта
    __phone_number: str

    # Эмейл контакта
    __email: str

    # Адрес контакта
    __address: str

    # Инициализация объкта контакта
    def __init__(self, name: str, surname: str, phone_number: str, email: str, address: str) -> None:
        self.__name = name
        self.__surname = surname
        self.__phone_number = phone_number
        self.__email = email
        self.__address = address

    # Метод, возвращающий имя контакта
    def get_name(self) -> str:
        return self.__name

    def _set_name(self, value: str) -> None:
        self.__name = value

    # Метод, возвращающий фамилию контакта
    def get_surname(self) -> str:
        return self.__surname

    def _set_surname(self, value: str) -> None:
        self.__surname = value

    # Метод, возвращающий телефонный номер контакта
    def get_phone_number(self) -> str:
        return self.__phone_number

    def _set_phone_number(self, value: str) -> None:
        self.__phone_number = value

    # Метод, возвращающий эмейл контакта
    def get_email(self) -> str:
        return self.__email

    def _set_email(self, value: str) -> None:
        self.__email = value

    # Метод, возвращающий адрес контакта
    def get_address(self) -> str:
        return self.__address

    def _set_address(self, value: str) -> None:
        self.__address = value

    # Метод, преобразующий контакт в строку
    def to_str(self) -> str:
        return ' '.join([self.__name, self.__surname, self.__phone_number, self.__email, self.__address])

# Класс, описывающий телефонный справочник
class Phonebook:

    # Список контактов телефонного справочника
    __contacts: list[Contact] = []

    # Метод, добавляющий контакт в телефонный справочник
    def add(self, contact: Contact) -> None:
        if contact in self.__contacts:
            return
        self.__contacts.append(contact)

    # Метод, удаляющий контакт в телефонный справочник
    def remove(self, contact: Contact) -> None:
        if not contact in self.__contacts:
            return
        self.__contacts.remove(contact)

    # Метод, изменяющий информацию о контакте
    def change_contact(self, contact: Contact, name: str | None = None, surname: str | None = None, \
        phone_number: str | None = None, email: str | None = None, address: str | None = None) -> None:

        if name != None: contact._set_name(name)
        if surname != None: contact._set_surname(surname)
        if phone_number != None: contact._set_phone_number(phone_number)
        if email != None: contact._set_email(email)
        if address != None: contact._set_address(address)

    # Метод, возвращающий все контакты из телефонного справочника
    def get_all(self) -> list[Contact]:
        contacts = self.__contacts.copy()
        contacts.sort(key=lambda contact: contact.get_surname())
        return contacts