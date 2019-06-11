import os
l = []


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
    if(path.endswith('.c')):
        l.append(path)
    else:
        if(os.path.isdir(path)):
            for file in os.listdir(path):
                if(os.path.isdir(os.path.join(path, file)) or os.path.isfile(os.path.join(path, file))):
                    new_path = os.path.join(path, file)
                    (find_files(suffix, new_path))
    return l


print(find_files('.c', 'testdir'))
