from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from server.config.database import Base
from server.model.user import User
from fastapi import HTTPException, status
from server.model.admin import Admin
from server.config.password_hashing import (
    get_password_hash,
    verify_password
)
def get_user(user_id: int, db):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

def get_admin(admin_id: int, db):
    admin = db.query(Admin).filter(Admin.id == admin_id).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Admin not found")
    return admin

    
def create_user(user: User, db):
    user.password = get_password_hash(user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_admin(admin: Admin, db):
    admin.password = get_password_hash(admin.password)
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin