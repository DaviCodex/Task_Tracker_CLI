import Json_handle

def get_file_size(path):
    dic=Json_handle.read_json(path)
    dic=list(dic)
    size=len(dic)
    return size

def create_key(size):
    str1='task'
    id_t=size+1
    key=str1+str(id_t)
    return key