"""UCS management utilities."""
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.org.OrgOrg import OrgOrg
from modules.utils import validate_sdk_method

add_file, add_line = validate_sdk_method(UcsHandle.add_mo)
commit_file, commit_line = validate_sdk_method(UcsHandle.commit)


def create_org(handle, name, parent_dn="org-root"):
    org = OrgOrg(parent_mo_or_dn=parent_dn, name=name)
    handle.add_mo(org)
    handle.commit()
    return org
