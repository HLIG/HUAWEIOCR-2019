# encoding = utf-8
from common_import import *

@util.dec.print_test
def test_ls():
    np.testing.assert_equal(ls('.', suffix = '.py'), ls('.', suffix = '.PY'))

@util.dec.print_test
def test_readlines():
    p = __file__
    lines = read_lines(p)
    for l in lines:
        print l    

@util.dec.print_test
def test_write_lines():
    p = '~/temp/log/w.txt'
    lines = read_lines(__file__)
    write_lines(p, lines)
    lines2 = read_lines(p)
    np.testing.assert_equal(lines, lines2)
    
@util.dec.print_test
def test_mat_io():
    path = '~/temp/testpython.mat'
    util.io.dump_mat(path, {'a': 1,'b': 2,'c': 3,'d': np.ones((3, 3))})   
    data =  util.io.load_mat(path)
    for c in data:
        print data[c]
      
    vs = util.io.dir_mat(path)
    print vs
#test_ls()
#test_readlines()
#test_write_lines()
test_mat_io()

