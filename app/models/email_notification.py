from __future__ import unicode_literals

from future.utils import python_2_unicode_compatible

from app.models import db
from utils.compat import u


@python_2_unicode_compatible
class EmailNotification(db.Model):
    """email notifications model class"""
    __tablename__ = 'email_notifications'
    id = db.Column(db.Integer,
                   primary_key=True)
    next_event = db.Column(db.Boolean, default=False)
    new_paper = db.Column(db.Boolean, default=False)
    session_accept_reject = db.Column(db.Boolean, default=False)
    session_schedule = db.Column(db.Boolean, default=False)
    after_ticket_purchase = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id', ondelete='CASCADE'))
    event = db.relationship("Event")
    user = db.relationship("User", backref="email_notifications")

    def __init__(self,
                 next_event=False,
                 new_paper=False,
                 session_accept_reject=False,
                 session_schedule=False,
                 after_ticket_purchase=True,
                 user_id=None,
                 event_id=None):
        self.next_event = next_event
        self.new_paper = new_paper
        self.session_accept_reject = session_accept_reject
        self.session_schedule = session_schedule
        self.user_id = user_id
        self.event_id = event_id
        self.after_ticket_purchase = after_ticket_purchase

    def __str__(self):
        return u('User:' + self.user_id + ' Event: ' + self.event_id)
