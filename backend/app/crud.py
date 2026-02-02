from sqlalchemy.orm import Session

from . import models, schemas


def create_project(db: Session, payload: schemas.ProjectCreate) -> models.Project:
    project = models.Project(**payload.model_dump())
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def list_projects(db: Session) -> list[models.Project]:
    return db.query(models.Project).order_by(models.Project.created_at.desc()).all()


def get_project(db: Session, project_id: int) -> models.Project | None:
    return db.query(models.Project).filter(models.Project.id == project_id).first()


def update_project(db: Session, project: models.Project, payload: schemas.ProjectUpdate) -> models.Project:
    data = payload.model_dump(exclude_unset=True)
    for key, value in data.items():
        setattr(project, key, value)
    db.commit()
    db.refresh(project)
    return project


def create_source(db: Session, project_id: int, payload: schemas.SourceCreate) -> models.Source:
    source = models.Source(project_id=project_id, **payload.model_dump())
    db.add(source)
    db.commit()
    db.refresh(source)
    return source


def list_sources(db: Session, project_id: int) -> list[models.Source]:
    return db.query(models.Source).filter(models.Source.project_id == project_id).all()


def create_claim(db: Session, project_id: int, payload: schemas.ClaimCreate) -> models.Claim:
    data = payload.model_dump()
    if not data.get("claim_type"):
        data["claim_type"] = "needs evidence"
    if not data.get("status"):
        data["status"] = "needs review"
    claim = models.Claim(project_id=project_id, **data)
    db.add(claim)
    db.commit()
    db.refresh(claim)
    return claim


def list_claims(db: Session, project_id: int) -> list[models.Claim]:
    return db.query(models.Claim).filter(models.Claim.project_id == project_id).all()
