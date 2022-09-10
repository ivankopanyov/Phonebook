from abc import ABC
from view import View
from repository import Repository
from contactsserializer import ContactsSerializer
from logger import Logger

# Абстрактный класс, описывающий контроллер для работы с репозиторием
class RepositoryController(ABC):
    
    # Модель репозитория
    _model: Repository = None

    # Объект класса представления
    _view: View = None

    # Сериалайзер модели
    _serializer: ContactsSerializer = None

    # Логгер
    _logger: Logger = None

    # Инициализация объекта контроллера
    def __init__(self, model: Repository, view: View, serializer: ContactsSerializer = None, logger: Logger = None) -> None:
        self._model = model
        self._view = view
        self._serializer = serializer
        self._logger = logger