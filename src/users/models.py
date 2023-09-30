from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    firstName: Mapped[str]
    lastName: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
