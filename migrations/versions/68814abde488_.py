"""empty message

Revision ID: 68814abde488
Revises: 728af93e7009
Create Date: 2019-09-18 11:38:23.121066

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68814abde488'
down_revision = '728af93e7009'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
