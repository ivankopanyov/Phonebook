from repository import Repository
from contact import Contact

# Класс, описывающий телефонный справочник
class Phonebook(Repository):

    # Список контактов телефонного справочника
    __contacts: list[Contact] = []

    # Метод, добавляющий контакт в телефонный справочник
    def add(self, contact: Contact) -> None:
        if contact in self.__contacts:
            return
        self.__contacts.append(contact)

    # Метод поиска контакта в телефонный справочник
    def find(self, pattern: str) -> list[Contact]:
        pattern = pattern.lower()
        return list(filter(lambda i: i.to_str().lower().find(pattern) != -1, self.__contacts))

    # Метод, удаляющий контакт в телефонный справочник
    def remove(self, contact: Contact) -> None:
        if not contact in self.__contacts:
            return
        self.__contacts.remove(contact)

    # Метод, возвращающий все контакты из телефонного справочника
    def get_all(self) -> list[Contact]:
        return self.__contacts.copy()