from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    status = db.Column(db.String(30), default='A Fazer')
    priority = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Recurso nao encontrado"}), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Erro interno do servidor"}), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Atributo "title" é obrigatório'}), 400
    
    task = Task(
        title=data['title'], 
        status=data.get('status', 'A Fazer'),
        priority=data.get('priority', False)
    )
    db.session.add(task)
    db.session.commit()
    
    return jsonify({
        'id': task.id, 
        'title': task.title, 
        'status': task.status,
        'priority': task.priority
    }), 201

@app.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = Task.query.all()
    return jsonify([{
        'id': t.id, 
        'title': t.title, 
        'status': t.status,
        'priority': t.priority
    } for t in tasks]), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = db.session.get(Task, task_id)
    if not task:
        return jsonify({'error': 'Tarefa nao encontrada'}), 404
    
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.status = data.get('status', task.status)
    task.priority = data.get('priority', task.priority)
    db.session.commit()
    
    return jsonify({
        'id': task.id, 
        'title': task.title, 
        'status': task.status,
        'priority': task.priority
    }), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = db.session.get(Task, task_id)
    if not task:
        return jsonify({'error': 'Tarefa nao encontrada'}), 404
    
    db.session.delete(task)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)