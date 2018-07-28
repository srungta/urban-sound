import pickle
def read_from_pickle(pickle_file):
    pickle_file = open(pickle_file, "rb")
    emp = pickle.load(pickle_file)
    pickle_file.close()
    return emp

def save_as_pickle(data, pickle_file):
    try:
        f = open(pickle_file, 'wb')
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
        f.close()
    except Exception as e:
        print('Unable to save data to', pickle_file, ':', e)
        raise

import os.path
def file_exists(filename):
    return os.path.isfile(filename) 

def get_file_name(filepath):
    if file_exists(filepath):
        return os.path.basename(filepath)
    return ''

def join_paths(path1, path2):
    return os.path.join(path1,path2)