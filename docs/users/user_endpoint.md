# User Endpoints

## Create custom user 

### `POST /api/users/`

#### Body
```
{
    username: "string",
    email: "email@mail.ru"
}
```
#### Response
```
{
    id: 0,
    username: "string",
    email: "email@mail.ru",
    is_active: false
}
```

## Create telegram user
### `POST /api/users/telegram-users/` 

#### Body
```
{
    username: "string",
    telegram_id: "string",
    first_name: "string",
    last_name: "string",
    additional_information: "string"
}
```
#### Response
```
{ 
    id: 0
    username: "string",
    telegram_id: "string",
    first_name: "string",
    last_name: "string",
    additional_information: "string",
    is_active: true
}
```