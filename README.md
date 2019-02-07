# csapp
Servidor de controle remoto

### Teste do comando
```bash
curl -X POST http://127.0.0.1:5191/comandoA \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{ "msg": "ola"}
```

#

- Raiz app: [http://localhost:5191/](http://localhost:5191)

- bash exemplo: [teste.sh](./teste.sh) <p>
  _obs: com parametros extras_