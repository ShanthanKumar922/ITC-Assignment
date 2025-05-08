import psycopg2

def get_conn():
    return psycopg2.connect(
        dbname="itc_fin",
        user="postgres",          
        password="123456",   
        host="localhost",
        port="5432"
    )

def create_tables():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS stock_prices (
            date DATE PRIMARY KEY,
            open FLOAT,
            high FLOAT,
            low FLOAT,
            close FLOAT,
            volume BIGINT
        );
    """)

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_tables()