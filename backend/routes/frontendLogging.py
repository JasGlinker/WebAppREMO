from flask import Blueprint, request, jsonify, json
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename="logging.log",
                    encoding="utf-8" ,
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

log_page = Blueprint('log_page', __name__)

@log_page.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        try:
            match request.form['type']:
                case 'info':
                    logger.info(request.form['msg'])
                case 'debug':
                    logger.debug(request.form['msg'])
                case 'warning':
                    logger.warning(request.form['msg'])
                case 'error':
                    logger.error(request.form['msg'])
                case _:
                    logger.info(request.form['msg'])
            ##log message
            ##if act save for statistics
            ##print("request form act act_id:", json.loads(request.form['act'])['act_id'])
            ## logger.info(msg=request.form['msg'])
            return jsonify({'success': True}), 200

        except Exception as e:
            logger.error(msg='failed to log activity as done')
            return jsonify({'success': False}), 500
            ## log problem

