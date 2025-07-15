"""Manual discovery - connect to a single Cisco IMC server."""
from imcsdk.imchandle import ImcHandle
from .utils import validate_sdk_method

login_file, login_line = validate_sdk_method(ImcHandle.login)


def connect(host, username, password):
    handle = ImcHandle(host, username, password)
    handle.login()
    return handle

