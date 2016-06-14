# ansible-role-module-suspend-asg

## Role Variables

| Variable        | Required           | Default  | Description |
| ---------------------------- |:----------------------------------------:| -----:| -------------------------------------------------------------------------:|
| suspend_asg_name | Yes |  | Name of the Auto Scaling group to suspend |
| suspend_asg_process_list | No |  Launch, Terminate, ReplaceUnhealthy, AZRebalance, ScheduledActions | List of Auto Scaling processes to suspend |
| suspend_asg_recovery_minutes | No | 3 | Number of minutes that system status check is allowed to fail before recovery |
