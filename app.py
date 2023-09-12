from flask import Flask, request, jsonify
from models import APIResponse
app = Flask(__name__)
@app.route('/api', methods=['POST'])
def postRequest():
    req_data = request.get_json()
    keys = req_data.keys()
    if 'startLoc' in keys and 'endLoc' in keys and 'timestamp' in keys:
        res = APIResponse(1, [1,2,3], "k", 123123123)
        return jsonify({
            'status': 200,
            'res': res.serialize()
    })
    else: 
        return jsonify({
            'status': 400,
            'res': 'wrong request'
        })
if __name__ == '__main__':
    app.run()
