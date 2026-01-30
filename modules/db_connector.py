# modules/db_connector.py
import sqlite3
import pandas as pd

class DatabaseConnector:
    def __init__(self, db_path='business_data.db'):
        """Initialise la connexion à la base de données"""
        self.conn = sqlite3.connect(db_path)
        self._create_tables()
    
    def _create_tables(self):
        """Crée les tables si elles n'existent pas"""
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY,
                date TEXT,
                product TEXT,
                quantity INTEGER,
                revenue REAL,
                category TEXT
            )
        ''')
        self.conn.commit()
    
    def get_sales_data(self, start_date=None, end_date=None):
        """Récupère les données de vente"""
        query = "SELECT product, SUM(quantity) as total_quantity, SUM(revenue) as total_revenue FROM sales"
        
        params = []
        if start_date and end_date:
            query += " WHERE date BETWEEN ? AND ?"
            params = [start_date, end_date]
        
        query += " GROUP BY product"
        
        return pd.read_sql_query(query, self.conn, params=params)
    
    def add_sale(self, date, product, quantity, revenue, category):
        """Ajoute une vente à la base"""
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO sales (date, product, quantity, revenue, category) VALUES (?, ?, ?, ?, ?)",
            (date, product, quantity, revenue, category)
        )
        self.conn.commit()
    
    def close(self):
        """Ferme la connexion"""
        self.conn.close()