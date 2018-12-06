#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def add(val1,val2):
    return val1 + val2 

def main():    
    module = AnsibleModule(
        argument_spec=dict(
            firstInput=dict(type='float', required='yes'),
            secondInput=dict(type='float', required='yes')
        )
    )

    value1 = module.params['firstInput'] 
    value2 = module.params['secondInput'] 

    response = add( value1, value2 )
    #module.exit_json(meta=response, changed='False')
    module.exit_json(meta=response, changed='True')
    #module.fail_json(msg="Fatal error occurred")


main()
