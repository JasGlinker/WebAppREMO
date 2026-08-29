import mysql.connector
import json

with open('../config.json', 'r') as f:
    config = json.load(f)
    db_config = config['database']

conn = mysql.connector.connect(host=db_config['host'],
                               user=db_config['user'],
                               password=db_config['password'])
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS database")
cursor.execute("USE database")
cursor.execute("""CREATE TABLE IF NOT EXISTS categories (
    ca_id int PRIMARY KEY AUTO_INCREMENT,
    ca_name varchar(255) NOT NULL,
    color CHAR(7) DEFAULT '#555555'
    )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS activities (
    act_id int PRIMARY KEY AUTO_INCREMENT,
    act_name varchar(255) NOT NULL, 
    start_time TIME NOT NULL,
    days SET('0', '1', '2', '3', '4', '5', '6') NOT NULL,
    esc_steps TINYINT(1) DEFAULT 3,
    category int,
    CONSTRAINT fk_cat_id FOREIGN KEY (category) REFERENCES categories(ca_id) ON DELETE SET NULL  
)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS escalations (
    esc_id int PRIMARY KEY AUTO_INCREMENT,
    esc_time int NOT NULL
)""")

conn.close()
