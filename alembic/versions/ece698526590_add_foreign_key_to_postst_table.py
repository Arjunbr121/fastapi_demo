"""add foreign key to postst  table

Revision ID: ece698526590
Revises: 9bfd1af6be28
Create Date: 2023-06-02 11:55:06.935573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ece698526590'
down_revision = '9bfd1af6be28'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('posts_users_fk',source_table="posts",referent_table="users",local_cols=["owner_id"],
                        remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')
    pass
