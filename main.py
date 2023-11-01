import json

class Note:
    def __int__(self, id, title, body, date):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

class NoteManeger:
    def __int__(self, filename):
        self.filename = filename
        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                for note_data in  data:
                    note = Note(note_data['id'],note_data['title'], note_data['body'], note_data['date'])
                    self.notes.append(note)
        except FileNotFoundError:
            print("Файл не найден или не может быть открыт ")


    def save_notes(self):
        data = []
        for note in self.notes:
            note_data = {"id": note.id, 'title': note.title, 'body': note.body, 'date':note.date}
            data.append(note_data)
        with open(self.filename, 'w') as file:
            json.dump(data,file)


    def add_note(self, title,body):
        id = len(self.notes) + 1
        date = self.get_current_datatime()
        note = Note(id,title,body,date)
        self.notes.append(note)
        self.save_notes()


    def edit_note_dy_id(self,id,title,body):
        for note in self.notes:
            if note.id == id:
                note.title = title
                note.body = body
                note.date = self.get_current_datatime()
                self.save_notes()
                return
        print("Заметка с указаным ID не найдена")


    def delete_note_by_id(self,id):
        for note in self.notes:
            if note.id == id:
                self.notes.remove(note)
                self.save_notes()
                return
        print("Заметка с указаным ID не найдена")


    def get_notes(self):
        return self.notes


    @staticmethod

    def get_current_datatime():
        import datetime
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")



    def print_note_list(notes):
        if len(notes) == 0:
            print("Заметок не найдено")

        else:
            for note in notes:
                print(f"ID: {note.id}")
                print(f"Заголовок: {note.title}")
                print(f"Тело: {note.body}")
                print(f"Дата/Время: {note.date}")
                print("---------------------------")



    def start_note_app(self):
         filename = "notes.json"
         note_maneger = NoteManeger(filename)


         while True:
             print("Меню:")
             print("1. Вывести список заметок")
             print("2. Добавить заметку")
             print("3. Редактировать заметку")
             print("4. Удалить заметку")
             print("5. Выйти")

             choice = input("Введите номер операции: ")

             if choice =="1":
                 notes = note_maneger.get_notes()
                 self.print_note_list(notes)

             elif choice == "2":
                 title = input("Введите заголовок заметки: ")
                 body = input("Введите тело заметки: ")
                 note_maneger.add_note(title, body)
                 print("Заметка успешно добавлена")

             elif choice == "3":
                 id = int(input("Введите ID заметки для редактирования: "))
                 title = input("Введите новый заголовок заметки: ")
                 body = input("Введите новое тело заметки: ")
                 note_maneger.edit_note_dy_id(id, title, body)
                 print("Заметка успешно отредактирована")

             elif choice == "4":
                 id = int(input("Введите D заметки для удаления: "))
                 note_maneger.delete_note_by_id(id)
                 print("Заметка успешно удалена")

             elif choice == "5":
                 break

             else:

                 print("Неверный номер операции")


def start_note_app():
    pass


start_note_app()