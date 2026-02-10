from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import claim_extraction, crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog Post Helper API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/projects", response_model=list[schemas.ProjectRead])
def list_projects(db: Session = Depends(get_db)):
    return crud.list_projects(db)


@app.post("/projects", response_model=schemas.ProjectRead)
def create_project(payload: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db, payload)


@app.get("/projects/{project_id}", response_model=schemas.ProjectRead)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@app.put("/projects/{project_id}", response_model=schemas.ProjectRead)
def update_project(project_id: int, payload: schemas.ProjectUpdate, db: Session = Depends(get_db)):
    project = crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return crud.update_project(db, project, payload)


@app.get("/projects/{project_id}/sources", response_model=list[schemas.SourceRead])
def list_sources(project_id: int, db: Session = Depends(get_db)):
    return crud.list_sources(db, project_id)


@app.post("/projects/{project_id}/sources", response_model=schemas.SourceRead)
def create_source(project_id: int, payload: schemas.SourceCreate, db: Session = Depends(get_db)):
    project = crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return crud.create_source(db, project_id, payload)


@app.get("/projects/{project_id}/claims", response_model=list[schemas.ClaimRead])
def list_claims(project_id: int, db: Session = Depends(get_db)):
    return crud.list_claims(db, project_id)


@app.post("/projects/{project_id}/claims", response_model=schemas.ClaimRead)
def create_claim(project_id: int, payload: schemas.ClaimCreate, db: Session = Depends(get_db)):
    project = crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return crud.create_claim(db, project_id, payload)


@app.post("/projects/{project_id}/claims/extract", response_model=list[schemas.ClaimRead])
def extract_claims(project_id: int, db: Session = Depends(get_db)):
    project = crud.get_project(db, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    if not project.draft:
        return []
    extracted = claim_extraction.extract_claims(project.draft)
    created = [crud.create_claim(db, project_id, schemas.ClaimCreate(text=text)) for text in extracted]
    return created
