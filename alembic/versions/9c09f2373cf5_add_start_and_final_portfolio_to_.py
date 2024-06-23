"""Add start and final portfolio to BacktestResult

Revision ID: 9c09f2373cf5
Revises: a8713f9aafb8
Create Date: 2024-06-22 15:07:28.375347

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c09f2373cf5'
down_revision: Union[str, None] = 'a8713f9aafb8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fact_backtests', sa.Column('StartPortfolio', sa.Numeric(precision=18, scale=4), nullable=True))
    op.add_column('fact_backtests', sa.Column('FinalPortfolio', sa.Numeric(precision=18, scale=4), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('fact_backtests', 'FinalPortfolio')
    op.drop_column('fact_backtests', 'StartPortfolio')
    # ### end Alembic commands ###