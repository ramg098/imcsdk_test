"""Firmware update utilities."""
from ucsmsdk.ucsgenutils import upload_firmware
from imc_modules.utils import validate_sdk_method

upload_file, upload_line = validate_sdk_method(upload_firmware)


def upload(handle, uri, file_dir, file_name):
    """Upload firmware image to UCS."""
    return upload_firmware(driver=handle, uri=uri, file_dir=file_dir, file_name=file_name)
