import mcp


def test_helloWorld():
    assert 1 == 1


def test_mcp():
    m = mcp.mcp()
    assert m.this_returns_one() == 1