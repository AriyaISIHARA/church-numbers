"""Church Numbers"""


ZERO = (lambda s: (lambda z: z))
SUCC = (lambda n: (lambda s: (lambda z: s(n(s)(z)))))
ADD = (lambda m: (lambda n: (lambda s: (lambda z: (m(s)(n(s)(z)))))))
MUL = (lambda m: (lambda n: (lambda s: m(n(s)))))
EXP = (lambda m: m)
PRED = (lambda n: (lambda s: (lambda z: (n(lambda f: (lambda g: (g(f(s)))))(lambda u: z)(lambda u: u)))))

TRUE = (lambda x: (lambda y: x))
FALSE = (lambda x: (lambda y: y))
AND = (lambda p: (lambda q: p(q)(FALSE)))
OR = (lambda p: (lambda q: p(TRUE)(q)))
NOT = (lambda p: p(FALSE)(TRUE))
COND = (lambda p: (lambda x: (lambda y: p(x)(y))))
ISZERO = (lambda n: (n(lambda x: FALSE)(TRUE)))


def rep(n):
    """representation of a given natural number"""
    return SUCC(rep(n - 1)) if n > 0 else ZERO


def sem(e):
    """Church numbers semantics"""
    return e(lambda x: x + 1)(0)


def semp(p):
    """Church booleans"""
    return p(True)(False)


if __name__ == '__main__':
    three = rep(3)
    five = rep(5)
    print('five:', sem(five))
    print('three plus five:', sem(ADD(three)(five)))
    print('three times five:', sem(MUL(three)(five)))
    print('third power of five:', sem(EXP(three)(five)))
    for i in range(5):
        print('predecessor of %d:' % i, sem(PRED(rep(i))))

    print('true and false:', semp(AND(TRUE)(FALSE)))
    print('true or false:', semp(OR(TRUE)(FALSE)))
    print('not true:', semp(NOT(TRUE)))
    print('not false:', semp(NOT(FALSE)))
    print('ZERO is zero:', semp(ISZERO(ZERO)))
    print('three is zero:', semp(ISZERO(three)))
