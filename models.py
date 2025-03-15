from sqlalchemy import Column, Integer, String, ForeignKey, Text, TIMESTAMP, UniqueConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    bookmarks = relationship("Bookmark", back_populates="user")

class Bookmark(Base):
    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    resource_id = Column(String, nullable=False)
    resource_type = Column(String, nullable=False)  # 'github_repo', 'blog', 'research_paper'
    title = Column(Text, nullable=False)
    description = Column(Text)
    url = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    user = relationship("User", back_populates="bookmarks")

    __table_args__ = (UniqueConstraint("user_id", "resource_id", "resource_type", name="unique_bookmark"),)
