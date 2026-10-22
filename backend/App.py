from flask import Flask
from routes.createActivity import create_page
from routes.dataAccess import data_page
from routes.dayView import day_page
from routes.weekView import week_page
from routes.monthView import month_page
from routes.frontendLogging import log_page
import logging
# Initializing logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename="logging.log",
                    encoding="utf-8" ,
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')



# Initializing flask app
app = Flask(__name__)
app.register_blueprint(create_page)
app.register_blueprint(data_page)
app.register_blueprint(day_page)
app.register_blueprint(week_page)
app.register_blueprint(month_page)
app.register_blueprint(log_page)

# Running app
if __name__ == '__main__':
    logger.info('logger started')
    app.run(debug=True)
