"""Module for checking the functionality of the arduino-cli hook."""
from pathlib import Path

import pytest

from arduino_hooks.arduino_cli import ArduinoCLI


def test_constructor(arduino_cli: ArduinoCLI):
    """Check a normal creation of the object is set up as expected."""
    assert len(arduino_cli.args) == 2  # compile, and fqbn args
    assert len(arduino_cli.paths) == 1


def test_project_dir_arg():
    """Checks passing a project directory argument to the hook works."""
    arduino_cli = ArduinoCLI(
        ["arduino-cli", "--fqbn=arduino:avr:nano", "--project-dir=ValidSketch/"]
    )
    assert len(arduino_cli.args) == 2  # verify no residual
    assert arduino_cli.run() is None


def test_syntax_error_fails(arduino_cli: ArduinoCLI):
    """Check uncompilable code throws errors correctly."""
    arduino_cli.paths[0] = Path("WarningSketch/").resolve().__str__()
    with pytest.raises(SystemExit):
        assert arduino_cli.run()
