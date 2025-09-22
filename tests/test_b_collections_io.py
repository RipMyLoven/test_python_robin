import pytest
from src.b_collections_io import (
    unique_sorted, count_words, merge_dicts, find_max_pair, flatten,
    read_file, write_file, safe_get, top_n, chunk_list
)

# B-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

def test_unique_sorted_basic():
    """Test unikaalsete sorteeritud arvude funktsiooni."""
    assert unique_sorted([3,1,2,2,3]) == [1,2,3]
    assert unique_sorted([]) == []
    assert unique_sorted([5,5,5]) == [5]

def test_count_words_basic():
    """Test sõnade loendamise funktsiooni."""
    text = "tere tere tulemast koju"
    out = count_words(text)
    assert out == {"tere": 2, "tulemast": 1, "koju": 1}

def test_merge_dicts():
    assert merge_dicts({}, {}) == {}
    assert merge_dicts({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}
    assert merge_dicts({"a": 1}, {"a": 2}) == {"a": 2}

def test_find_max_pair():
    assert find_max_pair([1, 2, 3]) == (3, 1)
    assert find_max_pair([1, 3, 3]) == (3, 2)
    assert find_max_pair([5]) == (5, 1)

def test_flatten():
    assert flatten([]) == []
    assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten([[1], [2, 3], []]) == [1, 2, 3]

def test_safe_get():
    assert safe_get({"a": 1}, "a") == 1
    assert safe_get({"a": 1}, "b") == None
    assert safe_get({"a": 1}, "b", "default") == "default"

def test_top_n():
    assert top_n([3, 1, 4, 2], 2) == [4, 3]
    assert top_n([5, 5, 1], 2) == [5, 5]
    assert top_n([1], 1) == [1]

def test_chunk_list():
    assert chunk_list([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
    assert chunk_list([1, 2, 3], 2) == [[1, 2], [3]]
    assert chunk_list([], 2) == []

def test_write_file():
    assert write_file("test.txt", "hello") == 5
    assert write_file("test.txt", "") == 0
    assert write_file("test.txt", "test text") == 9

def test_read_file():
    write_file("test.txt", "hello world")
    assert read_file("test.txt") == "hello world"
    write_file("test.txt", "")
    assert read_file("test.txt") == ""
    write_file("test.txt", "line1\nline2")
    assert read_file("test.txt") == "line1\nline2"
