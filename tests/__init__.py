import sys
from pathlib import Path

sources = '/src/parser201'
P = str(Path(__file__).resolve().parent.parent) + sources
sys.path.append(P)

try:
    import classes
except Exception as e:
    print(e)
    sys.exit(1)
