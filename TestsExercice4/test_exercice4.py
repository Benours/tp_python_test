from context import src

def test_index_minimum():
    t = [4, 2, 6, 1, 8, 3]
    d = 1
    f = 5
    assert src.index_minimum(t, d, f) == 3

def test_tri_a_bulle():
    t = [4, 2, 6, 1, 8, 3]
    assert src.tri_a_bulles(t) == [1, 2, 3, 4, 6, 8]

def test_find_in_sort_tab():
    t = [1, 2, 4, 8, 16, 32]
    e = 4
    assert src.find_in_sort_tab(t, e) == 2

def test_find_dichotomique():
    t = [1, 2, 4, 8, 16, 32]
    e = 4
    assert src.find_dichotomique(t, e) == 2

def test_insertion():
    t = [1, 2, 4, 8, 16, 32]
    e = 3
    assert src.insertion(e, t, len(t)) == [1, 2, 3, 4, 8, 16]

def test_tri_extraction():
    t = [4, 2, 6, 1, 8, 3]
    assert src.tri_extraction(t) == [1, 2, 3, 4, 6, 8]

def test_tri_insertion():
    t = [4, 2, 6, 1, 8, 3]
    assert src.tri_insertion(t) == [1, 2, 3, 4, 6, 8]