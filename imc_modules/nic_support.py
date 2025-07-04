"""NIC card related helpers."""
from imcsdk.apis.v2.server import adaptor
from .utils import validate_sdk_method

adaptor_file, adaptor_line = validate_sdk_method(adaptor.adaptor_unit_get)


def get_nic(handle, slot, server_id=1):
    return adaptor.adaptor_unit_get(handle, adaptor_slot=slot, server_id=server_id)

