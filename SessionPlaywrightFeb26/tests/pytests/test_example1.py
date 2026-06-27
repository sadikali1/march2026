import os
import pytest


def test_ition():
	assert 1 + 1 == 2


@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (2, 1, 5),
    (5, 5, 10)
])


def test_add(a, b, result):
    assert a + b == result

@pytest.fixture
def sample_list():
	return [1, 2, 3]


def test_fixture_len(sample_list):
	assert len(sample_list) == 3



@pytest.mark.xfail(reason="demonstration of xfail", strict=False)
def test_expected_failure():
	assert False


@pytest.mark.skip(reason="demonstration of skip")
def test_skipped():
	assert False

