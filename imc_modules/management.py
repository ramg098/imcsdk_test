"""Switch, server and site management helpers."""
from imcsdk.imchandle import ImcHandle
from .utils import validate_sdk_method

query_file, query_line = validate_sdk_method(ImcHandle.query_classid)


def list_servers(handle):
    return handle.query_classid("ComputeRackUnit")


def list_switches(handle):
    return handle.query_classid("PciSwitch")

