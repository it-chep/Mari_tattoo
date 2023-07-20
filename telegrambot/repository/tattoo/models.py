from sqlalchemy import MetaData, String, Integer, TIMESTAMP, ForeignKey, Table, Column, JSON

metadata = MetaData()

sketches = Table(
    'sketches',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("description", String),
    Column("photo", String(length=255), nullable=False),
    Column("category_id", Integer, ForeignKey('sketches_categories.id')),
    Column("Tags", JSON, nullable=True)
)

jobs = Table(
    'jobs',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("photo", String(length=255), nullable=False),
    Column("description", String),
    Column("date", TIMESTAMP),
    Column("category_id", Integer, ForeignKey('jobs_categories.id')),
    Column("Tags", JSON, nullable=True),
    Column("price", Integer)
)

jobs_categories = Table(
    'jobs_categories',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False)
)

sketches_categories = Table(
    'sketches_categories',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False)
)

