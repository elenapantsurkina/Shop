

from src.smartphone import Smartphone


def test_smartphone_init(smartphone2):
    assert smartphone2.name == "Iphone 15"
    assert smartphone2.description == "512GB, Gray space"
    assert smartphone2.price == 210000.0
    assert smartphone2.quantity == 8
    assert smartphone2.efficiency == 98.2
    assert smartphone2.model == "15"
    assert smartphone2.memory == 512
    assert smartphone2.color == "Gray space"


def test_smartphone_sum(smartphone1, smartphone2):
    assert smartphone1 + smartphone2 == 2580000.0
