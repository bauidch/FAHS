#!/usr/bin/python


DOCUMENTATION = '''
---
module: rename
short_description: Rename a simple file
version_added: "0.1"
options: 
    src: 
        description: 
            - Path from the orginal file 
        required: true
        default: null 
    dest: 
        description: 
            - Path with new of rename file
        required: true
        default: null
        
author: - "Lukas Bauer (@bauidch)"
'''

EXAMPLES = '''
- name: Rename a file
  rename:
    src: '/tmp/file1.old'
    dest: '/tmp/file1.new' 
  register: result

'''


from ansible.module_utils.basic import *
import os

def rename(data):
    org_path = data['src']
    new_path = data['dest']
    os.rename(org_path, new_path)

def main():

    fields = {
        "src": {"required": True, "type": "str"},
        "dest": {"required": True, "type": "str"},
    }

    module = AnsibleModule(argument_spec=fields)

    rename(module.params)
    module.exit_json(msg="Rename Sucessfull", changed=True, meta=module.params)
    module.fail_json(msg="Error by rename process", meta=module.params)

if __name__ == '__main__':
    main()