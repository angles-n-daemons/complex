from math import sin, cos, atan

CARTESIAN = 0
POLAR = 1


def from_polar(p, t):
    return (p * cos(t)), (p * sin(t))


class ComplexNumber:
    def __init__(self, x, y, rep=CARTESIAN):
        if rep == CARTESIAN:
            self.a, self.b = x, y
        else:
            self.a, self.b = from_polar(x, y)

    def __add__(self, cn):
        if not isinstance(cn, ComplexNumber):
            raise Exception("Can only add Complex Number to another Complex Number.")

        a = self.a + cn.a
        b = self.b + cn.b
        return ComplexNumber(a, b)

    def __mul__(self, cn):
        if not isinstance(cn, ComplexNumber):
            raise Exception("Can only multiply Complex Number with another Complex Number.")

        a, b = self.a, self.b
        c = (a * cn.a) - (b * cn.b)
        d = (a * cn.b) + (b * cn.a)
        return ComplexNumber(c, d)

    def __div__(self, cn):
        if not isinstance(cn, ComplexNumber):
            raise Exception("Can only divide Complex Number by another Complex Number.")

        denom = pow(cn.modulus(), 2)
        a, b = self.a, self.b
        c = (a * cn.a) + (b * cn.b)
        d = (cn.a * b) - (a * cn.b)
        return ComplexNumber(c / denom, d / denom)

    def __str__(self):
        params = ['(']
        a, b = self.a, self.b

        if not (a or b):
            params.append('0')
        if a:
            params.append(str(a))
        if a and b:
            params.append(' ')
        if b:
            if b > 0:
                if a:
                    params.append('+')
            else:
                params.append('-')

            if a:
                params.append(' ')

            if abs(b) != 1:
                params.append(str(abs(b)))

            params.append('i')
        params.append(')')
        return ''.join(params)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, cn):
        return cn.a == self.a and cn.b == self.b

    def conjugate(self):
        return ComplexNumber(self.a, -self.b)

    def modulus(self):
        return pow(pow(self.a, 2) + pow(self.b, 2), .5)

    def polar(self):
        p = self.modulus()
        t = atan(self.b / self.a)
        return p, t


class ComplexVector:
    def __init__(self, v=None):
        self.v = v if v and len(v) else []

    def insert(self, cn):
        self.v.append(cn)

    def inverse(self):
        cv = ComplexVector()
        for i, cn in enumerate(self):
            cv.insert(ComplexNumber(cn.a, cn.b * -1))
        return cv

    def __len__(self):
        return len(self.v)

    def __iter__(self):
        return iter(self.v)

    def __getitem__(self, i):
        return self.v[i]

    def __add__(self, cv):
        if not isinstance(cv, ComplexVector):
            raise Exception("Can only add Complex Vector to another Complex Vector.")

        if len(self) != len(cv):
            raise Exception('Complex Vectors must be of same length to add.')

        new_vec = ComplexVector()
        for i, cn in enumerate(self):
            new_vec.insert(cn + cv[i])

        return new_vec

    def __mul__(self, cn):
        if not isinstance(cn, ComplexNumber):
            raise Exception("Can only scalar multiply Complex Vector by a Complex Number.")

        new_vec = ComplexVector()

        for i, cni in enumerate(self):
            new_vec.insert(cn * cni)

        return new_vec

    def __str__(self):
        return str(self.v)

    def __repr__(self):
        return str(self)

    def __eq__(self, cv):
        return self.v == cv


class ComplexMatrix:
    def __init__(self, m, n):
        self.m, self.n = m, n
        self.rows = [[ComplexNumber(0, 0)] * n for _ in xrange(m)]

    def __getitem__(self, idx):
        return self.rows[idx]

    def __setitem__(self, idx, item):
        self.rows[idx] = item

    def __str__(self):
        s = '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    def __add__(self, cm):
        """ Add a matrix to this matrix and
        return the new matrix. Doesn't modify
        the current matrix """

        if self.get_rank() != cm.get_rank():
            raise Exception("Trying to add matrixes of varying rank!")

        ret = ComplexMatrix(self.m, self.n)
        for i in xrange(self.m):
            for j in xrange(self.n):
                ret[i][j] = cm[i][j] + self.rows[i][j]

        return ret

    def __mul__(self, co):
        if isinstance(co, ComplexNumber):
            return self.scalar_mul(co)
        elif isinstance(co, ComplexMatrix):
            return self.cross_mul(co)
        elif isinstance(co, ComplexVector):
            return self.vec_mul(co)
        else:
            raise Exception("Trying to multiply matrix with unknown type.")

    def get_rank(self):
        return [self.m, self.n]

    def conjugate(self):
        m, n = self.m, self.n
        mat = ComplexMatrix(m, n)
        mat.rows = [[e.conjugate() for e in r] for r in self.rows]
        return mat

    def transpose(self):
        n, m = self.m, self.n
        mat = ComplexMatrix(n, m)
        for i in xrange(m):
            for j in xrange(n):
                mat[j][i] = self.rows[i][j]
        return mat

    def adjoint(self):
        return self.conjugate().transpose()

    def scalar_mul(self, cn):
        mat = ComplexMatrix(self.m, self.n)
        mat.rows = [[e * cn for e in row] for row in self.rows]
        return mat

    def vec_mul(self, cv):
        if self.m != len(cv):
            raise Exception("Cannot multiply by vector with different rank!")

        rows = self.rows
        vec = ComplexVector()
        for i in xrange(self.m):
            cn = ComplexNumber(0, 0)
            for j in xrange(self.n):
                cn += rows[i][j] * cv[j]
            vec.insert(cn)
        return vec

    def cross_mul(self, cm):
        if self.n != cm.m:
            raise Exception("Trying to cross multiply matrices of varying rank!")

        rows = self.rows
        mat = ComplexMatrix(self.m, self.m)
        for i in xrange(self.m):
            for j in xrange(self.m):
                cn = ComplexNumber(0, 0)
                for k in xrange(self.n):
                    cn += rows[i][k] * cm[k][j]
                mat[i][j] = cn
        return mat
