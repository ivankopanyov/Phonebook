from os.path import exists
from tkinter import *
from tkinter import filedialog, simpledialog, messagebox
from phonebookcontroller import PhonebookController, Contact
from functools import partial

# Класс, описывающий кастомное диалоговое окно
class _Dialog(simpledialog.Dialog):

    # Словарь названий полей ввода и их дефолтных значений
    __questions: dict[str : str]

    # Список полей вввода
    __entries: list[Entry]

    # Список введенных значений из полей ввода
    __result: list[str] = None

    # Инициализация объекта диалогового окна
    def __init__(self, questions: dict[str : str], parent: Misc | None, title: str | None = ...) -> None:
        self.__questions = questions
        self.__entries = []
        super().__init__(parent, title)

    # Переопределение метода построения диалогового окна
    def body(self, master: Frame) -> Misc | None:

        row = 0
        for key in self.__questions:
            Label(master, text=key).grid(row=row, sticky=W, pady=MainWindow.PADDING)
            entry = Entry(master, width=50)
            entry.insert(END, self.__questions[key])
            entry.grid(column=1, row=row)
            self.__entries.append(entry)
            row += 1

        return super().body(master)

    def ok(self, event=None) -> None:
        self.__result = list(map(lambda i: i.get(), self.__entries))
        super().ok(event)
    
    def apply(self) -> list[str] | None:
        return self.__result

