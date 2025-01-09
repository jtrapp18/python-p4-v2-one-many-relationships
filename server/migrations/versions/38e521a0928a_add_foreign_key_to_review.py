from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '38e521a0928a'
down_revision = 'c52919f34234'
branch_labels = None
depends_on = None

def upgrade():
    # Using batch mode to handle constraints in SQLite
    with op.batch_alter_table('reviews') as batch_op:
        # Add the employee_id column
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        # Create the foreign key constraint
        batch_op.create_foreign_key('fk_reviews_employee_id_employees', 'employees', ['employee_id'], ['id'])

def downgrade():
    with op.batch_alter_table('reviews') as batch_op:
        # Drop the foreign key constraint
        batch_op.drop_constraint('fk_reviews_employee_id_employees')
        # Drop the employee_id column
        batch_op.drop_column('employee_id')
