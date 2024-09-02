"""Basic libraries of python to
    *Handle the os filesystem
    *Handle the JSON files and format
    *Handle the args from the CLI
    *Handle the time 
"""
import os
import json
import argparse
import time
#Variables
task_id=0
description=''
status=''
created_at=''
updated_at=''
paths=['all_tasks.json','todo_tasks.json','in_progress.json','done_tasks.json']
helps=[
    "Add the task description",
    "Enter the task id and the new description",
    "Delete the task with ID",
    "Mark in progress the task with the ID",
    "Mark a task status as done with the id",
    "List all the task"
    ]
parser=argparse.ArgumentParser(
    prog="TaskTracker",
    description="later",
    epilog="later"
)
parser.add_argument("--add", '-a', type=str, help=helps[0])
parser.add_argument("--update", '-u', nargs=2, help=helps[1])
parser.add_argument("--delete","-d", nargs=1,help=helps[2])
parser.add_argument("--markinprogress", "-mp", nargs=1, help=helps[3])
parser.add_argument("--markdone","-md",nargs=1,help=helps[4])
parser.add_argument("--list","-l",nargs='?',help=helps[5])
#Time handling functions
def get_time():
    """This function get the current time
    
    Keyword arguments: None
    Return: Return the current time in this format MM/DD/YYYY, HH:MM:SS
    """
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    return time_string
#JSON files handling functions
def read_json(path_file):
    """This function reads a JSON file and returns its contents as a dictionary.
    Keyword arguments:
    path_file -- a string representing the path of the file to be read.
    Return: 
    A dictionary containing the data from the JSON file.
    """
    with open(path_file, 'r', encoding="utf-8") as file:
        return json.load(file)

def re_write_file(path,data):
    """This function writes a dictionary to a JSON file, overwriting its contents.
    Keyword arguments:
    path -- a string representing the path of the file to be written.
    data -- a dictionary containing the data to be written to the JSON file.
    Return: 
    None
    """
    with open(path,"w", encoding="utf-8") as rewrite:
        json.dump(data, rewrite, indent=4)

def write_json(path_file,data):
    """This function reads a JSON file, adds new data under a unique task key, 
    and writes it back to the file.
    Keyword arguments:
    path_file -- a string representing the path of the file to be written.
    data -- a dictionary containing the data to be added to the JSON file.  
    Return: 
    None
    """
    dic=read_json(path_file)
    size=len(list(dic))
    dic[str('task'+str(size+1))]=data
    with open(path_file,"w", encoding="utf-8") as no_rewrite_file:
        json.dump(dic, no_rewrite_file, indent=4)

def create_file_if_not_exits(path):
    """This function checks if a JSON file exists at the specified path, 
    and creates an empty JSON file if it does not.
    Keyword arguments:
    path -- a string representing the path of the file to be checked or created.
    Return: 
    None
    """
    if not os.path.exists(path):
        with open(path,'w', encoding="utf-8") as all_tasks_file:
            json.dump({},all_tasks_file)
#Args handling functions
def add(descripcion):
    """This function takes a description as input of the CLI and returns it unchanged.
    Keyword arguments:
    descripcion -- a string representing the description to be returned.
    Return: 
    The input string `descripcion`.
    """
    return descripcion

def update(task_update):
    """This function updates the description and updated_at 
    fields of a specific task in a JSON file.
    Keyword arguments:
    task_update -- a list where the first element is the task ID (as a string or int) 
    and the second element is the new description (string).
    Return:
    None
    """
    id_task=task_update[0]
    new_description=task_update[1]
    #Udate in all
    dic=read_json(paths[0])
    tasks=list(dic.items())
    for i in range(len(tasks)):
        if i == int(id_task)-1:
            tasks[i][1]['description']=new_description
            tasks[i][1]['updated_at']=get_time()
    re_write_file(paths[0],dic)

def mark_in_progress(to_mark_in_progress):
    """This function marks a specific task as 'in-progress' 
    and adds it to a separate JSON file.
    Keyword arguments:
    to_mark_in_progress -- a list where the first element is the task ID 
    to be marked as 'in-progress'.
    Return:
    None
    """
    create_file_if_not_exits(paths[2])
    all_tasks_file=read_json(paths[0])
    tasks=list(all_tasks_file.items())
    for i in range(len(tasks)):
        if i == int(to_mark_in_progress[0])-1:
            tasks[i][1]['status']="in-progress"
            copy_in_progress=tasks[i][1]
    write_json(paths[2],copy_in_progress)

def mark_done(to_mark_done):
    """This function marks a specific task as 'done' 
    and adds it to a separate JSON file.
    Keyword arguments:
    to_mark_done -- a list where the first element
    is the task ID to be marked as 'done'.
    Return:
    None
    """
    create_file_if_not_exits(paths[3])
    all_tasks_file=read_json(paths[0])
    tasks=list(all_tasks_file.items())
    for i in range(len(tasks)):
        if i == int(to_mark_done[0])-1:
            tasks[i][1]['status']="done"
            copy_done=tasks[i][1]
    write_json(paths[3],copy_done)

def list_all(which_list):
    """This function lists all tasks from a specific category 
    or from the main task list, based on the input parameter.
    Keyword arguments:
    which_list -- a string indicating which list of tasks to display 
    ('in_progress', 'done', 'to-do' or None for all tasks).
    Return:
    None
    """
    if which_list is None:
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
        created_at=get_time()
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
    #Update
    if args.update:
        update(args.update)
    if args.markinprogress:
        mark_in_progress(args.markinprogress)
    if args.markdone:
        mark_done(args.markdone)
    if args.list is None or args.list is not None:
        list_all(args.list)
