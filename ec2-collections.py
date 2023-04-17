import boto3

ec2 = boto3.resource('ec2')

#comment out option 1 (filter all instances) or 2 (all instances in us-east-1c)
#for instance in ec2.instances.all():
for instance in ec2.instances.filter(Filters=[
    {
        'Name': 'availability-zone',
        'Values': ['us-east-1c']
    }]):
    print('Instance id is {} and instance type is {}'.format(instance.instance_id, instance.instance_type))