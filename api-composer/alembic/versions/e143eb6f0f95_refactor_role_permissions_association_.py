"""Refactor role_permissions association table

Revision ID: e143eb6f0f95
Revises: f9233720c0c5
Create Date: 2024-09-01 21:46:30.148838

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import inspect


# revision identifiers, used by Alembic.
revision: str = 'e143eb6f0f95'
down_revision: Union[str, None] = 'f9233720c0c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    inspector = inspect(op.get_bind())
    if 'role_permissions' not in inspector.get_table_names():
        op.create_table(
            'role_permissions',
            sa.Column('role_id', sa.Integer, sa.ForeignKey(
                'roles.id'), primary_key=True),
            sa.Column('permission_id', sa.Integer, sa.ForeignKey(
                'permissions.id'), primary_key=True)
        )


def downgrade() -> None:
    op.drop_table('role_permissions')
