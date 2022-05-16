"""add new column

Revision ID: c2170bd3165e
Revises: 95de07d7f89c
Create Date: 2022-05-15 18:42:18.584075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2170bd3165e'
down_revision = '95de07d7f89c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
