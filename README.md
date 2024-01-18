# DSMB (Discord server management bot)

## Developing on environment (requirements)

- Python 3.11
- MongoDB 7.0.5
- `requirements-lock.txt`

---

## Create user (mongosh)

```js
db.createUser({
    user: "cs66-dsmb-bot",
    pwd: "",
    roles: [{ role: "readWrite", db: "cs66-dsmb-db" }]
})
```

## config.yaml

```yaml
token: ""
guild-id: 0
channel:
    role: 0
    delete-log: 0
    command: 0
role:
    section-01: 0
    section-02: 0
    section-03: 0
    cs66: 0
    ss661: 0
    ss662: 0
database:
    host: "localhost"
    port: 27017
    user: "cs66-dsmb-bot"
    password: ""
    tls: false
    db: "cs66-dsmb-db"
auto-send-message-button-give-role: 3600
version: "DEV"
```
