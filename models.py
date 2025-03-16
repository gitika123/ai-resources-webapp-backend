from sqlalchemy import Column, Integer, String, ForeignKey, Text, TIMESTAMP, UniqueConstraint, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)  # Add the is_admin field


    bookmarks = relationship("Bookmark", back_populates="user")
    uploads = relationship("CommunityUpload", back_populates="user")

class Bookmark(Base):
    __tablename__ = "bookmarks"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)  # URL of the bookmark
    title = Column(String)  # Title or name of the resource
    description = Column(String)  # Description of the resource
    resource_type = Column(String)  # Type of the resource (e.g., 'GitHub', 'Blog', 'Research Paper')
    user_id = Column(Integer, ForeignKey("users.id"))  # Foreign key to associate with user

    user = relationship("User", back_populates="bookmarks")  # Change 'owner' to 'user'

class CommunityUpload(Base):
    __tablename__ = "community_uploads"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    resource_type = Column(String, nullable=False)  # e.g., 'GitHub', 'Course', 'Blog', 'Research Paper'
    status = Column(String, default="pending_approval")  # Can be 'pending_approval' or 'approved'
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Foreign key to link the user
    url = Column(String, nullable=False)  # New field for storing URL

    user = relationship("User", back_populates="uploads")  # Fix the relationship here


