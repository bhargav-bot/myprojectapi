"""create posts table

Revision ID: 1b3b38115c17
Revises: 
Create Date: 2024-05-15 05:24:10.113819

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b3b38115c17'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',
        sa.Column('content', sa.String(), nullable=False)
    )

    pass


def downgrade():
    op.drop_table('posts')
    pass
