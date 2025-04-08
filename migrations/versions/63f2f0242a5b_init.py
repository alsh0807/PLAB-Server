"""init

Revision ID: 63f2f0242a5b
Revises: 53fb53f1d37b
Create Date: 2025-04-08 10:31:36.244151

"""
from typing import Sequence, Union

import sqlmodel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63f2f0242a5b'
down_revision: Union[str, None] = '53fb53f1d37b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('username', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=False),
    sa.Column('password_hash', sa.VARCHAR(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
