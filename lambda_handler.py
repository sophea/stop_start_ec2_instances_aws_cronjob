import json
import boto3
import os

#region = "ap-southeast-1"
region = os.getenv('REGION')
ec2 = boto3.client("ec2", region_name=region)

def get_ec2_instance_ids(project, state):
    #print(project + ',' + state)
    ec2 = boto3.client("ec2", region_name=region)
    filters = [
        { 'Name' : "tag:project",
    	  'Values' : [project]
        },{ 'Name' : "instance-state-name",
    	  'Values' : [state]
    	}
    ]
    ##instances with tag and running state
    response = ec2.describe_instances(Filters=filters)
    #print(response)
    instancelist = []
    for reservation in (response["Reservations"]):
        for instance in reservation["Instances"]:
            instancelist.append(instance["InstanceId"])
    return instancelist 

### stop ec2 instances
def stop_ec2_instances(project):
	instance_ids = get_ec2_instance_ids(project, 'running')
	#print(instance_ids)
	ec2.stop_instances(InstanceIds=instance_ids)
	print ("stopped your instances: " + str(instance_ids))
	return "stopped:OK"

### stop ec2 instances
def start_ec2_instances(project):
    instance_ids = get_ec2_instance_ids(project, 'stopped')
    ec2.start_instances(InstanceIds=instance_ids)
    print ("started your instances: " + str(instance_ids))
    return "started:OK"

def lambda_handler(event, context):
    
    print(event)
    #instances = ['i-07f7c4e73af277834']

    project = event.get('project')
    action = event.get('action')
    if ('stop' == action):
        stop_ec2_instances(project)
		
    elif (action == 'start'):
	    print('start action')
	    start_ec2_instances(project)

    return {
        'statusCode': 200,
        'body': json.dumps('success')
    }
