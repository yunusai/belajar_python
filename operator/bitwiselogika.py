#Materi logika pada angka biner (bitwise)

a = int(input("Masukkan nilai a: "));
b = int(input("Masukkan nilai b: "));

#AND
c = a & b;
print("a & b?" + str(c));
#OR
c = a| b;
print("a | b?" + str(c));
#XOR
c = a ^b;
print("a ^ b?" + str(c));
#NOT
c = ~a;
print("~a?" + str(c));
c= ~b;
print("~b?" + str(c));
#SHIFT LEFT
c = a<<b;
print("a << b?" + str(c));
c = b<<a;
print("b << a?" + str(c));
#SHFIT RIGHT
c = a>>b;
print("a >> b?" + str(c));
c=b>>a;
print("b >> a?" + str(c));
