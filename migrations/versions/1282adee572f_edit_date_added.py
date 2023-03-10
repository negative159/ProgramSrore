"""edit date_added

Revision ID: 1282adee572f
Revises: 
Create Date: 2023-03-01 20:06:59.824920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1282adee572f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.alter_column('date_added',
               existing_type=sa.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.alter_column('date_added',
               existing_type=sa.Date(),
               type_=sa.DATETIME(),
               existing_nullable=True)

    # ### end Alembic commands ###
