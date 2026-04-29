from fastapi import FastAPI, Depends
import os, sqlite3

app = FastAPI(title="TITANIUM OS CONTROL PANEL")

@app.get("/")
def read_root():
    return {"status": "TITANIUM OS ONLINE", "version": "V1.0", "active_divisions": ["Dental", "Legal", "SaaS"]}

@app.get("/stats")
def get_stats():
    # Itt a holding összesített adatait kérjük le
    return {
        "total_revenue": "CHF 12,450",
        "mrr": "CHF 4,800",
        "active_leads": 142,
        "ai_worker_load": "14%"
    }
