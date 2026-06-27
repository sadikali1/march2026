from playwright.sync_api import Browser


def test_multiple_pages_same_context(browser: Browser):
    """Create multiple pages in a single browser context and interact with them."""
    context = browser.new_context()
    page1 = context.new_page()
    page1.goto("https://demoqa.com/buttons")

    page2 = context.new_page()
    page2.goto("https://demoqa.com/frames")

    # simple verifications on each page
    assert "Buttons" in page1.locator("h1").text_content()
    header = page2.locator("h1").text_content()
    assert "Frames" in header

    page1.close()
    page2.close()
    context.close()


def test_multiple_contexts_and_pages(browser: Browser):
    """Create two separate contexts (isolated sessions) each with its own page."""
    ctx1 = browser.new_context()
    p1 = ctx1.new_page()
    p1.goto("https://demoqa.com/webtables")

    ctx2 = browser.new_context()
    p2 = ctx2.new_page()
    p2.goto("https://demoqa.com/droppable")

    assert "Web Tables" in p1.locator("h1").text_content()
    assert "Droppable" in p2.locator("h1").text_content()

    ctx1.close()
    ctx2.close()

