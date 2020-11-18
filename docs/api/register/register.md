# Register: register

Registers a user

## HTTP Request

```text
POST /api/register
```

## Request body

In the request body, provide the following parameters:

```text
{
  "username": string,
  "password": string,
  "email": string,
  "first_name": string,
  "last_name": string
}
```

| Parameter  | Type   | Description            |
|:-----------|:-------|:-----------------------|
| username   | string | Username               |
| password   | string | Password               |
| email      | string | E-mail address         |
| first_name | string | First name of the user |
| last_name  | string | Last name of the user  |

## Response

If successful, this method returns an empty response body.

Otherwise, the following structure is returned:

```text
{
  "errorCode": integer
}
```

| Property name | Value   | Description                         |
|:--------------|:--------|:------------------------------------|
| error_code    | integer | See the table below for the details |

| Error code | Description                                   |
|:-----------|:----------------------------------------------|
| 1          | The provided username is already in use       |
| 2          | The provided e-mail address is already in use |
