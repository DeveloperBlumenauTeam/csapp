curl -X POST http://127.0.0.1:5191/comandoA \
  -H 'Autorizador: jwt eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJOUyIsImF1ZCI6InNtYXJ0Lm5zcG9ydGFsLmNvbS5iciIsInN1YiI6IjVhZmFjZWJjMzU2ZDhlNmQ4OGUyMzAxZCIsInNjb3BlIjpbIm1hc3Rlcjp0cnVlIl0sImlhdCI6MTUyODIzNzkyNX0.IgcapigIWPe_GzAQqDz4NbYw3bxgB6uQ9t3xL5piNXc' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 8db07bb5-5eae-4a1f-87c0-bc0a5300725e' \
  -H 'host: nome_maquina_generica' \
  -d '{ "cliente": { "id": "5bf6d1fdeab9cf533ad7de52", "name": "Cliente 1"}, "fieldsValue": { "valor1": "1234","valor2": "56789"},"user": {"email": "edupagotto@gmail.com","name": "admin"}}'
