import os 
import json
import argparse
import time

task_id=0
description=''
status=''
created_at=''
updated_at=''
tasks={}
parser=argparse.ArgumentParser(
    prog="TaskTracker",
    description="later",
    epilog="later"
)

parser.add_argument("--add", '-a', type=str, help="Add the task description")
parser.add_argument("--update", '-u', nargs=2, help="Enter the task id and the new description")
parser.add_argument("--list","-l",default="All",nargs='?', help="List all the task")
#parser.add_argument("delete")

def getTime():

    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    return time_string

def add(descripcion):
    return descripcion
def list_task(JSON):
    tasks[f'task{len(list(tasks))}']=JSON
    return tasks

if __name__=='__main__':

    args=parser.parse_args()

    if args.add:
        if len(list(tasks)) == 0:
            task_id=1
        else:
            task_id=len(list(tasks))+1
        description=add(args.add)
        status='todo'
        created_at=getTime()
    
    task={task_id:task_id, description:description, status:status, created_at:created_at, updated_at:updated_at}

    if args.list:

        if args.list == "all":
            tasks=list_task(args.list)
            JSON=json.dumps(tasks)
            print(JSON)

    


