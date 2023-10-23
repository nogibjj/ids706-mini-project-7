import pytest
from my_tool import database

def test_create_tables():
    database.create_tables()

def test_insert_sample_data():
    database.insert_sample_data()
