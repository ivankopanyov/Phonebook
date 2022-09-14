from phonebook import Phonebook
from gui import MainWindow
from phonebookcontroller import PhonebookController
from contactsxmlserializer import ContactsXmlSerializer
from contactsjsonserializer import ContactsJsonSerializer
from logger import Logger
from traceback import format_exc

# Точка входа в приложение
def main() -> None:
    logger = Logger('phonebook.log')
    logger.write_log('Запуск приложения')
    try:
        phonebook = Phonebook()
        serializers = {
            'xml' : ContactsXmlSerializer(),
            'json' : ContactsJsonSerializer()
        }
        controller = PhonebookController(phonebook, serializers, logger)
        view = MainWindow(' Телефонный справочник ', 600, 400, controller)
        view.show()
    except Exception:
        logger.write_log(format_exc())
    logger.write_log('Выход из приложения')

if __name__ == '__main__':
    main()