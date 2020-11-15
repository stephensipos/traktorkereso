# Login: login

Performs a login with the provided parameters

## HTTP Request

```text
POST /api/login
```

## Request body

In the request body, provide the following parameters:

| Parameter | Type   | Description    |
|:----------|:-------|:---------------|
| email     | string | e-mail address |
| password  | string | password       |

## Response

If successful, this method returns a response body with the following structure:

```text
{
  "session_id": string
}
```

Otherwise the followin structure is returned:

```text
{
  "errorCode": integer
}
```

| Property name | Value   | Description                         |
|:--------------|:--------|:------------------------------------|
| errorCode     | integer | See the table below for the details |

| Error code | Description                                    |
|:-----------|:-----------------------------------------------|
| 1          | The provided e-mail address not exists         |
| 2          | The password not match with the e-mail address |
