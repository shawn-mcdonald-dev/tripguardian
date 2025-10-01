import psycopg2
import csv
import os

# Database connection settings
DB_NAME = os.getenv("POSTGRES_DB", "tripguardian")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")

DATA_DIR = "./data/openflights"

def connect():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

def load_airports(conn):
    with conn.cursor() as cur, open(os.path.join(DATA_DIR, "airports.dat"), encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("""
                INSERT INTO airports (id, name, city, country, iata, icao, latitude, longitude, altitude, timezone, dst, tz_database)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                ON CONFLICT (id) DO NOTHING
            """, row)
    conn.commit()
    print("Loaded airports")

def load_airlines(conn):
    with conn.cursor() as cur, open(os.path.join(DATA_DIR, "airlines.dat"), encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("""
                INSERT INTO airlines (id, name, alias, iata, icao, callsign, country, active)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                ON CONFLICT (id) DO NOTHING
            """, row)
    conn.commit()
    print("Loaded airlines")

def load_routes(conn):
    with conn.cursor() as cur, open(os.path.join(DATA_DIR, "routes.dat"), encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("""
                INSERT INTO routes (airline, airline_id, source_airport, source_airport_id, dest_airport, dest_airport_id, codeshare, stops, equipment)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, row)
    conn.commit()
    print("Loaded routes")

if __name__ == "__main__":
    conn = connect()
    load_airports(conn)
    load_airlines(conn)
    load_routes(conn)
    conn.close()
    print("✅ All data loaded into Postgres")
