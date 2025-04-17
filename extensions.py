import os
import subprocess  # noqa: S404
from datetime import date

from jinja2.ext import Extension


def git_user_name(default: str) -> str:
    return subprocess.getoutput("git config user.name").strip() or default  # noqa: S605,S607


def git_user_email(default: str) -> str:
    return subprocess.getoutput("git config user.email").strip() or default  # noqa: S605,S607


def are_tags_gpg_signed(default: bool = False) -> bool:
    value = subprocess.getoutput("git config --bool tag.gpgsign").strip().lower()  # noqa: S605,S607
    if value in ["true", "1", "yes", "on"]:
        return True
    elif value in ["false", "0", "no", "off"]:
        return False
    return default


class GitExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["git_user_name"] = git_user_name
        environment.filters["git_user_email"] = git_user_email
        environment.filters["are_tags_gpg_signed"] = are_tags_gpg_signed


class CurrentYearExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.globals["current_year"] = date.today().year


class UserUIDGUIDExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.globals["uid"] = os.getuid()
        environment.globals["gid"] = os.getgid()
