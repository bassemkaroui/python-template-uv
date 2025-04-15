#!/usr/bin/env python
import sys
from pathlib import Path

try:
    from commitizen.cz.utils import get_backup_file_path
except ImportError as error:
    print(f"could not import commitizen:\n{error}")
    sys.exit(1)


def post_commit() -> None:
    backup_file = Path(get_backup_file_path())

    # remove backup file if it exists
    if backup_file.is_file():
        backup_file.unlink()


if __name__ == "__main__":
    post_commit()
    sys.exit(0)
