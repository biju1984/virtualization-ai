"""Initial migration

Revision ID: 11ce611daf96
Revises: 
Create Date: 2024-07-21 19:55:29.645230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11ce611daf96'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('specifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('version', sa.Integer(), nullable=True),
    sa.Column('spec', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_specifications_id'), 'specifications', ['id'], unique=False)
    op.create_index(op.f('ix_specifications_version'), 'specifications', ['version'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_specifications_version'), table_name='specifications')
    op.drop_index(op.f('ix_specifications_id'), table_name='specifications')
    op.drop_table('specifications')
    # ### end Alembic commands ###
