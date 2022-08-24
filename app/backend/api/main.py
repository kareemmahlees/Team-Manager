from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ..database import cr, conn
from . import schemas
from .routers import members, tasks


app = FastAPI()

app.include_router(members.router)
app.include_router(tasks.router)


@app.get("/")
def route():
    return {"msg", "Hello World"}


@app.post("/login", response_model=schemas.ReturnLogin)
def login_user(credentials: OAuth2PasswordRequestForm = Depends()):
    cr.execute(
        """select * from users where username=%s and password =%s""",
        (credentials.username, credentials.password),
    )
    user = cr.fetchone()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User '{credentials.username} was not found'",
        )
    return user
