from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(self.model).all()

    def get_by_id(self, _id):
        return self.db.query(self.model).filter(self.model.id == _id).first()

    def create(self, item):
        db_item = self.model(**item.dict())
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def update(self, _id, item):
        db_item = self.db.query(self.model).filter(self.model.id == _id).first()
        if db_item is None:
            return None
        for attr, value in item.dict().items():
            setattr(db_item, attr, value) if value else None
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def delete(self, _id):
        db_item = self.db.query(self.model).filter(self.model.id == _id).first()
        if db_item is None:
            return None
        self.db.delete(db_item)
        self.db.commit()
        return db_item