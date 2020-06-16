from flask import Flask, request, jsonify
from datalayer import ALL_scores, UID_scores
import os

app = Flask(__name__)

@app.route('/uid_scores', methods=['POST'])
def uid_averager():
    '''Takes a POST request with a payload in the format {"uid": $string,"points":$integer} and returns an average for given uid'''
    try:
        payload = request.get_json(force=True)
        if 'uid' in payload and 'points' in payload:
            uid_instance = UID_scores(payload['uid'], os.environ.get('JSON_FILE_LOCATION', 'scores.json'))
            uid_instance.append(payload['points'])
            uid_instance.write()
            return jsonify({"average":uid_instance.avg()})
        else:
            return jsonify({'error' : "Data retrieved not processable. API expects this syntax: {\"uid\": $string,\"points\":$integer}"}), 400
    except Exception as e:
        return jsonify({'error' : e}), 400


@app.route('/group_averager', methods=['GET'])
def group_averager():
    try:
        return jsonify({"group_average" : ALL_scores(os.environ.get('JSON_FILE_LOCATION', 'scores.json')).avg()})
    except Exception as e:
        return jsonify({'error' : e}), 400

if __name__ == '__main__':
    app.run(use_evalex=False,host='0.0.0.0', port=5000)