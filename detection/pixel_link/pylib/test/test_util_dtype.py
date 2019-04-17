import numpy as np

import util

@util.dec.print_test
def test_double():
    a = np.ones((3, 3), 'int')
    b = util.dtype.double(a)
    np.testing.assert_equal(b.dtype, np.dtype('float64'))

if util.mod.is_main(__name__):
    test_double()
