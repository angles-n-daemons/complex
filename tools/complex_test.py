from complex import ComplexNumber as CN,\
    ComplexVector as CV,\
    ComplexMatrix as CM, POLAR
from math import pi


def test_str():
    a, b, c, d, e, f, g, h, i, j = CN(0, 0),\
                                   CN(1, 0),\
                                   CN(0, 1),\
                                   CN(1, 1),\
                                   CN(-1, 0),\
                                   CN(0, -1),\
                                   CN(-1, -1),\
                                   CN(1, 2),\
                                   CN(1, -2),\
                                   CN(0, -2)

    assert(str(a) == '0')
    assert(str(b) == '1')
    assert(str(c) == 'i')
    assert(str(d) == '1 + i')
    assert(str(e) == '-1')
    assert(str(f) == '-i')
    assert(str(g) == '-1 - i')
    assert(str(h) == '1 + 2i')
    assert(str(i) == '1 - 2i')
    assert(str(j) == '-2i')


def test_conj():
    complex_nums = (CN(-1, 0), CN(1, -2), CN(-2, 4))
    conj_tuple = map(lambda x: x.conjugate(), complex_nums)

    answer = (CN(-1, 0), CN(1, -2), CN(-2, 4))
    assert(conj_tuple == answer)


def test_coordinates():

    a = CN(3, pi / 3, POLAR)
    b = CN(1, 1)
    c = CN(-2,-1)
    d = CN(-1,-2)
    print a
    print b.polar()
    print c.polar()
    print d.polar()
    import math
    print math.atan(-2/-1)
    print pow(5, .5)


def test_complex_vector():
    v = CV([CN(6, -4), CN(7, 3), CN(4.2, -8.1), CN(0, -3)])
    w = CV([CN(16, 2.3), CN(0, -7), CN(6, 0), CN(0, -4)])

    print v
    print w

    z = v + w

    print z

    l = CV([CN(6, 3), CN(0, 0), CN(5, 1), CN(4, 0)])

    print l
    print l.inverse()

    c = CN(3, 2)

    print l * c


def test_ex2_2_5():
    A = CM(3, 3)
    A[0][0] = CN(6, -3)
    A[0][1] = CN(2, 12)
    A[0][2] = CN(0, -19)
    A[1][0] = CN(0, 0)
    A[1][1] = CN(5, 2.1)
    A[1][2] = CN(17, 0)
    A[2][0] = CN(1, 0)
    A[2][1] = CN(2, 5)
    A[2][2] = CN(3, -4.5)

    print A
    print '\n'
    print A.conjugate()
    print '\n'
    print A.transpose()
    print '\n'
    print A.adjoint()


def test_mat_add():
    A = CM(2, 2)
    A[0][0] = CN(2, 5)
    A[0][1] = CN(-1, 2)
    A[1][0] = CN(4, 1)
    A[1][1] = CN(0, -9)

    B = CM(2, 2)
    B[0][0] = CN(-3, 1)
    B[0][1] = CN(2, 2)
    B[1][0] = CN(-6, -1.5)
    B[1][1] = CN(3, 0)

    print A + B


def test_mul():
    c1 = CN(0, 2)
    c2 = CN(1, 2)
    M = CM(2, 2)
    M[0][0] = CN(1, -1)
    M[0][1] = CN(3, 0)
    M[1][0] = CN(2, 2)
    M[1][1] = CN(4, 1)
    print c1 * c2
    print M * (c1 * c2)
    print '\n'

    A = CM(3, 3)
    A[0][0] = CN(3, 2)
    A[0][1] = CN(0, 0)
    A[0][2] = CN(5, -6)
    A[1][0] = CN(1, 0)
    A[1][1] = CN(4, 2)
    A[1][2] = CN(0, 1)
    A[2][0] = CN(4, -1)
    A[2][1] = CN(0, 0)
    A[2][2] = CN(4, 0)

    B = CM(3, 3)
    B[0][0] = CN(5, 0)
    B[0][1] = CN(2, -1)
    B[0][2] = CN(6, -4)
    B[1][0] = CN(0, 0)
    B[1][1] = CN(4, 5)
    B[1][2] = CN(2, 0)
    B[2][0] = CN(7, -4)
    B[2][1] = CN(2, 7)
    B[2][2] = CN(0, 0)
    print A
    print '\n'
    print B
    print '\n'
    print A * B
    print '\n'
    print B * A
    print '\n\n'
    print 'ex 2.2.9'
    print (A * B).transpose()
    print '\n'
    print (B.transpose()) * (A.transpose())
    print 'ex 2.2.10'
    print (A * B).adjoint()
    print '\n'
    print (B.adjoint()) * (A.adjoint())

def test_vec_mat_mul():
    M = CM(2, 2)
    M[0][0] = CN(1, -1)
    M[0][1] = CN(3, 0)
    M[1][0] = CN(2, 2)
    M[1][1] = CN(4, 1)

    cv = CV()
    cv.insert(CN(-1, 3))
    cv.insert(CN(2, 0))

    print M * cv


test_vec_mat_mul()

