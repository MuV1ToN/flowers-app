from tkinter import Toplevel, ttk
from utils.database import Database

class WatchWindow(Toplevel):
    def __init__(self):
        super().__init__()
        
        # Настройки окна
        self.title('Посмотреть')
        self.width = 800
        self.height = 600
        self.minsize(self.width, self.height)
        self.x = int(self.winfo_screenwidth()/2 - self.width/2)
        self.y = int(self.winfo_screenheight()/2 - self.height/2)
        self.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')
        
        # Виджеты
        tab_titles = [title[0] for title in Database().get_request_data(""" SELECT name FROM sqlite_master WHERE type='table' ORDER BY name """)]
        tab_titles.remove('sqlite_sequence')
        
        notebook = ttk.Notebook(self)
        notebook.pack(expand=1, fill="both")
        
        self.trees = {}

        for tab_name in tab_titles:
            tab = ttk.Frame(notebook)
            notebook.add(tab, text=tab_name) #f'{tab_name: ^20s}'
            tree = ttk.Treeview(tab, show="headings")
            tree.pack(expand=1, fill='both')
            
            self.trees[tab_name] = tree
            
            tree['columns'], data = self.get_data(tab_name)
            [tree.heading(column, text=column) for column in tree['columns']]
            [tree.insert("", "end", values=row) for row in data]
            
        ttk.Button(self, text='Обновить', padding=5, command=lambda : self.update_all_tables()).pack(fill='x', pady=(0, 10))
        
    # Обновление всех столбцов  
    def update_all_tables(self):
        for tab_name, tree in self.trees.items():
            for child in tree.get_children():
                tree.delete(child)

            columns, data = self.get_data(tab_name)
            tree['columns'] = columns 
            for col in columns:
                tree.heading(col, text=col)

            for row in data:
                tree.insert("", "end", values=row)

    
    # получение информации для таблицы
    def get_data(self, table):
        if table == 'Букет':
            titels = Database().get_request_data("select name from pragma_table_info('Букет')")
            data = Database().get_request_data("select * from Букет")
            return titels, data
        
        elif table == 'Курьер':
            titels = Database().get_request_data("select name from pragma_table_info('Курьер')")
            data = Database().get_request_data("select * from Курьер")
            return titels, data
        
        elif table == 'Покупатель':
            titels = Database().get_request_data("select name from pragma_table_info('Покупатель')")
            data = Database().get_request_data("select * from Покупатель")
            return titels, data
        
        elif table == 'Доставка':
            titels = Database().get_request_data("select name from pragma_table_info('Доставка')")
            data = Database().get_request_data("""
                                                select
                                                    Доставка_ID,
                                                    concat('id: ',Курьер.Курьер_ID, ' Имя: ',Курьер.Фамилия,' ', Курьер.Имя) as 'Курьер_ID',
                                                    Дата_доставки,
                                                    Статус,
                                                    Время_доставки
                                                from Доставка
                                                left join Курьер on Доставка.Доставка_ID = Курьер.Курьер_ID
                                               """)
            return titels, data
        
        elif table == 'Цветок':
            titels = Database().get_request_data("select name from pragma_table_info('Цветок')")
            data = Database().get_request_data("select * from Цветок")
            return titels, data
        
        elif table == 'Заказ':
            titels = Database().get_request_data("select name from pragma_table_info('Заказ')")
            data = Database().get_request_data("""
                                                SELECT
                                                    Заказ_ID,
                                                    concat('Имя:', Покупатель.Фамилия,' ', Покупатель.Имя,' Адрес: ',Покупатель.Адрес,' Телефон:',Покупатель.Телефон) as Покупатель,
                                                    concat('Дата доставки: ', Доставка.Дата_доставки,' в ',Доставка.Время_доставки) as Доставка,
                                                    concat('Букет: ', Букет.Название_букета, 'Цена: ', Букет.Цена) as Букет
                                                FROM Заказ
                                                LEFT JOIN Покупатель ON Заказ.Доставка_ID = Покупатель.Покупатель_ID
                                                LEFT JOIN Доставка ON Заказ.Доставка_ID = Доставка.Доставка_ID
                                                LEFT JOIN Букет ON Заказ.Букет_ID = Букет.Букет_ID
                                               """)
            return titels, data
        
        else:
            return [], []