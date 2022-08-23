from fastapi import APIRouter
from .. import models
from backend.database import cr, conn


router = APIRouter(tags=["Members"], prefix="/member")


@router.get("/all", response_model=list[models.ReturnLogin])
def get_all_memebers():
    cr.execute("""SELECT * FROM users """)
    members = cr.fetchall()
    return members
