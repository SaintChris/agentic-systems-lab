#!/usr/bin/env python3
"""Configuration-safety checks for the public dashboard module."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dashboard import app

passed = 0
failed = 0


def assert_test(condition, name):
    global passed, failed
    if condition:
        print(f"  PASSED: {name}")
        passed += 1
    else:
        print(f"  FAILED: {name}")
        failed += 1


assert_test(
    os.path.basename(app.DASHBOARD_HTML) == "index.html",
    "Dashboard serves repository-local index.html by default",
)
assert_test(
    app.DASHBOARD_HOST == "127.0.0.1",
    "Dashboard binds to loopback by default",
)
assert_test(
    app.ALLOWED_DIRS == [],
    "Local file browsing is disabled unless DASHBOARD_DATA_ROOT is configured",
)
assert_test(
    app.is_allowed_path(os.path.expanduser("~")) is False,
    "Home directory is not implicitly exposed",
)
assert_test(
    app.API_BASE.startswith("http"),
    "Paperclip API base has an explicit URL scheme",
)

print(f"\nResults: {passed} passed, {failed} failed")
sys.exit(0 if failed == 0 else 1)
