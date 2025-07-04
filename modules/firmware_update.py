"""Firmware update helpers."""
from imcsdk.utils import imcfirmwareinstall as fw
from .utils import validate_sdk_method

update_file, update_line = validate_sdk_method(fw.firmware_update)


def update_firmware(handle, remote_share, share_type, remote_ip, **kwargs):
    """Trigger firmware update using HUU image."""
    return fw.firmware_update(handle, remote_share, share_type, remote_ip, **kwargs)

