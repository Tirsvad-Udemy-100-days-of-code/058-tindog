"""@file test_constants.py
@brief Tests for the shared constants.
"""

from tindog import __version__, constants


def test_package_name_is_tindog() -> None:
    assert constants.PACKAGE_NAME == "tindog"


def test_default_host_is_loopback_only() -> None:
    assert constants.DEFAULT_HOST == "127.0.0.1"


def test_default_port_is_unprivileged() -> None:
    assert 1024 <= constants.DEFAULT_PORT <= 65535


def test_site_dir_is_inside_the_package() -> None:
    assert constants.SITE_DIR.name == constants.SITE_DIR_NAME
    assert constants.SITE_DIR.parent.name == constants.PACKAGE_NAME


def test_version_is_declared() -> None:
    assert __version__ == "0.1.0"
