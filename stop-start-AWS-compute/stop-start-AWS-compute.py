#!/bin/python3

"""
Stop or start AWS ec2 instances based on tag: dev. 
Script should typically be run as a cronjob on a schedule, i.e. stop at 7pm every evening mon-fri, and start again at 7am. 
For all of sat/sun, the instances should remain off.

To execute script run:
$./stop-start-AWS-compute.py stop
or
$./stop-start-AWS-compute.py start
"""


import boto3
import sys
from pprint import pprint

client = boto3.client('ec2')

def main():
    stop_start_input = sys_argv()
    get_ec2_data(stop_start_input)


# add logic for sys argv - 'stop' or 'start' on execution of script from cmdline
def sys_argv():
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'start' or sys.argv[1] == 'stop':
            return sys.argv[1]
        
        else:
            print(f"Exiting script due to incorrect entry...\n'stop' or 'start' are the only valid entries...")
            sys.exit(1)

    if len(sys.argv) < 2:
        stop_start_prompt = input(f"Enter 'stop' or 'start':\n> ").lower()
        if stop_start_prompt == 'stop' or stop_start_prompt == 'start':
            return stop_start_prompt
        else:
            print(f"Exiting script due to incorrect entry...\n'stop' or 'start' are the only valid entries...")
            sys.exit(1)            


# get instanceIDs/Names where tag eq dev
def get_ec2_data(stop_start_input, Token=None):
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

        #print(f"{InstanceId} : {InstanceName}")
        stop_start_ec2s(InstanceId, InstanceName, stop_start_input)


# for each instanceID, stop or start instances based on sys argv
def stop_start_ec2s(InstanceId, InstanceName, stop_start_input):
    if stop_start_input == 'stop':
        stop_response = client.stop_instances(
            InstanceIds=[
            InstanceId,
            ]
        )
        pprint(stop_response['StoppingInstances'])
        
    if stop_start_input == 'start':
        start_response = client.start_instances(
            InstanceIds=[
            InstanceId,
            ]
        )
        pprint(start_response)

    # print list of instanceIDs/Names that were stopped or started
    print(f"Instance={InstanceId}:{InstanceName}\n")


main()



