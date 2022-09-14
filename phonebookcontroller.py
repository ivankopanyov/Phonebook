from phonebook import Phonebook, Contact
from contactsserializer import ContactsSerializer
from logger import Logger
from traceback import format_exc

# Класс, описывающий контроллер для работы с телефонным справочником
class PhonebookController:

    # Константы для сортировки списка контактов
    NAME = 'name'
    SURNAME = 'surname'
    PHONE_NUMBER = 'phone_number'
    
    # Модель телефонного справочника
    __phonebook: Phonebook

    # Сериалайзеры телефонного справочника
    __serializers: dict[str : ContactsSerializer]

    # Логгер
    __logger: Logger

    # Текущее значение сортировки контактов
    __sort: str = SURNAME

    # Реверсивная сортировка
    __reversed: bool = False

    # Инициализация объекта контроллера
    def __init__(self, phonebook: Phonebook, serializers: dict[str : ContactsSerializer] = [], logger: Logger = None) -> None:

        self.__phonebook = phonebook
        self.__serializers = serializers
        self.__logger = logger

    # Метод получения списка всех контактов из телефонного справочника
    def get_all_contacts(self) -> list[Contact]:
        return self._sort(self.__phonebook.get_all())

    # Метод добавления контакта в телефонный справочник
    def add_contact(self, contact: Contact) -> None:
        self.__phonebook.add(contact)
        if self.__logger != None:
            self.__logger.write_log(f'Добавлен контакт {contact.to_str()}')

    # Метод изменения информации о контакте
    def change_contact(self, contact: Contact, name: str, surname: str, phone_number: str, email: str, address: str) -> None:
        before = contact.to_str()
        self.__phonebook.change_contact(contact, name, surname, phone_number, email, address)
        if self.__logger != None:
            self.__logger.write_log(f'Контакт {before} изменен на {contact.to_str()}')

    # Метод удаления контакта
    def remove_contact(self, contact: Contact) -> None:
        self.__phonebook.remove(contact)
        if self.__logger != None:
            self.__logger.write_log(f'Удален контакт {contact.to_str()}')

    # Метод поиска контакта
    def find_contact(self, pattern: str) -> list[Contact]:
        pattern = pattern.lower()
        contacts = list(filter(lambda i: i.to_str().lower().find(pattern) != -1, self.__phonebook.get_all()))
        return self._sort(contacts)

    # Метод экспорта списка контактов в файл
    def export_contacts(self, file_name: str) -> bool:
        extension = file_name.split('.')[-1]
        for serializer in self.__serializers:
            if serializer == extension:
                try:
                    self.__serializers[serializer].serialize(file_name, self.__phonebook.get_all())
                    if self.__logger != None:
                        self.__logger.write_log(f'Список контактов сохранен в файл {file_name}')
                    return True
                except Exception:
                    if self.__logger != None:
                        self.__logger.write_log(format_exc())
                    continue
        return False

    # Метод импорта списка контактов из файла
    def import_contacts(self, file_name: str) -> list[Contact]:
        extension = file_name.split('.')[-1]
        for serializer in self.__serializers:
            if serializer == extension:
                try:
                    result = self.__serializers[serializer].deserialize(file_name)
                    if len(result) == 0:
                        return []
                    if self.__logger != None:
                        self.__logger.write_log(f'Список контактов загружен из файла {file_name}')
                    return result
                except Exception as e:
                    if self.__logger != None:
                        self.__logger.write_log(format_exc())
                    continue
        return []

    # Метод изменения сортировки контактов
    def set_sort(self, sort_name: str) -> None:
        self.__reversed = not self.__reversed if sort_name == self.__sort else False
        self.__sort = sort_name

    # Метод сортировки контактов
    def _sort(self, contacts: list[Contact]) -> list[Contact]:
        if self.__sort == self.NAME:
            contacts.sort(key=lambda contact: contact.get_name())
        elif self.__sort == self.PHONE_NUMBER:
            contacts.sort(key=lambda contact: contact.get_phone_number())
        else:
            contacts.sort(key=lambda contact: contact.get_surname())

        return contacts if not self.__reversed else list(reversed(contacts))