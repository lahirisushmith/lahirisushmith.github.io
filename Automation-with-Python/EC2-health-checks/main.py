import boto3

ec2_client = boto3.client('ec2')

statuses = ec2_client.describe_instance_status()
for status in statuses['InstanceStatuses']:
    ins_status = status['InstanceStatus']['Status']
    sys_status = status['SystemStatus']['Status']
    state = status['InstanceState']['Name']
    print(f"Instance {status['InstanceId']} is {state} with instance status {ins_status} and system status is {sys_status}")

reservations = ec2_client.describe_instances()
for reservation in reservations['Reservations']:
    instances = (reservation['Instances'])
    for instance in instances:
        print(instance['State']['Name'])
