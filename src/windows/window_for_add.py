from tkinter import Toplevel, ttk
from utils.database import Database

class WindowForAdd(Toplevel):
    table_from_db = {
        'Букет': ['Букет', "Название_букета", "Цена", "Количество", "Цветок_ID"],
        'Доставка': ['Доставка', 'Курьер_ID', 'Дата_доставки', "Статус",  'Время_доставки'], 
        'Заказ': ['Заказ','Покупатель_ID', 'Доставка_ID', 'Букет_ID'],
        'Курьер': ["Курьер", 'Курьер_ID','Имя', 'Фамилия', 'Телефон', 'Тип_доставки'],
        'Покупатель': ['Покупатель','Имя',   'Фамилия', 'Телефон', 'Почта', 'Адрес'],
        'Цветок': ['Цветок','Название', 'Цена', "Наличие", 'Цвет', "Вид", "Описание"],
        
    }
    
    def __init__(self, title):
            super().__init__()
            
            # Настройка окна
            self.title(title)
            self.width = 300
            self.height = 305
            self.x = int(self.winfo_screenwidth()/2 - self.width/2)
            self.y = int(self.winfo_screenheight()/2 - self.height/2)
            self.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')
            self.resizable(False, False) 

            # Виджеты
            titles = WindowForAdd.table_from_db[title]
            fields = []
            data = {}
            for field in titles[1::]:
                ttk.Label(self, text=field).pack(fill='x', padx=(20))
                entry = ttk.Entry(self)
                entry.pack(fill='x', padx=(20))
                fields.append((field, entry))
        
            ttk.Button(self, text='Сохранить', command=lambda: self.save_to_db(titles[0], fields, data)).pack(pady=(20))
     
    # Функции       
    def save_to_db(self, table, fields, data):
                for field, entry in fields:
                    if entry.get() != '':
                        data[field] = entry.get()
            
                try:
                    Database().insert_data(table, data)
                    self.destroy()
                except:
                    self.destroy()    
                