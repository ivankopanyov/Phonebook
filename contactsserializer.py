from contact import Contact
from abc import ABC, abstractmethod

# Абстрактный класс, описывающий сериалайзер контатов
class ContactsSerializer(ABC):

    # Имя файла для чтения и записи
    _file_name: str = None

    # Инициализация объекта сериалайзера
    def __init__(self, file_name: str) -> None:
        self._file_name = file_name

    # Абстрактный метод серализации контактов
    @abstractmethod
    def serialize(self, contacts: list[Contact]) -> None:
        pass

    # Абстрактный метод десерализации контактов
    @abstractmethod
    def deserialize(self) -> list[Contact]:
        pass