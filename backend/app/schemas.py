from datetime import date, datetime
from pydantic import BaseModel, ConfigDict


class ProjectCreate(BaseModel):
    title: str
    topic: str
    audience: str | None = None
    deadline: date | None = None
    draft: str | None = None


class ProjectUpdate(BaseModel):
    title: str | None = None
    topic: str | None = None
    audience: str | None = None
    deadline: date | None = None
    draft: str | None = None


class ProjectRead(ProjectCreate):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class SourceCreate(BaseModel):
    url: str
    title: str
    publisher: str | None = None
    author: str | None = None
    published_date: date | None = None
    source_type: str | None = None
    notes: str | None = None
    excerpts: str | None = None
    is_primary: bool = False


class SourceRead(SourceCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class ClaimCreate(BaseModel):
    text: str
    claim_type: str | None = None
    status: str | None = None


class ClaimRead(ClaimCreate):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
