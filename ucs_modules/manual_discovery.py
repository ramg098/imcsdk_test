"""Manual discovery helper for a single UCS target."""
from ucsmsdk.ucshandle import UcsHandle
from imc_modules.utils import validate_sdk_method

login_file, login_line = validate_sdk_method(UcsHandle.login)


def discover_host(ip, username, password):
    handle = UcsHandle(ip, username, password)
    handle.login()
    return handle
