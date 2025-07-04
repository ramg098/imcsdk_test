"""Power control utilities using imcsdk."""
from imcsdk.apis.server import serveractions as sa
from .utils import validate_sdk_method

power_up_file, power_up_line = validate_sdk_method(sa.server_power_up)
power_down_file, power_down_line = validate_sdk_method(sa.server_power_down)


def power_on(handle, server_id=1):
    return sa.server_power_up(handle, server_id=server_id)


def power_off(handle, server_id=1):
    return sa.server_power_down(handle, server_id=server_id)

