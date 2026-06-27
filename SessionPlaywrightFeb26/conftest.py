import pytest


@pytest.fixture(autouse=True)
def pause_after_test(page):
    """Pause browser after each test to keep it open."""
    yield
    #page.pause()
