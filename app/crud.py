from sqlalchemy.orm import Session
from . import models, schemas

def get_item(db: Session, item_id: int):
    return db.query(models.MonModel).filter(models.MonModel.id == item_id).first()

def create_item(db: Session, item: schemas.MonSchema):
    db_item = models.MonModel(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
