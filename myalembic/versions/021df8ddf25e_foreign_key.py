"""foreign-key

Revision ID: 021df8ddf25e
Revises: b6b8b7be25b7
Create Date: 2024-05-16 19:35:52.336125

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic. 
revision: str = '021df8ddf25e'
down_revision: Union[str, None] = 'b6b8b7be25b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() :
    op.add_column('posts',sa.Column('user_id',sa.
                                    Integer(),nullable=False))
    op.create_foreign_key('post_user_fk',source_table='posts',referent_table='user',local_cols=['user_id'],remote_cols=['id'],ondelete='CASCADE')

    pass


def downgrade():
    op.drop_constraint('post_user_fk', 'posts', type_='foreignkey')
    op.drop_column('posts','user_id')
    pass
