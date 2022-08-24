from fastapi import APIRouter
from backend.database import cr, conn
from .. import schemas

router = APIRouter(tags=["Tasks"], prefix="/task")


@router.get("/all", response_model=list[schemas.TaskReturn])
def get_all_tasks():
    cr.execute("""SELECT * FROM tasks""")
    tasks = cr.fetchall()
    return tasks
