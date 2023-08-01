#!/bin/python3

# Stop or start instances based on tag: dev. 
# Script should typically be run as a cronjob on a schedule, i.e. stop at 7pm every evening mon-fri, and start again at 7am. 
# For all of sat/sun, the instances should remain off.
# 

import boto3

client = boto3.client('ec2')


# add logic for sys argv - 'stop' or 'start' on execution of script from cmdline


# get instanceIDs/Names where tag eq dev
response = client.describe.instances(
 
)

# add instanceIDs and Names to an array


# for each instanceID in array, stop or start instances based on sys argv


# print list of instanceIDs/Name that were stopped or started