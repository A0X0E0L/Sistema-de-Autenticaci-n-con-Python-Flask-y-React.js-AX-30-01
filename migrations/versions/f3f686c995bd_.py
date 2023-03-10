"""empty message

Revision ID: f3f686c995bd
Revises: ecf3eac9cf73
Create Date: 2023-01-26 14:40:56.847440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3f686c995bd'
down_revision = 'ecf3eac9cf73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('single__user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('single__user')
    # ### end Alembic commands ###
