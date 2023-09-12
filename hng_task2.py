from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import current_app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///persons.db'  # SQLite database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

@app.route('/api/person/<name>', methods=['POST'])
def create_person(name):
    try:
        new_person = Person(name=name)
        db.session.add(new_person)
        db.session.commit()
        return jsonify({'message': 'Person created successfully', 'person': new_person.to_dict()}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error', 'details': str(e)}), 500

@app.route('/api/<int:user_id>', methods=['GET'])
def get_person(user_id):
    person = Person.query.get(user_id)
    if person:
        return jsonify({'person': person.to_dict()})
    return jsonify({'error': 'Person not found'}), 404

@app.route('/api/<int:user_id>', methods=['PUT'])
def update_person(user_id):
    try:
        data = request.json
        person = Person.query.get(user_id)
        if person:
            person.name = data.get('name', person.name)
            db.session.commit()
            return jsonify({'message': 'Person updated successfully', 'person': person.to_dict()})
        return jsonify({'error': 'Person not found'}), 404
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error', 'details': str(e)}), 500

@app.route('/api/<int:user_id>', methods=['DELETE'])
def delete_person(user_id):
    try:
        person = Person.query.get(user_id)
        if person:
            db.session.delete(person)
            db.session.commit()
            return jsonify({'message': 'Person deleted successfully'})
        return jsonify({'error': 'Person not found'}), 404
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error', 'details': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0',port=5000,debug=True)
