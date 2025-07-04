"""Retrieve UCS event logs."""
from ucsmsdk.ucshandle import UcsHandle
from imc_modules.utils import validate_sdk_method

query_file, query_line = validate_sdk_method(UcsHandle.query_classid)


def get_events(handle):
    """Return eventInst objects."""
    return handle.query_classid("eventInst")
