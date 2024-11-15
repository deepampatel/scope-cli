from scope.dir_size import get_size

def test_get_size():
    size = get_size(".")
    assert size > 0
