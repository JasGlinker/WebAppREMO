import mysql.connector
import json

with open('../config.json', 'r') as f:
    config = json.load(f)
    db_config = config['database']

conn = mysql.connector.connect(host=db_config['host'],
                               user=db_config['user'],
                               password=db_config['password'])
cursor = conn.cursor()
# make database
cursor.execute("CREATE DATABASE IF NOT EXISTS database")
cursor.execute("USE database")
# make table for categories
cursor.execute("""CREATE TABLE IF NOT EXISTS categories (
    ca_id int PRIMARY KEY AUTO_INCREMENT,
    ca_name varchar(255) NOT NULL,
    color CHAR(7) DEFAULT '#555555'
    )""")
# make table for activities
cursor.execute("""CREATE TABLE IF NOT EXISTS activities (
    act_id int PRIMARY KEY AUTO_INCREMENT,
    act_name varchar(255) NOT NULL, 
    start_time TIME NOT NULL,
    esc_steps TINYINT(1) DEFAULT 3,
    category int,
    CONSTRAINT fk_cat_id FOREIGN KEY (category) REFERENCES categories(ca_id) ON DELETE SET NULL  
)""")
# make table for recurring days
cursor.execute("""CREATE TABLE IF NOT EXISTS days (
    act_id int NOT NULL,
    day_nmbr int NOT NULL,
    CONSTRAINT fk_act_id FOREIGN KEY (act_id) REFERENCES activities(act_id) ON DELETE CASCADE,
    PRIMARY KEY (act_id, day_nmbr))
    """
)
# make table for escalation steps
cursor.execute("""CREATE TABLE IF NOT EXISTS escalations (
    esc_id int PRIMARY KEY AUTO_INCREMENT,
    esc_time int NOT NULL
)""")


# make default categories
cursor.execute("""INSERT INTO categories (ca_name, color) 
                  VALUES ('work', '#ffb30f'), ('uni','#11d103');""")


#make default esc_times
cursor.execute("""INSERT INTO escalations (esc_time) VALUES
(30),
(50),
(60),
(70),
(80),
(90),
(100);""")
conn.commit()
conn.close()
