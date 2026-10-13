create venv

install requirements.txt 

dbms maria db

download maria db from https://mariadb.org/

ensure that mariadb server is running

open mariadb as root create new user and grant them privileges

Placeholders like < user > need to be replaced

```
-- Open MariaDB as root
$sudo mysql -u root -p

-- Create User
CREATE USER '<user>'@'localhost' IDENTIFIED BY '<password>';
GRANT ALL PRIVILEGES ON *.* TO '<user>'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

configure config.json with user and password just made for mariadb connection

run setupdb.py

to run app start backend App.py

start frontend in terminal first cd frontend then npm start

IMPORTANT NOTE:

If you have run setup db before 13.10.2026 please drop the current database and 
run the new setupdb for the changes in db structure to take effect.