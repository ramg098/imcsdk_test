"""NIC support utilities."""
from ucsmsdk.ucshandle import UcsHandle
from imc_modules.utils import validate_sdk_method

query_file, query_line = validate_sdk_method(UcsHandle.query_classid)


def get_adaptors(handle):
    """Return adaptorUnit objects."""
    return handle.query_classid("adaptorUnit")
