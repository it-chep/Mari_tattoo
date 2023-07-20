from fastapi import Depends
from .models import Session
from app.repository.work_session import get_db
from ..users.users import UsersRepository
from ..users.models import User


class SessionRepository:
    def __init__(self, db=Depends(get_db)):
        self.db = db

    def create_session(self, session_id, user, ):
        session = Session(
            session_id=session_id,
            user=user
        )
        self.db.add(session)
        self.db.commit()
        return session.session_id

    def delete_session(self, session_id):
        self.db.query(Session).filter(Session.session_id == session_id).delete()
        self.db.commit()

        pass

    def get_user_from_session_id(self, session_id):
        session = self.db.query(Session).filter(Session.session_id == session_id).first()

        if session:
            user = session.user
            return user

        return None

    # def session_by_user_id(self, email: str = ''):
    #     user = self.db.query(User).filter(User.email == email).first()
    #
    #     if user is None:
    #         return
    #
    #     session = self.db.query(Session).filter(Session.user_id == user.user_id).first()
    #
    #     if session is None:
    #         return
    #
    #     return session.session_id
