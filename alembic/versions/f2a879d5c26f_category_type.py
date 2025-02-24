"""category-type

Revision ID: f2a879d5c26f
Revises: 8c62318a54b2
Create Date: 2025-02-22 12:49:43.871089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2a879d5c26f'
down_revision: Union[str, None] = '8c62318a54b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Categories', sa.Column('type', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Categories', 'type')
    # ### end Alembic commands ###
