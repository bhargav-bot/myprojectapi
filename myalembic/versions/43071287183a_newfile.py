"""newfile

Revision ID: 43071287183a
Revises: b3a6378e04a1
Create Date: 2024-05-16 19:18:33.636257

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43071287183a'
down_revision: Union[str, None] = 'b3a6378e04a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column('rehsr',sa.String(),nullable=False))
    


def downgrade():
    op.drop_column('posts','rehsr')
    pass
