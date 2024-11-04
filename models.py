from app import db
import uuid
from datetime import datetime

class Timer(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    event_name = db.Column(db.String(200), nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    theme = db.Column(db.String(50), default='default')
    layout = db.Column(db.String(50), default='standard')
