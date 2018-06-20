#!/usr/bin/python

import xml.etree.ElementTree
from ansible.module_utils.basic import AnsibleModule
import os


def get_resources(cibroot, xmlresourcepath):
    resourcedict = {'nogroup': []}
    for element in cibroot.findall(xmlresourcepath):
        if element.tag == 'group':
            groupname = element.get('id')
            resourcedict[groupname] = []
            for resource in cibroot.findall(xmlresourcepath + 'group/'):
                resourcedict[groupname].append(resource.get('id'))
        elif element.tag == 'primitive':
            resourcedict['nogroup'].append(element.get('id'))
    return resourcedict


def get_constraints(cibroot, xmlconstraintpath):
    constraintlist = []
    for element in cibroot.findall(xmlconstraintpath):
        constraintlist.append(element.get('id'))
    return {'constraints': constraintlist}


def get_nodelist(cibroot, xmlnodepath):
    nodelist = []
    for element in cibroot.findall(xmlnodepath):
        nodelist.append(element.get('id'))
    return {'nodes': nodelist}


def main():
    module = AnsibleModule(
        argument_spec=dict(
            cibpath=dict(type='str', default='/var/lib/pacemaker/cib/cib.xml'),
            type=dict(type='str', required='true'),
        ),
        supports_check_mode=True
    )

    if not os.path.isfile(module.params['cibpath']):
        module.fail_json(msg="cib.xml not found in %s" % module.params['cibpath'])

    cibroot = xml.etree.ElementTree.parse(module.params['cibpath']).getroot()

    xmlresourcepath = './configuration/resources/'
    xmlconstraintpath = './configuration/constraints/'
    xmlnodepath = './configuration/nodes'

    kw = {}
    if module.params['type'] == 'resources':
        kw = get_resources(cibroot, xmlresourcepath)
    elif module.params['type'] == 'constraints':
        kw = get_constraints(cibroot, xmlconstraintpath)
    elif module.params['type'] == 'nodes':
        kw = get_nodelist(cibroot, xmlnodepath)
    else:
        module.fail_json(msg='Type %s not supported. ' % module.params['type'])

    module.exit_json(**kw)


if __name__ == '__main__':
    main()
