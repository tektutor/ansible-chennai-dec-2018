#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def sayHello(msg):
    return 'Hello ' + str(msg)

def main():    
    module = AnsibleModule(
        argument_spec=dict(
            message=dict(type='str', required='yes')
        )
    )

    msg = module.params['message'] 

    response = sayHello( msg )
    module.exit_json(meta=response, changed='True')

main()
