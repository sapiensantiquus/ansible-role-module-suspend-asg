#!/usr/bin/env python

import collections
from ansible import utils, errors
import json
import yaml
import sys
from ansible.module_utils.basic import *

try:
  import boto3
except ImportError:
  raise errors.AnsibleError(
    "Can't LOOKUP(cloudformation): module boto3 is not installed")

def main():
  module = AnsibleModule(
    argument_spec = dict(
      suspend_asg_name = dict(required=True, type='str'),
      suspend_asg_process_list = dict(required=True, type='list')
    )
  )

  asg_name = module.params.get('suspend_asg_name')
  process_list = module.params.get('suspend_asg_process_list')
  region = module.params.get('region')

  asg_client = boto3.client("autoscaling")
  asg_client.suspend_processes(AutoScalingGroupName=asg_name,ScalingProcesses=process_list)

  asgs = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])['AutoScalingGroups']

  if len(asgs) == 0:
    module.exit_json(
      Changed=False,
      Failed=True,
      msg=('Auto Scaling Group: {0} was not found!'.format(asg_name))
    )

  instance_ids = []
  for instance in asgs[0]['Instances']:
    instance_ids.append(instance['InstanceId'])

  result = dict(changed=False, failed=False)
  result['ansible_facts'] = { 'asg_instance_ids' : instance_ids }

  module.exit_json(**result)

main()
