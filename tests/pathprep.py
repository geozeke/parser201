"""Prepare `sys.path` for imports.

This module adds the package directory to `sys.path` so that the
Parser201 class can be imported for testing.
"""

import sys
from pathlib import Path

p = Path(__file__).resolve().parent.parent/'src/parser201'
sys.path.append(str(p))
