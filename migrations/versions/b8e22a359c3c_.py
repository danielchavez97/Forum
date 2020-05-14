"""empty message

Revision ID: b8e22a359c3c
Revises: fce1e45925d8
Create Date: 2020-04-26 01:13:11.320050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b8e22a359c3c"
down_revision = "fce1e45925d8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("posts", sa.Column("scene_updated", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "posts", "scenes", ["scene_updated"], ["id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "posts", type_="foreignkey")
    op.drop_column("posts", "scene_updated")
    # ### end Alembic commands ###
