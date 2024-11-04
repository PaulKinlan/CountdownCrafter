import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "a secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

db.init_app(app)

with app.app_context():
    import models
    db.drop_all()
    db.create_all()

@app.route('/')
def create():
    return render_template('create.html')

@app.route('/timer', methods=['POST'])
def create_timer():
    event_name = request.form['event_name']
    end_date = datetime.fromisoformat(request.form['end_date'].replace('Z', '+00:00'))
    theme = request.form.get('theme', 'default')
    layout = request.form.get('layout', 'standard')
    
    timer = models.Timer(
        event_name=event_name,
        end_date=end_date,
        theme=theme,
        layout=layout
    )
    db.session.add(timer)
    db.session.commit()
    
    return redirect(url_for('view_timer', timer_id=timer.id, token=timer.edit_token))

@app.route('/timer/<timer_id>')
def view_timer(timer_id):
    timer = models.Timer.query.get_or_404(timer_id)
    token = request.args.get('token')
    return render_template('timer.html', timer=timer, token=token if token == timer.edit_token else None)

@app.route('/timer/<timer_id>/edit')
def edit_timer_form(timer_id):
    timer = models.Timer.query.get_or_404(timer_id)
    token = request.args.get('token')
    
    if token != timer.edit_token:
        abort(403)
    
    return render_template('edit.html', timer=timer, token=token)

@app.route('/timer/<timer_id>/edit', methods=['POST'])
def edit_timer(timer_id):
    timer = models.Timer.query.get_or_404(timer_id)
    token = request.args.get('token')
    
    if token != timer.edit_token:
        abort(403)
    
    timer.event_name = request.form['event_name']
    timer.end_date = datetime.fromisoformat(request.form['end_date'].replace('Z', '+00:00'))
    timer.theme = request.form.get('theme', 'default')
    timer.layout = request.form.get('layout', 'standard')
    
    db.session.commit()
    return redirect(url_for('view_timer', timer_id=timer.id, token=token))

@app.route('/timer/<timer_id>/delete', methods=['POST'])
def delete_timer(timer_id):
    timer = models.Timer.query.get_or_404(timer_id)
    token = request.args.get('token')
    
    if token != timer.edit_token:
        abort(403)
    
    db.session.delete(timer)
    db.session.commit()
    return '', 204

@app.route('/manifest/<timer_id>')
def manifest(timer_id):
    timer = models.Timer.query.get_or_404(timer_id)
    manifest_data = {
        "name": f"Countdown: {timer.event_name}",
        "short_name": timer.event_name,
        "start_url": f"/timer/{timer.id}",
        "display": "standalone",
        "background_color": "#212529",
        "theme_color": "#212529",
        "icons": [{
            "src": url_for('static', filename='icons/timer.svg'),
            "sizes": "any",
            "type": "image/svg+xml"
        }]
    }
    return jsonify(manifest_data)

@app.route('/api/timer/<timer_id>')
def get_timer_data(timer_id):
    timer = models.Timer.query.get_or_404(timer_id)
    return {
        'event_name': timer.event_name,
        'end_date': timer.end_date.isoformat(),
        'theme': timer.theme,
        'layout': timer.layout
    }
