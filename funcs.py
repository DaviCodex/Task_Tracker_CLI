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

def re_order_dic(dic):
    values=dic.values()
    values=change_ids(values)
    size=len(list(dic))
    new_keys=[]
    base='task'
    for i in range(size):
        new_key=base+str(i+1)
        new_keys.append(new_key)
    new_dic=dict(zip(new_keys,values))
    return new_dic

def change_ids(list_dicts):
    list_dicts=list(list_dicts)
    size=len(list_dicts)
    for i in range(size):
        list_dicts[i]['task_id']=i+1
    return list_dicts
def checking_status(dic):
    list_dict=list(dic.values())
    size=len(list_dict)
    status_list=[]
    for i in range(size):
        status=list_dict[i]['status']
        status_list.append(status)
    return status_list
def get_contents_dic(dic):
    items=dic.items()
    items=list(items)
    return items 

