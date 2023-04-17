import boto3

#Comment Out Option 1 (Find running instances) or option 2 (Find instances tagged 'prod')

#Option 1
#client = boto3.client('ec2')
#resp = client.describe_instances(Filters=[{
#    'Name': 'instance-state-name',
#    'Values': ['running']
#}])

#Option 2
client = boto3.client('ec2')
resp = client.describe_instances(Filters=[{
    'Name': 'tag:ENV',
    'Values': ['Dev']
}])

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print("InstanceId is {} ",format(instance['InstanceId']))