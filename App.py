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
def get_tasks():
    return jsonify({'flasks': flasks})

if __name__ == '__main__':
    app.run(debug=True)
