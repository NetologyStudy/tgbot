from datetime import date, time

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from database import Base



class UserOrm(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(16))
    chat_id: Mapped[int]
    day: Mapped[date]
    time_from: Mapped[time]
    time_to: Mapped[time]