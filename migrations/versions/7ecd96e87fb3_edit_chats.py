"""edit chats

Revision ID: 7ecd96e87fb3
Revises: fb771009b3e4
Create Date: 2025-05-22 14:05:21.888589

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '7ecd96e87fb3'
down_revision: Union[str, None] = 'fb771009b3e4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'chats', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'chats', type_='foreignkey')
    # ### end Alembic commands ###
