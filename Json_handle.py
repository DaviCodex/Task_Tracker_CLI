import json
import os 
import funcs 

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
def read_json(path_file):
    """This function reads a JSON file and returns its contents as a dictionary.
    Keyword arguments:
    path_file -- a string representing the path of the file to be read.
    Return: 
    A dictionary containing the data from the JSON file.
    """
    with open(path_file, 'r', encoding="utf-8") as file:
        return json.load(file)

def write_json(path_file,data,update):
    """This function reads a JSON file, adds new data under a unique task key, 
    and writes it back to the file.
    Keyword arguments:
    path_file -- a string representing the path of the file to be written.
    data -- a dictionary containing the data to be added to the JSON file.  
    Return: 
    None
    """
    if update:
        dic=data
        with open(path_file,"w", encoding="utf-8") as no_rewrite_file:
            json.dump(dic, no_rewrite_file, indent=4)
    else:
        dic=read_json(path_file)
        file_size=funcs.get_file_size(path_file)
        new_key=funcs.create_key(file_size)
        dic[new_key]=data
        with open(path_file,"w", encoding="utf-8") as no_rewrite_file:
            json.dump(dic, no_rewrite_file, indent=4)
