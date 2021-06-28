from pessoa import Pessoa


p1 = Pessoa('Ronald', 25)
p2 = Pessoa ('Thainá', 19)
p1.falar('Python')
p1.parar_falar()
p1.comer('Pizza')
p2.falar('Arquitetura')
p1.falar('POO')
p1.parar_comer()
p2.comer('Nutella')
p2.parar_comer()
p1.falar('POO')
p2.comer('Nutella')
print(p2.get_ano_nasc())
print(p1.get_ano_nasc())