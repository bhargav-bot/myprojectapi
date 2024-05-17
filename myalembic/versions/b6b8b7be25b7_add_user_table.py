"""add_user_table

Revision ID: b6b8b7be25b7
Revises: 43071287183a
Create Date: 2024-05-16 19:24:45.062398

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b6b8b7be25b7'
down_revision: Union[str, None] = '43071287183a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('user',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),sa.Column('name',sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('user')
    pass
