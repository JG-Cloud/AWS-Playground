#!/bin/python3

# Stop or start instances based on tag: dev. 
# Script should typically be run as a cronjob on a schedule, i.e. stop at 7pm every evening mon-fri, and start again at 7am. 
# For all of sat/sun, the instances should remain off.
# 

import boto3
from pprint import pprint

client = boto3.client('ec2')


# add logic for sys argv - 'stop' or 'start' on execution of script from cmdline


# get instanceIDs/Names where tag eq dev
response = client.describe_instances(
    Filters=[
        {
            'Name' :'tag:env','Values': ['dev']
        }
    ]
)

Reservations = response['Reservations']

for output in Reservations:
    instances = output['Instances']

    
    # Get Instance Name / InstanceID from tag
    for instance in instances:
        InstanceId = instance['InstanceId']
        tags = instance['Tags']
        for tag in tags:
            if tag['Key'] == 'Name':
                InstanceName = tag['Value']

    print(f"{InstanceId} : {InstanceName}")

# add instanceIDs and Names to an array


# for each instanceID in array, stop or start instances based on sys argv


# print list of instanceIDs/Name that were stopped or started