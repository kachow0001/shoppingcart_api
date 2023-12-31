"""empty message

Revision ID: 8546c27ac8cc
Revises: 188e6874b3a4
Create Date: 2023-07-27 17:03:05.364727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8546c27ac8cc'
down_revision = '188e6874b3a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts', sa.Column('account_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'accounts', 'accounts', ['account_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('admins_account_id_fkey', 'admins', type_='foreignkey')
    op.create_foreign_key(None, 'admins', 'accounts', ['account_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('categories_user_id_fkey', 'categories', type_='foreignkey')
    op.create_foreign_key(None, 'categories', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'categories', type_='foreignkey')
    op.create_foreign_key('categories_user_id_fkey', 'categories', 'users', ['user_id'], ['id'])
    op.drop_constraint(None, 'admins', type_='foreignkey')
    op.create_foreign_key('admins_account_id_fkey', 'admins', 'accounts', ['account_id'], ['id'])
    op.drop_constraint(None, 'accounts', type_='foreignkey')
    op.drop_column('accounts', 'account_id')
    # ### end Alembic commands ###
