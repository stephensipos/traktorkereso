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
  "firstName": string,
  "lastName": string
}
```

| Parameter | Type   | Description            |
|:----------|:-------|:-----------------------|
| username  | string | Username               |
| password  | string | Password               |
| email     | string | E-mail address         |
| firstName | string | First name of the user |
| lastName  | string | Last name of the user  |

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
| errorCode     | integer | See the table below for the details |

| Error code | Description                                   |
|:-----------|:----------------------------------------------|
| 1          | The provided username is already in use       |
| 2          | The provided e-mail address is already in use |
