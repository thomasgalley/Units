from nose.tools import assert_true
from Amount import*
def test_equalities():
    assert_true(Amount('length','meters',5)==Amount('length','kilometers',0.005))
    assert_true(Amount('time','seconds',60)==Amount('time','minutes',1))
