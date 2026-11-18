from server.model.user import User
from server.model.admin import Admin
from server.config.database import get_db
from fastapi import Depends, FastAPI
from server.query import user

router=FastAPI()
@router.get("/users/{user_id}")
def get_user(user_id: int, db=Depends(get_db)):
    return user.get_user(user_id, db)

@router.get("/admins/{admin_id}")
def get_admin(admin_id: int, db=Depends(get_db)):
    return user.get_admin(admin_id, db)

@router.post("/users")
def create_user(user: User, db=Depends(get_db)):
    return user.create_user(user, db)

@router.post("/admins")
def create_admin(admin: Admin, db=Depends(get_db)):
    return user.create_admin(admin, db)