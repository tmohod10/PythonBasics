class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.mro())
D.__str__


# order is D then B->C and then A
#     A
#   /   \
# B       C
#   \   /
#     D


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.__mro__)
# MRO is complicated and the algorithm is handled by Python
