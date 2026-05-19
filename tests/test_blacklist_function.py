import pytest
from src.manager import Manager

def test_blacklist_function():
    manager = Manager()
    blacklist = manager.get_blacklist()
    assert blacklist == ['Jan Kowalski', 'Mariusz czarny']