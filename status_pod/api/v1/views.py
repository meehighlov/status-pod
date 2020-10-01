from status_pod.api.v1.blueprint import activity



@activity.route('/mock/response', methods=['POST'])
def process_message():
    return '', 200
