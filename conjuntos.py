# conjuntos
Fconjunto = set()
Fconjunto = {1, 2, 3, "Carlos", 4, 5, 6}
Fconjunto.add(7)
Fconjunto.add("Milian")
a = frozenset({1, 2, 3})
b = {4, 5, 6}
c = a | b
d = a & b
e = b - a
f = a ^ b
g = {1, 2, 3, 5, 6}
print(11 not in Fconjunto)
print(c)
print(d)
print(e)
print(f)
print(b.issubset(g))
print(g.issuperset(e))
print(a.isdisjoint(b))
print()
