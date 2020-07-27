# flask-Generator
Uma aplicação python que gera um app base para flask ja com as estrutura e configurações prontas

```sh
$ git clone https://github.com/psicopython/flask-Generator

$ cd flask-Generator

$ python GerarApp

```

Ele vai pedir um nome para o projeto
Neste exemplo, vou chamar de Blog.

```sh
Nome do package: _Blog_
```
E se td ocorrer bem, vai mostrar uma mensagem de sucesso.

Após isso você pode cria uma venv
(não é obrigatório,mas é recomendado).

```sh

$ python -m venv venv

$ source venv/bin/activate

$ cd Blog

$ pip install -r requirements.txt

$ flask run

```
Após isso, abra o navegador, acesse o endereço:
```sh
127.0.0.1:5000
```
E deve aparecer um 'Hello World' se td estiver certo
