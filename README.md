### Запуск приложения

- Установить pg secret
```shell
kubectl apply -f .kube/pg-secret.yml
```

- Запустить БД
```shell
helm install postgresql oci://registry-1.docker.io/bitnamicharts/postgresql -f pg-values.yaml
```

- Применить манифесты
```shell
kubectl apply -f .kube/
```


### Миграции

Создать папку с миграциями
```shell
alembic init
```

Создать миграцию
```shell
alembic revision --autogenerate -m 'initial'
```

Накатить миграцию
```shell
alembic upgrade head
```

### Дополнительные заметки
Удаление БД
```shell
helm delete postgresql
```