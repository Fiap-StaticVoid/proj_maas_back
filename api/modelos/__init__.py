from pydantic import BaseModel
from uuid import UUID


class BaseRecurso(BaseModel):
    id: UUID
