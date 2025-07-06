from fastapi import FastAPI, Request
from app.api import pt
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="USAF PT Calculator API")

# Include the PT calculator router
app.include_router(pt.router, prefix="/api/pt", tags=["PT Calculator"])

# Serve React build as static files if it exists
frontend_build_dir = os.path.join(os.path.dirname(__file__), "frontend", "build")
if os.path.isdir(frontend_build_dir):
    app.mount("/static", StaticFiles(directory=os.path.join(frontend_build_dir, "static")), name="static")

    @app.get("/{full_path:path}")
    async def serve_react_app(request: Request, full_path: str):
        # Only serve index.html for non-API routes
        if request.url.path.startswith("/api/"):
            return {"detail": "Not Found"}
        index_path = os.path.join(frontend_build_dir, "index.html")
        return FileResponse(index_path)

# Root endpoint (for health check or API info)
@app.get("/api")
def read_root():
    return {"message": "Welcome to the USAF PT Calculator API!"}
