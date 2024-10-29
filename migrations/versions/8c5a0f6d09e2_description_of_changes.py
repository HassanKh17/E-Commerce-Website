"""Description of changes

Revision ID: 8c5a0f6d09e2
Revises: d28441ce63b2
Create Date: 2023-12-05 18:35:46.470001

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c5a0f6d09e2'
down_revision = 'd28441ce63b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('order_item_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'order_items', ['order_item_id'], ['id'])
        batch_op.drop_column('content')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('content', sa.VARCHAR(), nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('order_item_id')

    # ### end Alembic commands ###
