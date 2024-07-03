from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from shared.core.db.db_base import Base
from shared.core.config import DATABASE_URL

engine = create_engine(str(DATABASE_URL))
Base = declarative_base()

class DishModel(Base):
    __tablename__ = "dishes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    price = Column(Float)

class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    status = Column(String)
    created = Column(DateTime)

