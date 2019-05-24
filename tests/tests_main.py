import pytest
from main import search
class Testmain:
    def test_type_error(self):
        with pytest.raises(TypeError):
            search('ololo',123)

    def test_empty(self):
        assert search([],"1") == []

    def test_one(self):
        assert search(sorted(["123","234","124"]), "12") == ["123","124"]

    def test_two(self):
        assert search(sorted(["123", "234", "124","2355", "235341658","752","72","237589"]), "23") == ["234", "235341658","2355","237589"]

    #doesn't work
    #@pytest.mark.randomize(spsiok=pytest.list_of(int,num_items=10),string="123")
    def test_quickcheck(self,spisok, string):
        result = search(sorted(spisok),string)
        for i in result:
            assert (str(i)[:len(string)]==string)
        assert (len(result) <= 10)