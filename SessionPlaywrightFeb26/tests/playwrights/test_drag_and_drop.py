from playwright.sync_api import Page
import time


def test_drag_and_drop(page: Page):
	"""Navigate to droppable page, perform drag and drop and verify result."""
	page.goto("https://demoqa.com/droppable")

	draggable = page.locator("#draggable")
	droppable = page.locator("div[id='simpleDropContainer'] > #droppable")

	# Perform drag and drop
	draggable.drag_to(droppable)

	# wait for any animation/processing
	time.sleep(2)

	# Verify the droppable text changed to 'Dropped!'
	droppable_text = droppable.text_content()
	assert "Dropped!" == droppable_text

