# tiempo_girish_test

This script takes instance type, pem key file name and region as an argument 
Create a cloudformation stack.
Checks:
1. If StackName already exists, script will exit
2. If Stack already exists, script will exit
3. If there is any error, in parameters, script will exit. 

Improvments:
1. Handling Exception for File Handling
2. Improving Parameters handling for create-stack
3. Generate the JSON or YAML , rather than using the template. 
4. Logging
5. Verbose mode to be added