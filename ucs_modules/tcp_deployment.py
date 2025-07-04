"""TCP stack deployment helpers."""
from ucsmsdk.ucshandle import UcsHandle
from imc_modules.utils import validate_sdk_method

query_file, query_line = validate_sdk_method(UcsHandle.query_classid)


def get_vnics(handle):
    """Return vNIC Ethernet interfaces."""
    return handle.query_classid("vnicEther")