# Класс, описывающий главное окно приложения
class MainWindow:

    # Значение дефолтного отступа
    PADDING = 5

    # Объект контроллера телефонного справочника
    __phonebookController: PhonebookController

    # Объект окна приложения
    __window: Tk

    # Объект фрейма списка контактов
    __content_frame: Frame

    # Паттерно для поиска контакта
    __pattern: StringVar

    # Инициализация главного окна приложения
    def __init__(self, name: str, width: int, height: int, phonebookController: PhonebookController) -> None:

        self.__phonebookController = phonebookController
        self.__window = Tk()
        self.__window.title(name)
        self.__window.geometry(f'{width}x{height}')

    # Метод отображения главного окна приложения
    def show(self) -> None:

        frame = Frame(self.__window)
        frame.pack(fill=X, side=TOP)

        Label(frame, text='Поиск:').pack(side=LEFT, padx=self.PADDING, pady=self.PADDING)

        self.__pattern = StringVar()
        self.__pattern.trace("w", lambda name, index, mode, pattern=self.__pattern: self.__find_contact())
        Entry(frame, textvariable=self.__pattern).pack(fill=X, expand=True, side=LEFT, pady=self.PADDING)

        Frame(frame, width=self.PADDING * 4).pack(side=LEFT)
        Button(frame, text='Создать контакт', command=self.__add_contact).pack(side=LEFT, padx=self.PADDING, pady=self.PADDING)
        Button(frame, text='Импорт', command=self.__import_contacts).pack(side=LEFT, pady=self.PADDING)
        Button(frame, text='Экспорт', command=self.__export_contacts).pack(side=LEFT, padx=self.PADDING, pady=self.PADDING)

        container = Frame(self.__window, relief = RAISED, borderwidth = 1)
        container.pack(fill=BOTH, expand=True, side=TOP)

        canvas = Canvas(container)
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        self.__content_frame = Frame(canvas)
        self.__content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.__content_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.__show_contacts(self.__phonebookController.get_all_contacts())

        self.__window.mainloop()

    # Метод  вывода списка контактов
    def __show_contacts(self, contacts: list[Contact]) -> None:
        
        for widget in self.__content_frame.winfo_children():
            widget.destroy()

        Label(self.__content_frame, text='#').grid(column=0, row=0)
        Button(self.__content_frame, text='Имя', borderwidth=0, command=partial(self.__sort, PhonebookController.NAME)).grid(column=1, row=0)
        Button(self.__content_frame, text='Фамилия', borderwidth=0, command=partial(self.__sort, PhonebookController.SURNAME)).grid(column=2, row=0)
        Button(self.__content_frame, text='Номер телефона', borderwidth=0, command=partial(self.__sort, PhonebookController.PHONE_NUMBER)).grid(column=3, row=0)
            
        for i in range(len(contacts)):
            Label(self.__content_frame, text=f'{i + 1}.').grid(row=i + 1, sticky=E)
            Label(self.__content_frame, text=contacts[i].get_name()).grid(column=1, row=i + 1, sticky=W)
            Label(self.__content_frame, text=contacts[i].get_surname()).grid(column=2, row=i + 1, sticky=W)
            Label(self.__content_frame, text=contacts[i].get_phone_number()).grid(column=3, row=i + 1, sticky=W)
            Button(self.__content_frame, text='Инфо', command=partial(self.__change_contact, contacts[i])).grid(column=4, row=i + 1)
            Button(self.__content_frame, text='Удалить', command=partial(self.__remove_contact, contacts[i])).grid(column=5, row=i + 1)

    # Метод вывода диалогового окна для создания нового контакта
    def __add_contact(self) -> None:
        result = _Dialog({
            'Имя:' : '',
            'Фамилия:' : '',
            'Hомер телефона:' : '',
            'E-mail:' : '',
            'Адрес:' : ''
            }, self.__window, 'Создать контакт').apply()
        
        if result != None:
            contact = Contact(*result)
            self.__phonebookController.add_contact(contact)

        self.__find_contact()
    
    # Метод вывода диалогового окна для импортирования контактов из файла
    def __import_contacts(self) -> None:
        file_name = filedialog.askopenfilename(filetypes=[("Data files", "*.xml *.json")])

        if file_name == '':
            return

        if not exists(file_name):
            messagebox.showerror(title="Ошибка", message="Файл не найден!")
            return

        answer = False

        if (len(self.__phonebookController.get_all_contacts()) > 0):
            answer = messagebox.askyesno("", f"Удалить имеющиеся контакты?")

        result = self.__phonebookController.import_contacts(file_name)

        if len(result) == 0:
            messagebox.showwarning(title="", message="Список контатков не найден!")
        
        if answer:
            for contact in self.__phonebookController.get_all_contacts():
                self.__phonebookController.remove_contact(contact)

        for contact in result:
                self.__phonebookController.add_contact(contact)
        
        self.__find_contact()

    # Метод вывода диалогового окна для экспортирования контактов в файл
    def __export_contacts(self) -> None:
        filetypes = [("XML file", "*.xml"), ("JSON file", "*.json")]
        file_name = filedialog.asksaveasfilename(defaultextension=filetypes[0], filetypes=filetypes, initialfile="contacts")
        
        if file_name == '':
            return

        if self.__phonebookController.export_contacts(file_name):
            messagebox.showinfo(message="Список контактов успешно сохранен!")
        else:
            messagebox.showerror(title="Ошибка", message="Не удалось сохранить список контактов!")

    # Метод вывода диалогового окна для изменения контакта
    def __change_contact(self, contact: Contact) -> None:
        result = _Dialog({
            'Имя:' : contact.get_name(), 
            'Фамилия:' : contact.get_surname(),
            'Hомер телефона:' : contact.get_phone_number(),
            'E-mail': contact.get_email(),
            'Адрес:' : contact.get_address()
            }, self.__window, 'Инфо').apply()
        
        if result != None:
            self.__phonebookController.change_contact(contact, *result)
            self.__find_contact()

    # Метод вывода диалогового окна для удаления контакта
    def __remove_contact(self, contact: Contact) -> None:
        result = messagebox.askokcancel("Удалить контакт", \
            f"Вы уверены, что хотите удалить контакт {contact.get_name()} {contact.get_surname()}?")
        if result:
            self.__phonebookController.remove_contact(contact)
            self.__find_contact()

    # Метод поиска контакта
    def __find_contact(self) -> None:
        pattern = self.__pattern.get()
        self.__show_contacts(self.__phonebookController.get_all_contacts() if len(pattern) == 0 else self.__phonebookController.find_contact(pattern))

    # Метод сортировки контактов
    def __sort(self, sort_name: str) -> None:
        self.__phonebookController.set_sort(sort_name)
        self.__find_contact()