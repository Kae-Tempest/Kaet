"""create restaurant table

Revision ID: ceb3231cb040
Revises: 
Create Date: 2024-12-15 19:14:12.367717

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'restaurants',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('country', sa.String, nullable=False),
        sa.Column('street', sa.String, nullable=False),
        sa.Column('number', sa.String, nullable=False),
        sa.Column('is_open', sa.Boolean, nullable=False),
        sa.Column('hourly', sa.JSON, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
    )


def downgrade() -> None:
    op.drop_table('restaurants')
