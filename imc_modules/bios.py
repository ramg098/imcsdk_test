"""BIOS configuration helpers."""
from imcsdk.apis.server import bios
from .utils import validate_sdk_method

backup_file, backup_line = validate_sdk_method(bios.bios_profile_backup_running)


def backup_running(handle, server_id=1):
    return bios.bios_profile_backup_running(handle, server_id=server_id)

