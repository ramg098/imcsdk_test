"""OS deployment utilities via KVM."""
from ucsmsdk.utils import ucskvmlaunch
from modules.utils import validate_sdk_method

kvm_file, kvm_line = validate_sdk_method(ucskvmlaunch.ucs_kvm_launch)


def launch_kvm(handle, **kwargs):
    """Launch KVM for a server."""
    return ucskvmlaunch.ucs_kvm_launch(handle, **kwargs)
