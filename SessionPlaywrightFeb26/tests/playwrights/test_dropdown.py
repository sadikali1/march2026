from playwright.sync_api import Page, expect


def test_dropdown_selection(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")

    # Locate the dropdown using the XPath selector.
    dropdown = page.locator("//select[@id='dropdown']")

    # Verify the dropdown is visible.
    expect(dropdown).to_be_visible()

    # Select option by value.
    dropdown.select_option("1")
    expect(dropdown).to_have_value("1")

    # Select option by label.
    dropdown.select_option(label="Option 2")
    expect(dropdown).to_have_value("2")


def test_dropdown_all_options(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")

    dropdown = page.locator("//select[@id='dropdown']")

    # Get all available options.
    options = dropdown.locator("option").all()

    # Skip the "Please select an option" placeholder and test other options.
    for option in options[1:]:
        value = option.get_attribute("value")
        label = option.inner_text()
        
        dropdown.select_option(value)
        expect(dropdown).to_have_value(value)
