from fastapi import APIRouter
from .. import schemas
from backend.database import cr, conn


router = APIRouter(tags=["Members"], prefix="/member")


@router.get("/all", response_model=list[schemas.ReturnLogin])
def get_all_memebers():
    cr.execute("""SELECT * FROM users """)
    members = cr.fetchall()
    return members
