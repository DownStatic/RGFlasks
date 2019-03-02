#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

flasks = [
    {
        'id': 1,
        'title': u'Eternal Life',
        'description': u'Prevents death by natural causes and all disease',
        'origin': u'Western Philosophy',
        'consumed': False
    },
    {
        'id': 2,
        'title': u'Arcane Might',
        'description': u'Grants overflowing arcane magic for a full day.',
        'origin': u'WoW',
        'consumed': False
    }
]

@app.route('/api/v1/flasks', methods=['GET'])
def get_flasks():
    return jsonify({'flasks': flasks})

from flask import abort

@app.route('/api/v1/flasks/<int:flask_id>', methods=['GET'])
def get_flask_by_id(flask_id):
    flask = [flask for flask in flasks if flask['id'] == flask_id]
    if len(flask) == 0:
        abort(404)
    return jsonify({'flask': flask[0]})

from flask import make_response

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

from flask import request

@app.route('/api/v1/flasks', methods=['POST'])
def create_flask():
    if not request.json or not 'title' in request.json:
        abort(400)
    flask = {
        'id': flasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'origin': request.json.get('origin', ""),
        'consumed': False
    }
    flasks.append(flask)
    return jsonify({'flask': flask}), 201

if __name__ == '__main__':
    app.run(debug=True)
