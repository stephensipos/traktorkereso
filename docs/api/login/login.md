# Login: login

Performs a login with the provided parameters

## HTTP Request

```text
POST /api/login
```

## Request body

In the request body, provide the following parameters:

```text
{
  "username": string,
  "password": string
}
```

| Parameter | Type   | Description |
|:----------|:-------|:------------|
| username  | string | Username    |
| password  | string | Password    |

## Response

If successful, this method returns a response body with the following structure:

```text
{
  "session_id": string
}
```

Otherwise the following structure is returned:

```text
{
  "errorCode": integer
}
```

| Property name | Value   | Description                         |
|:--------------|:--------|:------------------------------------|
| errorCode     | integer | See the table below for the details |

| Error code | Description                                       |
|:-----------|:--------------------------------------------------|
| 1          | The provided username not exists                  |
| 2          | The password not match with the provided username |
