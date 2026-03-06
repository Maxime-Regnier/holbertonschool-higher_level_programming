#!/usr/bin/python3
"""Module containing City class"""
from sqlalchemy import Column, Integer, String, ForeignKey  # type: ignore
from model_state import Base


class City(Base):
    """The City class"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)