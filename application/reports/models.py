from application.extensions import db


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    title = db.Column(db.String(128), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    progress = db.Column(db.Integer, nullable=False)

    def __init__(self, title, summary, priority):
        self.title = title
        self.summary = summary
        self.priority = priority
        self.progress = 0
