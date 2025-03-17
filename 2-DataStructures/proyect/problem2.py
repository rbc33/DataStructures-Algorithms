# %%
import os 


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    """
    if not path:    return
    file_list = []
    dir_list= os.listdir(path)  
    # Iterate over all the entries
    for item in dir_list:
        #build path
        new_path = os.path.join(path, item)
        #recursion base case
        if os.path.isfile(new_path) and new_path.endswith(suffix):
            file_list.append(new_path)
        #if directory, then concatenate current list with all 
        #to be qualified files then recurse 
        elif os.path.isdir(new_path):
            file_list += find_files(suffix, new_path)
                
    return file_list 




# %%
## Test Case 1  No patg provided

list_of_directories = find_files(".h", None)
print(list_of_directories)

# %%

## Test Case 2 ./testdir
list_of_directories = find_files(".h", "testdir")
print(list_of_directories)

# %%
## Test Case 3 no given suffix
list_of_directories = find_files("", "testdir")
print(list_of_directories)


