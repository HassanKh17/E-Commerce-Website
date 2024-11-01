"""Description of changes7

Revision ID: 2ad722b81107
Revises: ef67cff0f339
Create Date: 2023-12-06 01:44:30.603875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ad722b81107'
down_revision = 'ef67cff0f339'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.alter_column('order_item_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.drop_constraint('fk_review_order_item', type_='foreignkey')
        batch_op.create_foreign_key(None, 'orders', ['order_item_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('fk_review_order_item', 'order_items', ['order_item_id'], ['id'])
        batch_op.alter_column('order_item_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
