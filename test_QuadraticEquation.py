# %%
import pytest
from QuadraticEquation import QuadraticEquation
from QuadraticEquation import ParamAZeroError, ConvertToFloatError


def test_QuadraticEquation_0():
    a, b, c, roots_true = 1, 0, 1, []
    eq = QuadraticEquation(a, b, c)
    roots = eq.solve()
    assert len(roots) == 0
    assert roots == roots_true


def test_QuadraticEquation_1():
    a, b, c, roots_true = 1, 0, -1, [-1, 1]
    eq = QuadraticEquation(a, b, c)
    roots = eq.solve()
    assert len(roots) == 2
    assert roots == roots_true


def test_QuadraticEquation_2():
    a, b, c, roots_true = 1, 2, 1, [-1, ]
    eq = QuadraticEquation(a, b, c)
    roots = eq.solve()
    assert len(roots) == 1
    assert roots == roots_true


def test_QuadraticEquation_3():
    a, b, c, roots_true = 0, 2, 1, None
    eq = QuadraticEquation(a, b, c)
    with pytest.raises(ParamAZeroError):
        eq.solve()


def test_QuadraticEquation_4():
    a, b, c, roots_true = 1, 2, 1.0000001, [-1, ]
    eq = QuadraticEquation(a, b, c)
    roots = eq.solve()
    assert len(roots) == 1
    assert roots == roots_true


@pytest.mark.parametrize("a, b, c", [('a', 2, 1),
                                     (1, 'b', 1),
                                     (1, 2, 'c'),
                                     ([1,], 2, 1),
                                     (1, [2,], 1),
                                     (1, 2, [1,]),
                                     ('a', 'b', ['c',]),])
def test_QuadraticEquation_5(a, b, c):
    eq = QuadraticEquation(a, b, c)
    with pytest.raises(ConvertToFloatError):
        eq.solve()
