"""create tables table

Revision ID: bf3265cdb01b
Revises: 20d331000d3f
Create Date: 2024-12-15 19:23:57.166426

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '3'
down_revision: Union[str, None] = '2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'tables',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('is_reserved', sa.Boolean, nullable=False),
        sa.Column('nbr_person', sa.Integer, nullable=False),
        sa.Column('restaurant_id', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
    )
    op.create_foreign_key(
        'fk_tables_restaurant',
        'tables', 'restaurants',
        ['restaurant_id'], ['id'])


def downgrade() -> None:
    op.drop_table('tables')
