import re
from playwright.sync_api import Page, expect


def test_facebook_signup_form(page: Page):
    page.goto("https://www.facebook.com/")

    # Open the signup modal.
    page.locator('//a[@aria-label="Create new account"]').click()

    # Wait for the signup form to appear.
    expect(page.locator("//label[text()='First name']/../input")).to_be_visible(timeout=15000)

    page.fill("//label[text()='First name']/../input", "TestFirst")
    page.fill("//label[text()='Surname']/../input", "TestLast")

    
