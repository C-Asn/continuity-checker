"""Double-click this file to open the GUI without a terminal window."""
from pathlib import Path
import runpy

runpy.run_path(str(Path(__file__).with_name("continuity_checker.py")), run_name="__main__")
