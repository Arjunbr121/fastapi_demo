"""add contrnt column in the post table

Revision ID: 56da379a6527
Revises: d73a02dd6685
Create Date: 2023-06-02 11:29:34.305768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56da379a6527'
down_revision = 'd73a02dd6685'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('contenet',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','contenet')
    pass
