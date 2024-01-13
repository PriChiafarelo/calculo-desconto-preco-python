"""Faça um algorítimo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto"""

preco = float(input('Digite o preço do produto: '));

print('O preço com desconto de 5% é R${:.2f}'.format(preco - preco * 0.05))
