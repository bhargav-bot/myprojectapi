"""change the keytype

Revision ID: 2c7456bd0202
Revises: 021df8ddf25e
Create Date: 2024-05-16 19:43:08.779498

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2c7456bd0202'
down_revision: Union[str, None] = '021df8ddf25e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
