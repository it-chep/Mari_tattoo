from datetime import datetime
#
# from pydantic import BaseModel
# from typing import Optional, List
#
#
# class JobCreateSchema(BaseModel):
#     name: str
#     photo: str
#     description: Optional[str] = None
#     date: Optional[str] = None  # Должно быть datetime если вы используете дату и время
#     category_id: int
#     tags: Optional[List[str]] = None
#     price: Optional[int] = None
#
#
# class JobUpdate(BaseModel):
#     name: Optional[str] = None
#     photo: Optional[str] = None
#     description: Optional[str] = None
#     date: Optional[datetime] = None
#     category_id: Optional[int] = None
#     tags: Optional[List[str]] = None
#     price: Optional[int] = None
