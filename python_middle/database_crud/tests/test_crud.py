import pytest

from funcs.crud import create, read_database, update, delete

test_db = {}

def test_create():
    create(test_db, 'test', 100)
    assert 'test' in test_db
    assert test_db['test'] == 100


def test_read_db():
    create(test_db, 'test_prod', 200)
    prod = read_database(test_db)
    assert 'test_prod' in prod
    product = read_database(test_db, 'test_prod')
    assert product == 200


def test_raises_error():
    with pytest.raises(ValueError) as exc:
        read_database(test_db, 'rgjlnwmfewlfewfq')

def test_update():
    create(test_db, 'test1', 300)
    update(test_db, 'test1', 400)
    assert test_db['test1'] == 400

def test_delete():
    create(test_db, 'test2', 500)
    create(test_db, 'test3', 600)
    delete(test_db, 'test2')
    assert 'test3' in test_db
    assert 'test2' not in test_db