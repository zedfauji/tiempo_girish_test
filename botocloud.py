#################################
#                               #
#Created By :- Girish Dudhwal   #
#                               #
#################################
import boto3
import sys
import yaml
from botocore.exceptions import ClientError
import argparse

'''
Usage: botocloud.py -i <InstanceType> -k <Pem File> -r <Region>
or 
botocloud.py -h for help
Argparser() function take cares of the arguments those are passed to the script. It will display script help.
'''
def ArgParser():
    parser = argparse.ArgumentParser(description="Create Instance through Cloudformation stack")
    parser.add_argument('-i','--instaType',type=str, default='t2.micro',required=True)
    parser.add_argument('-r','--region',type=str)
    parser.add_argument('-k','--pem',type=str,required=False)
    args = parser.parse_args()
    return args

''' Create Stack Cloud function, first check the Stack Name exists already
if not, then it will create boto3 connection for cloudformation,
Parameters provided through script cli , will configure region, instance type and 
pem file to be added to instance provisioning
'''
def creat_stack_cloud(config_yaml,instType,keyName,region):
    Stackname = 'demostack1'
    if isStackNameExists(Stackname,region):
        print("Stack Name Exists")
        exit()
    params = [
        {'ParameterKey': 'InstanceType', 'ParameterValue': str(instType)},
        {'ParameterKey': 'KeyName', 'ParameterValue': str(keyName)},
    ]

    try:
        cf_conn = boto3.client('cloudformation',region_name=region)
        output = cf_conn.create_stack(
            StackName='demostack1',
            TemplateBody=config_yaml,
            Parameters=params
        )
        print ("Stack Created with ARN",output['StackId'])
    except ClientError as err:
        print (err)
        print("Stack Already Exists")

'''
This Function check the Stack Name already exists. 
'''
def isStackNameExists(stack_name,region):
    stackExists = False
    try:
        cf_conn = boto3.client('cloudformation',region_name=region)
        response = cf_conn.describe_stacks(
        StackName = stack_name
    )
    except Exception as err:
        pass
        return stackExists


def main():
    Args = ArgParser()
    config = yaml.load(open('config.yaml'))
    config_yaml = yaml.dump(config,allow_unicode=True, default_flow_style=False)
    creat_stack_cloud(config_yaml,Args.instaType,Args.pem,Args.region)


if __name__ == "__main__":
    main()