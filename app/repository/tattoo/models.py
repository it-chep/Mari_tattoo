from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, JSON
from sqlalchemy.orm import relationship

from app.repository.work_session import Base


class JobCategory(Base):
    __tablename__ = 'jobs_categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    jobs = relationship('Job', back_populates='category')


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    photo = Column(String(length=255), nullable=False)
    description = Column(String)
    date = Column(TIMESTAMP)
    category_id = Column(Integer, ForeignKey('jobs_categories.id'))
    tags = Column(JSON, nullable=True)
    price = Column(Integer)

    category = relationship('JobCategory', back_populates='jobs')


class SketchCategory(Base):
    __tablename__ = 'sketches_categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    sketches = relationship('Sketch', back_populates='category')


class Sketch(Base):
    __tablename__ = 'sketches'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    photo = Column(String(length=255), nullable=False)
    category_id = Column(Integer, ForeignKey('sketches_categories.id'))
    tags = Column(JSON, nullable=True)

    category = relationship('SketchCategory', back_populates='sketches')
