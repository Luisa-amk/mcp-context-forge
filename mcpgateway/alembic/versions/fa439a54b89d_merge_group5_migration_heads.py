"""merge_group5_migration_heads

Revision ID: fa439a54b89d
Revises: 1d27bc0a81f5, 373c8cc5e13a, 615af4ab94b4, a1b2c3d4e5f6, e1f2g3h4i5j6
Create Date: 2026-03-25 19:42:17.121733

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fa439a54b89d'
down_revision: Union[str, Sequence[str], None] = ('1d27bc0a81f5', '373c8cc5e13a', '615af4ab94b4', 'a1b2c3d4e5f6', 'e1f2g3h4i5j6')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
