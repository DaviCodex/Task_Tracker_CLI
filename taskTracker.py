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
parser.add_argument("--markinprogress", "-mp", nargs=1, help="Mark in progress the task with the ID")
parser.add_argument("--markdone","-md",nargs=1,help="Mark a task status as done with the id")
parser.add_argument("--list","-l",nargs='?',help="List all the task")

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

def re_write_file(path,data):
    with open(path,"w") as rewrite:
        json.dump(data, rewrite, indent=4)

def write_json(path_file,data):
    dic=read_json(path_file)
    size=len(list(dic))
    dic[str('task'+str(size+1))]=data
    with open(path_file,"w") as no_rewrite_file:
        json.dump(dic, no_rewrite_file, indent=4)     

def create_file_if_not_exits(path):
    if not os.path.exists(path):
        with open(path,'w') as all_tasks_file:
            json.dump({},all_tasks_file)

""" Args handling functions"""

def add(descripcion):
    return descripcion

def update(to_update):
    id_task=to_update[0]
    new_description=to_update[1]
    #Udate in all
    dic=read_json(paths[0])
    tasks=list(dic.items())
    for i in range(len(tasks)):
        if i == int(id_task)-1:
            tasks[i][1]['description']=new_description
            tasks[i][1]['updated_at']=getTime()
    re_write_file(paths[0],dic)

def mark_in_progress(to_mark_in_progress):
    create_file_if_not_exits(paths[2])
    all_tasks_file=read_json(paths[0])
    tasks=list(all_tasks_file.items())
    for i in range(len(tasks)):
        if i == int(to_mark_in_progress[0])-1:
            tasks[i][1]['status']="in-progress"
            copy=tasks[i][1]
    write_json(paths[2],copy)

def mark_done(to_mark_done):
    create_file_if_not_exits(paths[3])
    all_tasks_file=read_json(paths[0])
    tasks=list(all_tasks_file.items())
    for i in range(len(tasks)):
        if i == int(to_mark_done[0])-1:
            tasks[i][1]['status']="done"
            copy=tasks[i][1]
    write_json(paths[3],copy)

def list_all(which_list):

    if which_list==None:
        dic=read_json(paths[0])
        for k,v in dic.items():
            print(f"{k}: {v} ")
    elif which_list=='in_progress':
        dic=read_json(paths[2])
        for k,v in dic.items():
            print(f"{k}: {v} ")
    elif which_list=='done':
        dic=read_json(paths[3])
        for k,v in dic.items():
            print(f"{k}: {v} ")

if __name__=='__main__':

    args=parser.parse_args()
    print(args)
    #check if the all_tasks.json file exist
    create_file_if_not_exits(paths[0])
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
    if args.markinprogress:
        mark_in_progress(args.markinprogress)
    if args.markdone:
        mark_done(args.markdone)
    if args.list==None or args.list!=None:
        list_all(args.list)


        


