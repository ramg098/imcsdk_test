"""Configuration backup helpers."""
from imcsdk.utils import imcbackup as bk
from .utils import validate_sdk_method

create_file, create_line = validate_sdk_method(bk.backup_create)
import_file, import_line = validate_sdk_method(bk.backup_import)


def create_backup(handle, remote_host, remote_file, protocol, username, password, passphrase, **kwargs):
    return bk.backup_create(handle, remote_host, remote_file, protocol, username, password, passphrase, **kwargs)


def import_backup(handle, remote_host, remote_file, protocol, username, password, passphrase, **kwargs):
    return bk.backup_import(handle, remote_host, remote_file, protocol, username, password, passphrase, **kwargs)

