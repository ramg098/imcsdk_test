"""BIOS utilities for UCS servers."""
from ucsmsdk.ucshandle import UcsHandle
from modules.utils import validate_sdk_method

query_file, query_line = validate_sdk_method(UcsHandle.query_classid)


def get_bios_units(handle):
    """Return BIOS units via query_classid."""
    return handle.query_classid("biosUnit")
