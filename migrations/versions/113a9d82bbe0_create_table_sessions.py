"""create table sessions

Revision ID: 113a9d82bbe0
Revises: 4adeea899717
Create Date: 2023-06-12 18:53:07.400690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '113a9d82bbe0'
down_revision = '4adeea899717'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Сессии пользователей',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session_id', sa.String(), nullable=True),
    sa.Column('user_id', sa.UUID(), nullable=True),
    sa.Column('status', sa.Boolean(create_constraint=True), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('session_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Сессии пользователей')
    # ### end Alembic commands ###
