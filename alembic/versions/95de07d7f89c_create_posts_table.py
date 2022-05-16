"""create posts table

Revision ID: 95de07d7f89c
Revises: 
Create Date: 2022-05-15 15:14:39.910900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95de07d7f89c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(),nullable=False,
                                       primary_key=True),sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
