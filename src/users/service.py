from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        firstName=user.firstName,
        lastName=user.lastName,
        email=user.email,
        phone=user.phone
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user: models.User):
    db.delete(user)
    db.commit()
    return user


def update_user(db: Session, user: models.User, user_data: schemas.UserUpdate):
    user.firstName = user_data.firstName
    user.lastName = user_data.lastName
    user.email = user_data.email
    user.phone = user_data.phone
    db.commit()
    return user



