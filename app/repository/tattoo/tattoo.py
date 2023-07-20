from fastapi import Depends
from app.repository.repository import BaseRepository
from app.repository.tattoo.models import *
from app.repository.work_session import get_db


class WorksRepository(BaseRepository):
    model = Job


class WorksCategoryRepository(BaseRepository):
    model = JobCategory


class SketchesRepository(BaseRepository):
    model = Sketch


class SketchesCategoryRepository(BaseRepository):
    model = SketchCategory


class TattooRepository:

    def __init__(self, db=Depends(get_db)):
        self.works_repository = WorksRepository(db)
        self.category_works_repository = WorksCategoryRepository(db)
        self.sketches_repository = SketchesRepository(db)
        self.category_sketches_repository = SketchesCategoryRepository(db)