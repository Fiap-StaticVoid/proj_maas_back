# Te Entrega
O backend do Aplicativo Te Entrega

## Rodando
Basta instalar o [`docker-compose`](https://docs.docker.com/compose/install/) e usar o comando `docker compose up` na raiz do projeto(onde está o arquivo compose.yaml).

Para conseguir visualizar toda a api, acesse a rota `localhost:8000` no seu navegador.

## Informações extras
Para garantir a segurança de nossas rotas, apenas a rota de criar clientes pode ser acessada sem estar logado no sistema,
 assim sendo necessário ter uma conta de cliente para poder usar o sistema.

### Segurança da sua conta
Assim garantimos que oque você faz no nosso sistema esteja sempre privado a você.

- Apenas você consegue ver e editar seu usuário;
- Apenas você consegue ver e editar as suas entregas;
