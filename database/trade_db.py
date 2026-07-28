import sqlite3


class TradeDatabase:

    def __init__(self, db_name="forexmind.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS trades (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            time TEXT,

            symbol TEXT,

            decision TEXT,

            entry REAL,

            stop_loss REAL,

            take_profit REAL,

            lot_size REAL,

            status TEXT

        )
        """)

        self.conn.commit()

    def save_trade(self, trade):

        self.cursor.execute("""
        INSERT INTO trades(
            time,
            symbol,
            decision,
            entry,
            stop_loss,
            take_profit,
            lot_size,
            status
        )

        VALUES (?,?,?,?,?,?,?,?)
        """, (

            trade["time"],
            trade["symbol"],
            trade["decision"],
            trade["entry"],
            trade["stop_loss"],
            trade["take_profit"],
            trade["lot_size"],
            trade["status"]

        ))

        self.conn.commit()

    def get_all_trades(self):

        self.cursor.execute("SELECT * FROM trades")

        return self.cursor.fetchall()

    def close(self):
        self.conn.close()