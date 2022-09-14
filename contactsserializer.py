from phonebook import Contact
from abc import ABC, abstractmethod

# Абстрактный класс, описывающий сериалайзер контатов
class ContactsSerializer(ABC):

    # Абстрактный метод серализации контактов
    @abstractmethod
    def serialize(self, file_name: str, contacts: list[Contact]) -> None:
        pass

    # Абстрактный метод десерализации контактов
    @abstractmethod
    def deserialize(self) -> list[Contact]:
        pass