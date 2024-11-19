from tkinter import Tk, ttk
from src.windows.add_order_menu import AddOrederWindow
from src.windows.watch_window import WatchWindow

class MenuWindow(Tk):
    def __init__(self):
        super().__init__()
        
        # Настройка онка
        self.title("Главное Меню")
        self.width = 300
        self.height = 300
        self.x = int(self.winfo_screenwidth()/2 - self.width/2)
        self.y = int(self.winfo_screenheight()/2 - self.height/2)
        self.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')
        self.resizable(False, False)
        
        # Виджеты
        ttk.Label(self, text='Магазин цветов «АртЦветы»', font=('Arial',15)).pack(pady=(25))
        btns = [
            ttk.Button(self, text='Посмотреть', padding=10, command=lambda: self.check_order()),
            ttk.Button(self, text='Добавить', padding=10, command=lambda: self.add_order()),
            ttk.Button(self, text='Выйти', padding=10, command=lambda: self.exit()),
        ]
        [btn.pack(padx=40, pady=10, fill='x') for btn in btns]
        
        self.mainloop()
    
    # Методы (функции)
    
    # Посмотреть заказ
    def check_order(self):
        WatchWindow()
    
    # Добавить заказ
    def add_order(self):
        AddOrederWindow()
    
    # Выход
    def exit(self):
        self.quit()
        self.destroy()
        