"""Unit tests for interaction filtering logic."""

from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="attempt")


def test_filter_returns_all_when_item_id_is_none() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, None)
    assert result == interactions


def test_filter_returns_empty_for_empty_input() -> None:
    result = _filter_by_item_id([], 1)
    assert result == []


def test_filter_returns_interaction_with_matching_ids() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 1
    assert result[0].id == 1

def test_filter_by_item_id_returns_only_matching():
    interactions = [
        _make_log(1, 1, 1),
        _make_log(2, 1, 2),
        _make_log(3, 2, 1),
    ]
    filtered = _filter_by_item_id(interactions, 1)
    assert len(filtered) == 2
    assert all(log.item_id == 1 for log in filtered)
    assert {log.id for log in filtered} == {1, 3}
def test_filter_returns_empty_for_nonexistent_item_id():
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, 999)
    assert result == []

def test_filter_returns_all_when_multiple_matching_items():
    interactions = [
        _make_log(1, 1, 1),
        _make_log(2, 2, 1),
        _make_log(3, 3, 2),
        _make_log(4, 4, 1),
    ]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 3
    assert all(i.item_id == 1 for i in result)

def test_filter_preserves_original_order():
    interactions = [
        _make_log(5, 5, 2),
        _make_log(1, 1, 1),
        _make_log(3, 3, 2),
        _make_log(2, 2, 1),
    ]
    result = _filter_by_item_id(interactions, 1)
    assert [log.id for log in result] == [1, 2]

def test_filter_with_negative_item_id():
    interactions = [_make_log(1, 1, -1), _make_log(2, 2, 1)]
    result = _filter_by_item_id(interactions, -1)
    assert len(result) == 1
    assert result[0].id == 1

def test_filter_with_maximum_integer():
    import sys
    max_int = sys.maxsize
    interactions = [_make_log(1, 1, max_int), _make_log(2, 2, 1)]
    result = _filter_by_item_id(interactions, max_int)
    assert len(result) == 1
    assert result[0].id == 1
