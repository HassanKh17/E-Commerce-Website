"""Description of changes5

Revision ID: 56c3b4fff3f2
Revises: 742742469f2f
Create Date: 2023-12-06 01:08:06.296936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56c3b4fff3f2'
down_revision = '742742469f2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('order_item_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'order_items', ['order_item_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('order_item_id')

    # ### end Alembic commands ###
