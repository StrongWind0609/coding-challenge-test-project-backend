# backend/main.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import math

app = FastAPI()

# Enable CORS for frontend dev server on localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Fake job data structure (simplified)
class Job(BaseModel):
    id: str
    jobTitle: str
    location: str
    dateFound: str  # ISO date string
    description: str

# Generate 50 fake jobs for pagination and filtering demo
FAKE_JOBS = [
    Job(
        id=str(i),
        jobTitle=f"Fullstack Developer {i}",
        location="Hilversum, NL" if i % 2 == 0 else "Amsterdam, NL",
        dateFound=f"2025-07-{(i%30)+1:02d}T12:00:00Z",
        description="This is a sample job description for job #" + str(i)
    )
    for i in range(1, 51)
]

@app.post("/api/token")
async def get_token():
    # Stub token response
    return {"access_token": "stubbed-bearer-token", "token_type": "bearer"}

@app.get("/api/jobs", response_model=List[Job])
async def get_jobs(
    search: Optional[str] = Query(None),
    location: Optional[str] = Query(None),
    maxAgeDays: Optional[int] = Query(None),
    page: int = Query(1, ge=1),
    pageSize: int = Query(10, ge=1, le=25),
):
    filtered = FAKE_JOBS

    # Filter by search text in jobTitle (case-insensitive)
    if search:
        filtered = [job for job in filtered if search.lower() in job.jobTitle.lower()]

    # Filter by location substring (case-insensitive)
    if location:
        filtered = [job for job in filtered if location.lower() in job.location.lower()]

    # Filter by maxAgeDays (dateFound after today - maxAgeDays)
    if maxAgeDays is not None:
        from datetime import datetime, timedelta, timezone
        cutoff = datetime.now(timezone.utc) - timedelta(days=maxAgeDays)
        filtered = [
            job for job in filtered if datetime.fromisoformat(job.dateFound.replace("Z", "+00:00")).astimezone(timezone.utc) >= cutoff
        ]

    # Pagination
    start = (page - 1) * pageSize
    end = start + pageSize
    paged = filtered[start:end]

    return paged
