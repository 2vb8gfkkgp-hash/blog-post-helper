from datetime import datetime
from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200))
    topic: Mapped[str] = mapped_column(String(200))
    audience: Mapped[str | None] = mapped_column(String(200), nullable=True)
    deadline: Mapped[Date | None] = mapped_column(Date, nullable=True)
    draft: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    sources: Mapped[list["Source"]] = relationship(back_populates="project", cascade="all, delete-orphan")
    claims: Mapped[list["Claim"]] = relationship(back_populates="project", cascade="all, delete-orphan")


class Source(Base):
    __tablename__ = "sources"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    url: Mapped[str] = mapped_column(String(500))
    title: Mapped[str] = mapped_column(String(300))
    publisher: Mapped[str | None] = mapped_column(String(200), nullable=True)
    author: Mapped[str | None] = mapped_column(String(200), nullable=True)
    published_date: Mapped[Date | None] = mapped_column(Date, nullable=True)
    source_type: Mapped[str | None] = mapped_column(String(100), nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    excerpts: Mapped[str | None] = mapped_column(Text, nullable=True)
    is_primary: Mapped[bool] = mapped_column(Boolean, default=False)

    project: Mapped["Project"] = relationship(back_populates="sources")


class Claim(Base):
    __tablename__ = "claims"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    text: Mapped[str] = mapped_column(Text)
    claim_type: Mapped[str] = mapped_column(String(100), default="needs evidence")
    status: Mapped[str] = mapped_column(String(100), default="needs review")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    project: Mapped["Project"] = relationship(back_populates="claims")
