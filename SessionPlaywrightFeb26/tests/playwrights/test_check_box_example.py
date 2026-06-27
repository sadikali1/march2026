from turtle import delay

from playwright.sync_api import Page, expect
import pytest

@pytest.mark.regression
@pytest.mark.smoke
def test_demoqa_checkbox_home(page: Page):
    page.goto("https://demoqa.com/checkbox")

    home_checkbox = page.locator("//span[@aria-label='Select Home']")
    expect(home_checkbox).to_be_visible(timeout=10000)

    # Verify checkbox is not selected before clicking.
    expect(home_checkbox).to_have_attribute("aria-checked", "false")

    # Click the Home checkbox.
    home_checkbox.click()

    # Verify the checkbox is selected after clicking.
    expect(home_checkbox).to_have_attribute("aria-checked", "true", timeout=10000)


def test_demoqa_radio_yes_selected(page: Page):
    page.goto("https://demoqa.com/radio-button")

    yes_radio = page.locator("//input[@id='yesRadio']")
    expect(yes_radio).to_be_visible(timeout=10000)

    # Verify radio button is not selected before clicking.
    expect(yes_radio).not_to_be_checked()

    # Click the radio button.
    yes_radio.click()

    # Verify the radio button is selected after clicking.
    expect(yes_radio).to_be_checked(timeout=10000)
    delay(5000)

