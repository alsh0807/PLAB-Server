"""create chat

Revision ID: 9ba332328e8c
Revises: 28aa37e338ae
Create Date: 2025-04-23 18:42:12.762895

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '9ba332328e8c'
down_revision: Union[str, None] = '28aa37e338ae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chats',
    sa.Column('user_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('last_answer', sa.VARCHAR(), nullable=False),
    sa.Column('last_question', sa.VARCHAR(), nullable=False),
    sa.Column('type', sa.VARCHAR(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_chats_id'), 'chats', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_chats_id'), table_name='chats')
    op.drop_table('chats')
    # ### end Alembic commands ###
