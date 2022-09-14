from phonebook import Contact
from contactsserializer import ContactsSerializer

# Класс, описывающий объект сериализатора контактов в формате xml
class ContactsXmlSerializer(ContactsSerializer):

    # Метод сериализации контактов в xml
    def serialize(self, file_name: str, contacts_list: list[Contact]) -> None:

        with open(file_name, 'w') as file:
            file.write('')

        with open(file_name, 'a', encoding='utf8') as file:

            file.write(f'<?xml version="1.0"?>\n<Phonebook>\n')

            for contact in contacts_list:
                data = f'''    <Contact>
        <name>{contact.get_name()}</name>
        <surname>{contact.get_surname()}</surname>
        <phone_number>{contact.get_phone_number()}</phone_number>
        <email>{contact.get_email()}</email>
        <address>{contact.get_address()}</address>
    </Contact>\n'''
                file.write(data)
        
            file.write(f'</Phonebook>')

    # Метод десериализации контактов из xml
    def deserialize(self, file_name: str) -> list[Contact]:
        
        is_write = False
        contacts = []
        name, surname, phone_number, email, address = None, None, None, None, None
        with open(file_name, 'r', encoding='utf8') as file:
            for line in file:
                if line.find(f'    </Contact>') == 0:
                    is_write = False
                    if name == None or surname == None or phone_number == None or email == None or address == None:
                        continue
                    contact = Contact(name, surname, phone_number, email, address)
                    contacts.append(contact)
                if is_write:
                    if line.find('        <name>') == 0:
                        name = line.replace('<name>', '').replace('</name>', '').strip()
                    if line.find('        <surname>') == 0:
                        surname = line.replace('<surname>', '').replace('</surname>', '').strip()
                    if line.find('        <phone_number>') == 0:
                        phone_number = line.replace('<phone_number>', '').replace('</phone_number>', '').strip()
                    if line.find('        <email>') == 0:
                        email = line.replace('<email>', '').replace('</email>', '').strip()
                    if line.find('        <address>') == 0:
                        address = line.replace('<address>', '').replace('</address>', '').strip()
                if line.find(f'    <Contact>') == 0:
                    name, surname, phone_number, email, address = None, None, None, None, None
                    is_write = True
        return contacts
