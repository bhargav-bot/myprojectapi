"""newtable with content column

Revision ID: b3a6378e04a1
Revises: 1b3b38115c17
Create Date: 2024-05-15 22:27:23.083323

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b3a6378e04a1'
down_revision: Union[str, None] = '1b3b38115c17'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False),

    )
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
