"""Server inventory collection."""
from imcsdk.apis.v2.server import inventory
from .utils import validate_sdk_method

inventory_file, inventory_line = validate_sdk_method(inventory.inventory_get)


def collect_inventory(handle, component="all", file_format="json", file_name=None):
    return inventory.inventory_get(handle, component=component, file_format=file_format, file_name=file_name)

