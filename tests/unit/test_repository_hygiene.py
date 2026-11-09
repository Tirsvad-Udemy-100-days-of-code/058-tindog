"""@file test_repository_hygiene.py
@brief Checks that files which must not be published are not tracked by git.
"""

import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
FORBIDDEN_FRAGMENTS = (
    "goal images",
    "mashable.png",
    "bizinsider.png",
    "techcrunch.png",
    "tnw.png",
    "iphone.png",
    "dog-img.jpg",
    "solution.html",
)


@pytest.fixture(scope="module")
def tracked_files() -> list[str]:
    try:
        result = subprocess.run(
            ["git", "ls-files"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
            timeout=30,
        )
    except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        pytest.skip("git is unavailable or the folder is not a git work tree")
    return [line for line in result.stdout.splitlines() if line]


def test_no_tracked_file_is_a_zip_archive(tracked_files: list[str]) -> None:
    assert [p for p in tracked_files if p.lower().endswith(".zip")] == []


@pytest.mark.parametrize("fragment", FORBIDDEN_FRAGMENTS)
def test_no_tracked_path_contains_udemy_download_file(tracked_files: list[str], fragment: str) -> None:
    assert [p for p in tracked_files if fragment in p.lower()] == []


def test_env_file_is_not_tracked(tracked_files: list[str]) -> None:
    assert ".env" not in tracked_files
