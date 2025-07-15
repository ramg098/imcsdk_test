"""Automatic discovery of Cisco IMC servers in a given IP range."""
from imcsdk.imchandle import ImcHandle
from .utils import validate_sdk_method

# validate that login method exists and capture its location
login_file, login_line = validate_sdk_method(ImcHandle.login)


def discover_hosts(ips, username, password):
    """Attempt to login to each IP and return a list of handles."""
    handles = []
    for ip in ips:
        handle = ImcHandle(ip, username, password)
        try:
            handle.login()
            handles.append(handle)
        except Exception:
            pass
    return handles

