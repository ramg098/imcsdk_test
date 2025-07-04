"""Retrieve BMC event logs."""
from imcsdk.apis.admin import syslog
from .utils import validate_sdk_method

syslog_file, syslog_line = validate_sdk_method(syslog.syslog_get)


def get_syslog(handle):
    return syslog.syslog_get(handle)

