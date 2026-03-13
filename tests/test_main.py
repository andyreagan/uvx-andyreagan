"""Tests for the andyreagan package."""

import subprocess
import sys


import andyreagan
from andyreagan.main import main


def test_version_string():
    """__version__ is a non-empty string in semver-ish format."""
    assert isinstance(andyreagan.__version__, str)
    assert len(andyreagan.__version__) > 0
    parts = andyreagan.__version__.split(".")
    assert len(parts) == 3, f"Expected 3 version parts, got: {andyreagan.__version__}"


def test_main_prints_resume(capsys):
    """main() prints resume content to stdout."""
    main()
    captured = capsys.readouterr()
    assert "ANDY REAGAN" in captured.out
    assert captured.err == ""


def test_main_contains_key_sections(capsys):
    """Resume output includes the expected section headings."""
    main()
    output = capsys.readouterr().out
    for section in ("EXPERIENCE", "EDUCATION", "RESEARCH", "PERSONAL"):
        assert section in output, f"Missing section: {section}"


def test_main_contains_contact_info(capsys):
    """Resume output includes GitHub contact link."""
    main()
    output = capsys.readouterr().out
    assert "github.com/andyreagan" in output


def test_cli_entry_point():
    """The installed `andyreagan` console script runs and exits 0."""
    result = subprocess.run(
        [sys.executable, "-m", "andyreagan.main"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "ANDY REAGAN" in result.stdout
    assert result.stderr == ""


def test_cli_via_entry_point_script():
    """Running `python -c 'from andyreagan.main import main; main()'` works."""
    result = subprocess.run(
        [sys.executable, "-c", "from andyreagan.main import main; main()"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "ANDY REAGAN" in result.stdout
