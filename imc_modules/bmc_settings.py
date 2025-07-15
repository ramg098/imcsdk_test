"""BMC network configuration utilities."""
from imcsdk.apis.v2.admin import network
from .utils import validate_sdk_method

mgmt_file, mgmt_line = validate_sdk_method(network.mgmt_if_configure)
block_file, block_line = validate_sdk_method(network.ip_blocking_enable)


def configure_network(handle, **kwargs):
    """Configure management interface settings."""
    return network.mgmt_if_configure(handle, **kwargs)


def enable_ip_blocking(handle, **kwargs):
    """Enable IP blocking on the BMC."""
    return network.ip_blocking_enable(handle, **kwargs)

