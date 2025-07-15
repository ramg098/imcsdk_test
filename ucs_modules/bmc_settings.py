"""BMC network configuration utilities for UCS."""
from ucsmsdk.ucshandle import UcsHandle
from imc_modules.utils import validate_sdk_method

query_file, query_line = validate_sdk_method(UcsHandle.query_classid)


def get_mgmt_interfaces(handle):
    """Return management interface objects."""
    return handle.query_classid("mgmtIf")
