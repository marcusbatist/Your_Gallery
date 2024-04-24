# Minha Galeria de Fotos

Este é um projeto de aplicação web onde os usuários podem gerenciar suas galerias de fotos, com funcionalidades de autenticação, login e registro.

## Objetivo do Projeto

O objetivo deste projeto é desenvolver um serviço de autenticação com funcionalidades de login e registro para os usuários. Após o login, os usuários serão capazes de acessar sua galeria de fotos, onde poderão gerenciar suas fotos, inserindo novas fotos e removendo as existentes.

### Funcionalidades Principais

1. **Autenticação de Usuário:**
   - Permitir que os usuários se registrem e façam login em suas contas.
   - Garantir a segurança das informações de login dos usuários.

2. **Galeria de Fotos:**
   - Após o login, os usuários serão redirecionados para sua galeria de fotos pessoal.
   - Os usuários podem visualizar todas as fotos em sua galeria.
   - Os usuários podem adicionar novas fotos à sua galeria.
   - Os usuários podem remover fotos existentes de sua galeria.

### Principais Componentes

1. **Autenticação:**
   - Implementação de formulários de registro e login.
   - Validação de dados de usuário durante o registro.
   - Verificação de credenciais durante o login.

2. **Galeria de Fotos:**
   - Desenvolvimento de uma página de galeria de fotos.
   - Integração de um formulário de upload de fotos.
   - Implementação de funcionalidades para adicionar e remover fotos.

## Justificação Técnica da Escolha do Framework

Este projeto utiliza o framework Django devido à sua robustez, segurança e facilidade de desenvolvimento. Django fornece um sistema de autenticação de usuário integrado e uma ORM poderosa, que simplifica o desenvolvimento de aplicações web com autenticação. Além disso, Django possui uma grande comunidade de desenvolvedores e uma vasta documentação, o que facilita o aprendizado e a resolução de problemas.

## Processo de Instalação

Siga estas instruções para configurar o ambiente de desenvolvimento e executar a aplicação:

1. Clone este repositório:

    ```bash
    git clone https://github.com/marcusbatist/Your_Gallery.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd my_gallery
    ```


3. Inicie o servidor de desenvolvimento:

    ```bash
    python3 manage.py runserver
    ```

4. Abra o navegador e acesse `http://localhost:8000` para visualizar a aplicação.

## Como Utilizar a Aplicação

Após iniciar a aplicação, siga estes passos:

1. Faça o registro depois login para sua conta.

2. Você será redirecionado para a sua galeria de fotos, onde poderá ver todas as fotos que 
você já adicionou. SE não aparecer nenhuma foto e porque não inseri-tes nada ainda.

3. Para adicionar uma nova foto, clique no botão "Adicionar Foto" e selecione a foto desejada.

4. Para remover uma foto, clique na foto que deseja remover e selecione a opção "Remover Foto".

5. Você pode visualizar suas fotos em uma grade na página principal da galeria.
