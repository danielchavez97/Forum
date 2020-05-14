"""empty message

Revision ID: 2290731c1bbf
Revises: b8e22a359c3c
Create Date: 2020-04-26 02:32:10.762041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2290731c1bbf"
down_revision = "b8e22a359c3c"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_test_timestamp", table_name="test")
    op.drop_table("test")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "test",
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("title", sa.VARCHAR(length=128), nullable=True),
        sa.Column("body", sa.TEXT(), nullable=True),
        sa.Column("timestamp", sa.DATETIME(), nullable=True),
        sa.Column("author_id", sa.INTEGER(), nullable=True),
        sa.ForeignKeyConstraint(["author_id"], ["users.id"],),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_test_timestamp", "test", ["timestamp"], unique=False)
    # ### end Alembic commands ###
