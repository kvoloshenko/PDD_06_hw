import os_tools.tools as f
import os

def test_create_dir():
    dir_name = 'test_dir_1'
    if os.path.exists(dir_name):
        os.rmdir(dir_name)
    f.create_dir(dir_name)
    assert os.path.exists(dir_name)
    os.rmdir(dir_name)

def test_del_dir():
    dir_name = 'test_dir_2'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    f.del_dir(dir_name)
    assert not os.path.exists(dir_name)