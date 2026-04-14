# CapCut SaaS

A SaaS platform for generating CapCut (剪映) video drafts from templates with user-provided materials.

## Architecture

- **Frontend**: React + Vite + TypeScript
- **Backend**: FastAPI + Python
- **Database**: PostgreSQL
- **Storage**: MinIO (S3-compatible)
- **Cache**: Redis

## Quick Start

### Development

1. Start infrastructure:
```bash
docker-compose up -d db redis minio
```

2. Install backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Run backend:
```bash
cd backend
uvicorn app.main:app --reload --port 8000
```

4. Install frontend dependencies:
```bash
cd frontend
npm install
```

5. Run frontend:
```bash
cd frontend
npm run dev
```

### Production (Docker)

```bash
docker-compose up -d
```

## Features

- User authentication (JWT)
- Workspace management
- Material upload (video/audio/images)
- Template system
- Draft generation from templates
- Export CapCut-compatible JSON

## Project Structure

```
capcut-saas/
├── backend/
│   ├── app/
│   │   ├── api/v1/       # API routes
│   │   ├── models/       # SQLAlchemy models
│   │   ├── services/     # Business logic
│   │   └── draft_engine/ # Draft generation
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── pages/        # React pages
│   │   └── services/     # API client
│   ├── Dockerfile
│   └── package.json
├── docker-compose.yml
└── nginx/
    └── nginx.conf
```

## API Endpoints

### Auth
- `POST /api/v1/auth/register` - Register user
- `POST /api/v1/auth/login` - Login
- `GET /api/v1/auth/me` - Get current user

### Workspaces
- `GET /api/v1/workspaces` - List workspaces
- `POST /api/v1/workspaces` - Create workspace

### Materials
- `GET /api/v1/workspaces/:id/materials` - List materials
- `POST /api/v1/workspaces/:id/materials/upload` - Upload material

### Templates
- `GET /api/v1/workspaces/:id/templates` - List templates
- `POST /api/v1/workspaces/:id/templates` - Create template

### Drafts
- `POST /api/v1/workspaces/:wid/projects/:pid/drafts/generate` - Generate draft
- `GET /api/v1/workspaces/:wid/projects/:pid/drafts/:id/export` - Export draft

## Usage Flow

1. Register/Login
2. Create a workspace
3. Upload video/audio/image materials
4. Import or create a template (CapCut draft JSON)
5. Generate a new draft by mapping materials to template placeholders
6. Export the draft JSON
7. Open in CapCut, make manual adjustments
8. Export final video in CapCut
