from tkinter import Toplevel, ttk
from src.windows.window_for_add import WindowForAdd

class AddOrederWindow(Toplevel):
    def __init__(self):
        super().__init__()
        
        # Настройка окна
        self.title("Добавить заказ")
        self.width = 500
        self.height = 500
        self.x = int(self.winfo_screenwidth()/2 - self.width/2)
        self.y = int(self.winfo_screenheight()/2 - self.height/2)
        self.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')
        self.resizable(False, False)
        
        # Виджеты
        ttk.Label(self, text='Добавить...', font=('Arial',15)).pack(pady=(25))
        btns = [
            ttk.Button(self, text='Букет', padding=10, command=lambda: self.open_window('Букет')),
            ttk.Button(self, text='Доставку', padding=10, command=lambda: self.open_window('Доставка')),
            ttk.Button(self, text='Заказ', padding=10, command=lambda: self.open_window('Заказ')),
            ttk.Button(self, text='Курьера', padding=10, command=lambda: self.open_window('Курьер')),
            ttk.Button(self, text='Покупателя', padding=10, command=lambda: self.open_window('Покупатель')),
            ttk.Button(self, text='Цветы', padding=10, command=lambda: self.open_window('Цветок')),
        ]
        
        [btn.pack(padx=40, pady=10, fill='x') for btn in btns]
        
    def open_window(self, title):
        WindowForAdd(title)
        