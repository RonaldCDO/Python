from produto import Produto


p1 = Produto()
p2 = Produto()

p1.set_nome('Faca')
p1.set_preco(20)
p1.get_nome()
p1.get_preco()

p2.set_nome('Notebook')
p2.set_preco(3000)
p2.get_nome()
p2.get_preco()

book = {
    'title': 'The Giver',
    'author': 'Lois Lowry',
    'rating': 4.13
}
d1 = {'format': 'paperback'}
book.update(d1)
print(book.get('title'))
