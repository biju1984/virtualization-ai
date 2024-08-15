"""Initial migration

Revision ID: 0253211db6b4
Revises: 11ce611daf96
Create Date: 2024-07-21 21:05:27.182988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0253211db6b4'
down_revision = '11ce611daf96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('specifications', sa.Column('name', sa.String(), nullable=False))
    op.add_column('specifications', sa.Column('description', sa.String(), nullable=True))
    op.add_column('specifications', sa.Column('spec_type', sa.String(), nullable=False))
    op.add_column('specifications', sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
    op.add_column('specifications', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('specifications', 'updated_at')
    op.drop_column('specifications', 'created_at')
    op.drop_column('specifications', 'spec_type')
    op.drop_column('specifications', 'description')
    op.drop_column('specifications', 'name')
    # ### end Alembic commands ###
