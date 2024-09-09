"""Basic libraries of python to
    *Handle the os filesystem
    *Handle the JSON files and format
    *Handle the args from the CLI
    *Handle the time 
"""
import argparse
import time
import Json_handle
import funcs
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
#CRUD
def add(descripcion):
    """This function takes a description as input of the CLI and returns it unchanged.
    Keyword arguments:
    descripcion -- a string representing the description to be returned.
    Return: 
    The input string `descripcion`.
    """
    all_tasks_len=funcs.get_file_size(paths[0])
    task_id=all_tasks_len+1
    description=descripcion[0]
    status='todo'
    created_at=get_time()
    task={
            "task_id":task_id, 
            "description":description, 
            "status":status, 
            "created_at":created_at, 
            "updated_at":updated_at
        }
    all_tasks_path=paths[0]
    Json_handle.write_json(all_tasks_path,task)
    print("Task added successfully"+"("+"ID: "+str(task["task_id"])+")")

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
    dic=Json_handle.read_json(paths[0])
    tasks=list(dic.items())
    print(tasks)
    for i in range(len(tasks)):
        if i == int(id_task)-1:
            tasks[i][1]['description']=new_description
            tasks[i][1]['updated_at']=get_time()
    Json_handle.write_json(paths[0],dic,True)

def delete(task_delete):
    """This function deletes a specific task from the JSON file based on the task ID.
    Keyword arguments:
    task_delete -- a list where the first element is the task ID of the task to be deleted.
    Return:
    None
    """
    id_task=task_delete[0]
    dic=Json_handle.read_json(paths[0])
    tasks=list(dic.items())
    for i in range(len(tasks)):
        if i == int(id_task)-1:
            tasks.pop(i)
    dic=dict(tasks)
    dic_ordered=funcs.re_order_dic(dic)
    Json_handle.write_json(paths[0],dic_ordered,True)

def mark_in_progress(to_mark_in_progress):
    """This function marks a specific task as 'in-progress' 
    and adds it to a separate JSON file.
    Keyword arguments:
    to_mark_in_progress -- a list where the first element is the task ID 
    to be marked as 'in-progress'.
    Return:
    None
    """
    id_change=int(to_mark_in_progress[0])
    Json_handle.create_file_if_not_exits(paths[2])
    all_tasks_file=Json_handle.read_json(paths[0])
    tasks=list(all_tasks_file.items())
    for i in range(len(tasks)):
        if i == id_change-1:
            tasks[i][1]['status']="in-progress"
            copy_in_progress=tasks[i][1]
            Json_handle.write_json(paths[2],copy_in_progress)
            delete([i])

def mark_done(to_mark_done):
    """This function marks a specific task as 'done' 
    and adds it to a separate JSON file.
    Keyword arguments:
    to_mark_done -- a list where the first element
    is the task ID to be marked as 'done'.
    Return:
    None
    """
    Json_handle.create_file_if_not_exits(paths[3])
    all_tasks_file=Json_handle.read_json(paths[0])
    tasks=list(all_tasks_file.items())
    for i in range(len(tasks)):
        if i == int(to_mark_done[0])-1:
            tasks[i][1]['status']="done"
            copy_done=tasks[i][1]
            Json_handle.write_json(paths[3],copy_done)
            delete([i])

def list_all(which_list):
    """This function lists all tasks from a specific category 
    or from the main task list, based on the input parameter.
    Keyword arguments:
    which_list -- a string indicating which list of tasks to display 
    ('in_progress', 'done', 'to-do' or None for all tasks).
    Return:
    None
    """
    if which_list == 'all':
        dic=Json_handle.read_json(paths[0])
        for k,v in dic.items():
            print(f"{k}: {v} ")
    elif which_list=='in_progress':
        dic=Json_handle.read_json(paths[2])
        for k,v in dic.items():
            print(f"{k}: {v} ")
    elif which_list=='done':
        dic=Json_handle.read_json(paths[3])
        for k,v in dic.items():
            print(f"{k}: {v} ")

#General Propouse functions
if __name__=='__main__':

    args=parser.parse_args()
    print(args)
    #check if the all_tasks.json file exist
    Json_handle.create_file_if_not_exits(paths[0])
    #Add
    if args.add:
        add(args.add)
    #Update
    if args.update:
        update(args.update)
    #Delete
    if args.delete:
        delete(args.delete)
    #Mark in progress
    if args.markinprogress:
        mark_in_progress(args.markinprogress)
    #Mark done
    if args.markdone:
        mark_done(args.markdone)
    #Print the list
    if args.list is not None:
        list_all(args.list)
