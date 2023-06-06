"""add user table

Revision ID: 9bfd1af6be28
Revises: 56da379a6527
Create Date: 2023-06-02 11:34:11.290153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bfd1af6be28'
down_revision = '56da379a6527'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',sa.Column('id',sa.Integer(),nullable=False),
                    sa.Column('email',sa.String(),nullable=False),
                    sa.Column('pasword',sa.String(),nullable=False),
                    sa.Column('created_at',sa.TIMESTAMP(timezone='now()'),nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_index('users')
    pass
