#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for

app = Flask(__name__)

#Initial seed
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
        'title': u'Infinite Wisdom',
        'description': u'Grants godlike insight.',
        'origin': u'Eastern Legend',
        'consumed': False
    }
]

#Index
@app.route('/api/v1/flasks', methods=['GET'])
def get_flasks():
    return jsonify({'flasks': [make_public_flask(flask) for flask in flasks]})

#Show
@app.route('/api/v1/flasks/<int:flask_id>', methods=['GET'])
def get_flask_by_id(flask_id):
    flask = [flask for flask in flasks if flask['id'] == flask_id]
    if len(flask) == 0:
        abort(404)
    return jsonify({'flask': flask[0]})

#Error
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

#Create
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

#Update
@app.route('/api/v1/flasks/<int:flask_id>', methods=['PUT'])
def update_flask(flask_id):
    flask = [flask for flask in flasks if flask['id'] == flask_id]
    if len(flask) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'origin' in request.json and type(request.json['origin']) is not unicode:
        abort(400)
    if 'consumed' in request.json and type(request.json['consumed']) is not bool:
        abort(400)
    flask[0]['title'] = request.json.get('title', flask[0]['title'])
    flask[0]['description'] = request.json.get('description', flask[0]['description'])
    flask[0]['origin'] = request.json.get('origin', flask[0]['origin'])
    flask[0]['consumed'] = request.json.get('consumed', flask[0]['consumed'])
    return jsonify({'flask': flask[0]})

#Delete
@app.route('/api/v1/flasks/<int:flask_id>', methods=['DELETE'])
def delete_flask(flask_id):
    flask = [flask for flask in flasks if flask['id'] == flask_id]
    if len(flask) == 0:
        abort(404)
    flasks.remove(flask[0])
    return jsonify({'result': True})

#Serializer equivalent
def make_public_flask(flask):
    new_flask = {}
    for field in flask:
        if field != 'id':
            new_flask[field] = flask[field]
    return new_flask

if __name__ == '__main__':
    app.run(debug=True)
