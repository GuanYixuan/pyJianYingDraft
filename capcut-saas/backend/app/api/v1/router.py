from fastapi import APIRouter
from app.api.v1 import auth, workspaces, projects, materials, templates, drafts

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
router.include_router(workspaces.router, prefix="/workspaces", tags=["Workspaces"])
router.include_router(projects.router, prefix="/workspaces/{workspace_id}/projects", tags=["Projects"])
router.include_router(materials.router, prefix="/workspaces/{workspace_id}/materials", tags=["Materials"])
router.include_router(templates.router, prefix="/workspaces/{workspace_id}/templates", tags=["Templates"])
router.include_router(drafts.router, prefix="/workspaces/{workspace_id}/projects/{project_id}/drafts", tags=["Drafts"])
