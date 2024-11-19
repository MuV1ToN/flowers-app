import sqlite3 as sq

class Database:
    # Singletone
    __instance = None
    def __new__(cls, *args, **kwgs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    # Конструктор
    def __init__(self):
        self.connection = sq.connect('flowers.db')
        # self.connection.execute('PRAGMA foreign_keys = ON;')
        self.cursor = self.connection.cursor()
        
    # Получить данные 
    def get_request_data(self, request: str) -> list:
        self.cursor.execute(request)
        data = self.cursor.fetchall()
        return data
    
    # Сохранить данные
    def insert_data(self, table: str, data: dict) -> None:
        columns = ', '.join(f'"{key}"' for key in data.keys())
        placeholders = ', '.join(['?'] * len(data))
        values = tuple(data.values())
        query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
        self.cursor.execute(query, values)
        self.connection.commit()
            
     # Деструктор
    def __del__(self):
        self.connection.close()