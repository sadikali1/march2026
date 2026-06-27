import os
from playwright.sync_api import Page


def test_full_page_screenshot(page: Page):
	"""Take a full-page screenshot and save to reports/full_page.png."""
	page.goto("https://demoqa.com")
	os.makedirs("reports", exist_ok=True)
	out = "reports/full_page.png"
	page.screenshot(path=out, full_page=True)
	assert os.path.exists(out)


def test_element_screenshot(page: Page):
	"""Take a screenshot of a specific element and save to reports/element.png."""
	page.goto("https://demoqa.com/buttons")
	os.makedirs("reports", exist_ok=True)
	elem = page.locator("h1").first
	out = "reports/element.png"
	elem.screenshot(path=out)
	assert os.path.exists(out)

