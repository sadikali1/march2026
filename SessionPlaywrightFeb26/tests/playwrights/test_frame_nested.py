from playwright.sync_api import Page


def test_nested_frames(page: Page):
	"""Navigate to nested frames page and verify main, parent and child texts."""
	page.goto("https://demoqa.com/nestedframes")

	# main context header
	main_header = page.locator("h1").text_content()
	print("Main header:", main_header)
	assert "Nested Frames" in main_header

	# parent frame text
	parent_text = page.frame_locator("iframe").locator("body").text_content()
	print("Parent frame text:", parent_text)
	assert "Parent" in parent_text

	# child frame (inside the first/parent frame)
	child_text = page.frame_locator("iframe").nth(0).frame_locator("iframe").locator("body").text_content()
	print("Child frame text:", child_text)
	assert "Child" in child_text

