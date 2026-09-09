from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from app.database.connection import check_db_connection
from app.config import settings

app = FastAPI(
    title="DBPilot API",
    description="Natural Language to Safe SQL Engine for PostgreSQL",
    version="0.1.0",
)

# Enable CORS for React Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    """Health endpoint returning application and database readiness state."""
    db_ok = check_db_connection()
    if not db_ok:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={"status": "degraded", "database": "disconnected"},
        )
    return {
        "status": "healthy",
        "database": "connected",
        "environment": settings.APP_ENV,
    }