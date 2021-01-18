import pytest


class TestDemo():
    @pytest.mark.parametrize('a,b,c',[(1,2,3),(2,3,6),(4,6,10)])
    def test_add(self,a,b,c,per):
        result = per.add(a,b)
        assert result == c
