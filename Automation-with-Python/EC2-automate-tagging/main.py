import boto3

ec2_client_frankfurt = boto3.client('ec2', region_name="eu-central-1")
ec2_resource_frankfurt = boto3.resource('ec2', region_name="eu-central-1")
ec2_client_mumbai = boto3.client('ec2', region_name="eu-central-1")
ec2_resource_mumbai = boto3.resource('ec2', region_name="eu-central-1")


instance_ids_frankfurt = []
instance_ids_mumbai = []

reservations_frankfurt = ec2_client_frankfurt.describe_instances()['Reservations']
for res in reservations_frankfurt:
    instances = res['Instances']
    for ins in instances:
        instance_ids_frankfurt.append(ins['InstanceId'])

response = ec2.create_tags(
    Resources= instance_ids_frankfurt
    Tags=[
        {
            'Key': 'enviornment',
            'Value': 'prod'
        },
    ]
)
reservations_mumbai = ec2_client_mumbai.describe_instances()['Reservations']
for res in reservations_mumbai:
    instances = res['Instances']
    for ins in instances:
        instance_ids_mumbai.append(ins['InstanceId'])

response = ec2.create_tags(
    Resources= instance_ids_mumbai
    Tags=[
        {
            'Key': 'enviornment',
            'Value': 'dev'
        },
      ]
)
