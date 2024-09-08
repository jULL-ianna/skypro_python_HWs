import pytest
from StringUtils import StringUtils

utils = StringUtils()

#capitilize
@pytest.mark.parametrize("in_str, expect_out", [
        ("world", "World"),
        ("мир, труд", "Мир, труд"),
        ("2024", "2024"),

        ("&?", "&?"),
        ("", ""),
        (" ", " ")
])
def test_capitilize(in_str, expect_out):
        assert utils.capitilize(in_str) == expect_out



#trim
@pytest.mark.parametrize("in_str, expect_out", [
        (" world", "world"),
        (" мир, труд ", "мир, труд "),

        ("2024", "2024"),
])
def test_trim(in_str, expect_out):
        assert utils.trim(in_str) == expect_out
@pytest.mark.xfail()
def test_trim_num_input():
        assert utils.trim(2023) == "2023"



#to_list
@pytest.mark.parametrize("string, delimeter, result", [
        ("1,2,3,4", ",", ["1", "2", "3", "4"]),
        ("мир!труд!май", "!", ["мир", "труд", "май"]),

        ("a,b,cd", None, ["a", "b", "cd"])
])
def test_to_list(string, delimeter, result):
        if delimeter is None:
            res = utils.to_list(string)
        else:
            res = utils.to_list(string, delimeter)    
        assert res == result



#contains
@pytest.mark.parametrize("string, symbol, result", [
    ("Черный", "й", True),
    ("world", "l", True),
    ("20214", "1", True),

    ("Черный", "ч", False),
    ("cat", "1", False)
])
def test_contains(string, symbol, result):
    res = utils.contains(string, symbol)
    assert res == result



#delete_symbol
@pytest.mark.parametrize("string, symbol, result", [
    ("олень", "о", "лень"),
    ("20124", "1", "2024"),
    ("так же", " ", "также"),

    ("мороженое", "", "мороженое"),

])
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result



#starts_with
@pytest.mark.parametrize("string, symbol, result", [
    ("Черный", "Ч", True),
    ("world", "w", True),
    ("2024", "2", True),

    ("Черный", "ч", False),
    ("cat", "1", False),
    (" dog", "d", False)
])
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result



#end_with
@pytest.mark.parametrize("string, symbol, result", [
    ("Черный", "й", True),
    ("world", "d", True),
    ("2024", "4", True),

    ("Черный", "ч", False),
    ("cat", "1", False),
    (" dog", "d", False)
])
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result



#is_empty
@pytest.mark.parametrize("str, result", [
    ("  ", True),
    ("", True),

    ("cat", False),
    ("2024", False),
    ("!!!", False)
])
def test_is_empty(str, result):
    res = utils.is_empty(str)
    assert res == result



#list_to_string
@pytest.mark.parametrize("lst, joiner, result", [
    (["c", "a", "t"], ",", "c,a,t"),
    ([2, 0, 2, 4], ",", "2,0,2,4"),
    (["по", "другому"], "-", "по-другому"),

    ([], "!", ""),
    ([], None, ""),
    ([], "dog", "")
])
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result