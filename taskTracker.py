import os 
import json
import argparse
import time

task_id=0
description=''
status=''
created_at=''
updated_at=''
paths=['all_tasks.json','todo_tasks.json','in_progress.json','done_tasks.json']

parser=argparse.ArgumentParser(
    prog="TaskTracker",
    description="later",
    epilog="later"
)
parser.add_argument("--add", '-a', type=str, help="Add the task description")
parser.add_argument("--update", '-u', nargs=2, help="Enter the task id and the new description")
parser.add_argument("--list","-l",nargs=1, help="List all the task")
#parser.add_argument("--prueba","-p",help="Este argumento es para hacer pruebas")
#parser.add_argument("delete")

"""Time handling functions"""

def getTime():
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    return time_string


"""JSON files handling functions"""

def read_json(path_file):
    with open(path_file, 'r') as file:
        return json.load(file)


def write_json(path_file,data):
    dic=read_json(path_file)
    size=len(list(dic))
    dic[str('task'+str(size+1))]=data
    with open(path_file,"w") as rewrite_file:
        json.dump(dic, rewrite_file, indent=4)     

""" Args handling functions"""

def add(descripcion):
    return descripcion
def update(to_updte):
    id_task=to_update[0]
    new_description=to_update[1]

    dic=read_json(paths[0])



if __name__=='__main__':

    args=parser.parse_args()
    print(args)
    #check if the all_tasks.json file exist
    if not os.path.exists(paths[0]):
        with open(paths[0],'w') as all_tasks_file:
            json.dump({},all_tasks_file)
    #Add
    if args.add:
        all_tasks_len=len(list(read_json(paths[0])))
        task_id=all_tasks_len+1
        description=add(args.add)
        status='todo'
        created_at=getTime()
        #Creating the task dict
        task={
            "task_id":task_id, 
            "description":description, 
            "status":status, 
            "created_at":created_at, 
            "updated_at":updated_at
        }
    
        write_json(paths[0],task)
        print("Task added successfully"+"("+"ID: "+str(task["task_id"])+")")
    
    if args.update:
        to_update=update(args.update)
        print(to_update)


