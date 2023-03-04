# Bot Login e Repository
- Este é um projeto de um bot para automatizar o processo de login no GitHub, criação de um repositório e criação de um arquivo, tudo isso usando a API do GitHub. O bot foi desenvolvido em Python e pode ser facilmente adaptado para outras plataformas.

## Como funciona
- O bot utiliza a biblioteca Requests do Python para fazer chamadas à API do GitHub e automatizar o processo de login e criação de repositórios. Para isso, ele faz uso de tokens de acesso pessoais do GitHub, que permitem que o bot acesse sua conta sem a necessidade de digitar a senha a cada vez.

## O processo é dividido em três etapas:
- Autenticação: O bot faz um login usando as informações de acesso pessoal.
- Criação de repositório: O bot faz uma chamada à API do GitHub para criar um repositório com o nome fornecido pelo usuário.
- Criação de arquivo: O bot cria um arquivo no repositório criado anteriormente e adiciona o código do próprio bot ao arquivo.

## Pré-requisitos
### Antes de executar o bot, você precisa ter os seguintes pré-requisitos:
- Python 3.6 ou superior instalado
- Bibliotecas Pyautogui e Webbrowser instaladas (você pode instalá-las usando o comando pip install requests e pip install Pyautogui no terminal)
- Como executar
- Para executar o bot, siga os passos abaixo:

## Instalação

- Clone este repositório em sua máquina local.
- Copy code
```bash
$ git clone https://github.com/seu_usuario/bot_repositorio.git
```
- Crie um virtualenv e ative-o.
- Instale as dependências listadas no arquivo requirements.txt usando o comando:
- Copy code
```bash
$ pip install -r requirements.txt
```
```bash
$ pip install pyautogui
```

## Abra o arquivo auto.py e insira as informações de login (nome de usuário e senha) no trecho de código indicado.
- O bot irá solicitar o nome que você deseja dar ao seu repositório e o nome que você deseja dar ao arquivo a ser criado. Após fornecer essas informações, o bot irá criar o repositório, criar o arquivo e adicionar o código ao arquivo.

## Contribuições
- Este é um projeto aberto e aceitamos contribuições. Se você quiser contribuir, por favor, faça um fork deste repositório, crie um branch com suas alterações e faça um pull request.

## Licença
- Este projeto está licenciado sob a licença MIT - consulte o arquivo LICENSE para obter detalhes.

