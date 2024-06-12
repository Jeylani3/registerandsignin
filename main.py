# File: app/main.py

from fastapi import FastAPI, Depends
from auth import router as auth_router
from config import get_db_connection
from server import app as server_app

app = server_app
@app.get("/test-db-connection")
def test_db_connection(db_conn = Depends(get_db_connection)):
    if db_conn:
        return {"message": "Database connection successful"}
    else:
        return {"message": "Failed to connect to the database"}
    

# Include the auth router
# `app.include_router(auth_router, prefix="/auth")` is including the routes defined in the
# `auth_router` in the FastAPI application `app`. The `prefix="/auth"` parameter specifies that all
# routes defined in the `auth_router` will be accessible under the `/auth` URL path. This helps in
# organizing and grouping related routes together under a common base path.
app.include_router(auth_router)
