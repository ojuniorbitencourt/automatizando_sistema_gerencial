import pyautogui as bot
from time import sleep

# 1 - Clicar e digitar meu usuário
bot.click(975, 542, duration=1)
bot.write("jhonatan")
# 2 - Clicar e digitar minha senha
bot.click(974, 567, duration=1)
bot.write("123456")
# 3 - Clicar em "Entrar"
bot.click(871, 594, duration=1)
# 4 - Extrair cada produto
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        # 1 - Clicar e digitar produto
        bot.click(706, 528, duration=1)
        bot.write(produto)
        # 2 - Clicar e digitar quantidade
        bot.click(701, 556, duration=1)
        bot.write(quantidade)
        # 3 - Clicar e digitar preço
        bot.click(698, 581, duration=1)
        bot.write(preco)
        # 4 - Clicar em registrar
        bot.click(591, 741, duration=1)
        sleep(1)
