"""Automatic discovery of UCS Manager servers in a given IP range."""
from ucsmsdk.ucshandle import UcsHandle
from modules.utils import validate_sdk_method

login_file, login_line = validate_sdk_method(UcsHandle.login)


def discover_hosts(ips, username, password):
    """Attempt to login to each IP and return a list of handles."""
    handles = []
    for ip in ips:
        handle = UcsHandle(ip, username, password)
        try:
            handle.login()
            handles.append(handle)
        except Exception:
            pass
    return handles
