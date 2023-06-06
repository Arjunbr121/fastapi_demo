"""add the login table

Revision ID: 221fc896afd4
Revises: f2f4bb324cfb
Create Date: 2023-06-06 10:48:10.709963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '221fc896afd4'
down_revision = 'f2f4bb324cfb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('login',sa.Column('id',sa.Integer(),nullable=False),
                    sa.Column('Username',sa.String(),nullable=False),
                    sa.Column('email',sa.String(),nullable=False),
                    sa.Column('pasword',sa.String(),nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone='now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_index('login')
    pass
