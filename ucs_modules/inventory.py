"""Inventory helpers using ucsmsdk."""
from ucsmsdk.utils import inventory
from imc_modules.utils import validate_sdk_method

get_file, get_line = validate_sdk_method(inventory.get_inventory)


def get_system_inventory(handle, component="all", file_format="json", file_name=None):
    return inventory.get_inventory(handle, component=component, file_format=file_format, file_name=file_name)
