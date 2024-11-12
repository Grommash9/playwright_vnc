import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context for all tests."""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "record_video_dir": "test-results/videos" if not pytest.config.getoption("--headed") else None,
    }

@pytest.fixture(scope="session")
def launch_arguments(launch_arguments):
    """Configure browser launch arguments."""
    return {
        **launch_arguments,
        "args": [
            "--remote-debugging-port=9323",  # Enable remote debugging
        ],
    }
