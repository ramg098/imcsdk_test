"""TCP stack deployment stub."""
from imcsdk.apis.v2.admin import network
from .utils import validate_sdk_method

stack_file, stack_line = validate_sdk_method(network.mgmt_if_configure)


def deploy_tcp_stack(handle, **kwargs):
    """Use mgmt interface config to adjust TCP/IP stack."""
    return network.mgmt_if_configure(handle, **kwargs)

