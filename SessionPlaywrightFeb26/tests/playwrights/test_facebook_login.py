import os
from playwright.sync_api import Page, expect
import pytest

@pytest.mark.smoke
def test_facebook_login(page: Page):
    fb_email = "sdsfds"
    fb_password = "test111"

    if not fb_email or not fb_password:
        raise ValueError(
            "Set FB_EMAIL and FB_PASSWORD environment variables before running the test."
        )

    page.goto("https://www.facebook.com/login")

    page.fill('input[name="email"]', fb_email)
    page.fill('input[name="pass"]', fb_password)
    page.click('button[name="login"]')

    # Wait for a page element that appears after successful login.
    expect(page.get_by_text("Create post")).to_be_visible(timeout=20000)
    expect(page).to_have_url(lambda url: "facebook.com" in url)


# Browser (chrome, firefox, edge) 
# Context (incognito/private)
# Page (tab/window)