"""create reservations table

Revision ID: 901e37d5c416
Revises: bf3265cdb01b
Create Date: 2024-12-15 19:26:17.248799

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4'
down_revision: Union[str, None] = '3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'reservations',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('restaurant_id', sa.Integer, nullable=False),
        sa.Column('table_id', sa.Integer, nullable=False),
        sa.Column('reserved_at', sa.DateTime, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, nullable=False, server_default=sa.func.now()),
    )
    op.create_foreign_key(
        'fk_reservations_table',
        'reservations', 'tables',
        ['table_id'], ['id']
    )
    op.create_foreign_key(
        'fk_reservations_restaurant',
        'reservations', 'restaurants',
        ['restaurant_id'], ['id']
    )

def downgrade() -> None:
    op.drop_table('reservations')
