from flask import Blueprint


activity = Blueprint('main', __name__, url_prefix='/main')


@activity.route('/mock', methods=['GET'])
def process_message():
    print('hui')
    return '', 200
