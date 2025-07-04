"""Power control utilities using ucsmsdk."""
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.compute.ComputeRackUnit import ComputeRackUnit
from modules.utils import validate_sdk_method

set_file, set_line = validate_sdk_method(UcsHandle.set_mo)
commit_file, commit_line = validate_sdk_method(UcsHandle.commit)
query_file, query_line = validate_sdk_method(UcsHandle.query_dn)


def power_on(handle, dn):
    server = handle.query_dn(dn)
    server.admin_power = "admin-up"
    handle.set_mo(server)
    return handle.commit()


def power_off(handle, dn):
    server = handle.query_dn(dn)
    server.admin_power = "admin-down"
    handle.set_mo(server)
    return handle.commit()
