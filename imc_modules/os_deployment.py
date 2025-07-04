"""OS deployment utilities via virtual media."""
from imcsdk.apis.server import vmedia
from .utils import validate_sdk_method

enable_file, enable_line = validate_sdk_method(vmedia.vmedia_enable)
mount_file, mount_line = validate_sdk_method(vmedia.vmedia_mount_create)


def mount_iso(handle, volume_name, remote_share, remote_file, **kwargs):
    vmedia.vmedia_enable(handle)
    return vmedia.vmedia_mount_create(handle, volume_name, remote_share, remote_file, **kwargs)

