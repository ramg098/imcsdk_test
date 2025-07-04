"""Backup utilities using ucsmsdk."""
from ucsmsdk.utils import ucsbackup
from modules.utils import validate_sdk_method

backup_file, backup_line = validate_sdk_method(ucsbackup.backup_ucs)


def create_backup(handle, backup_type, file_dir, file_name, **kwargs):
    """Create and download a UCS backup."""
    return ucsbackup.backup_ucs(handle, backup_type, file_dir, file_name, **kwargs)
