from fastapi import FastAPI
from routes import deals, missions, mesh, intelligence, doctrine

app = FastAPI()

# Include routers
app.include_router(deals.router)
app.include_router(missions.router)
app.include_router(mesh.router)
app.include_router(intelligence.router)
app.include_router(doctrine.router)

# Health check endpoint
@app.get("/health")
def health():
    return {"status": "ok"}
