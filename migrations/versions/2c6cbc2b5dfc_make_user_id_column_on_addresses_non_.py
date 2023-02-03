"""Make user_id column on addresses non-nullable

Revision ID: 2c6cbc2b5dfc
Revises: 73c1613e527d
Create Date: 2023-02-03 15:58:05.166966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c6cbc2b5dfc'
down_revision = '73c1613e527d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('addresses', 'user_id',
               existing_type=sa.UUID(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('addresses', 'user_id',
               existing_type=sa.UUID(),
               nullable=True)
    # ### end Alembic commands ###