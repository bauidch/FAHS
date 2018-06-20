#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type


def check_pacemaker_resources(value, checkdict):
    if 'group' in value.keys():
        if value['group']['name'] in checkdict.keys():
            if value['id'] in checkdict[value['group']['name']]:
                return True
            else:
                return False
        else:
            return False
    else:
        if value['id'] in checkdict['nogroup']:
            return True
        else:
            return False


# ---- Ansible filters ----
class FilterModule(object):
    ''' Ansible filters for checking target pacemaker configuration '''

    # --------------------------------
    def filters(self):
        # --------------------------------
        return {
            'check_pacemaker_resources': check_pacemaker_resources
        }
