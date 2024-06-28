class A:
    def display_a(self):
        print("Iam inside a class A")
class B:
    def display_b(self):
        print("Iam inside a class B")
class C:
    def display_c(self):
        print("Iam inside a class C")
class X(A,B):
    def display_X(self):
        print("Iam inside a class X")
class Y(B,C):
    def display_Y(self):
        print("Iam inside a class Y")
class Z(X,Y,C):
    def display_Z(self):
        print("Iam inside a class Z")
z1=Z()
z1.display_a()

print(Z.mro())