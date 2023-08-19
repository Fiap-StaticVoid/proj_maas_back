from typing import Annotated
from uuid import UUID, uuid4
from sqlalchemy.orm import mapped_column


UUIDPK = Annotated[UUID, mapped_column(primary_key=True, default=uuid4)]
