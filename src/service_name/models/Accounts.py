from pydantic import BaseModel
from typing import Optional, List

from .MongoBaseModel import MongoBaseModel

class AccountBase(BaseModel):
    account_id: int
    limit: float
    products: List[str] = []

class AccountCreate(AccountBase):
    """
    POST validation here
    """
    pass

class AccountUpdate(BaseModel):
    """
    PATCH validation here
    """
    limit: Optional[float] = None
    products: Optional[List[str]] = None

class AccountView(AccountBase, MongoBaseModel):
    """
    GET validation here
    """
    pass