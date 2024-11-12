from playwright.sync_api import sync_playwright
import pytest
import sys
import time

def test_run():
    # Initialize the browser in headed mode
    with sync_playwright() as p:
        browser = p.webkit.launch(
            headless=False,  # Force headed mode
            args=[]
        )
        context = browser.new_context()
        page = context.new_page()
        
        try:
            # Navigate and perform test actions
            page.goto("https://example.com")
            # Wait to see the page
            time.sleep(2)  # Gives us time to see the browser
            
            # Take a screenshot
            page.screenshot(path="test-results/test.png")
            
            # Do some visible actions
            page.get_by_role("heading", name="Example Domain").highlight()
            time.sleep(1)
            
            # Click somewhere
            page.click("body")
            time.sleep(1)
            
        finally:
            context.close()
            browser.close()

if __name__ == "__main__":
    run_test()
