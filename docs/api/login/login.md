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
  "bearer": string
}
```

If the user already has an existing token, the same token is returned.

Otherwise the following structure is returned:

```text
{
  "error_code": integer
}
```

| Property name | Value   | Description                         |
|:--------------|:--------|:------------------------------------|
| error_code    | integer | See the table below for the details |

| Error code | Description                                       |
|:-----------|:--------------------------------------------------|
| 1          | Authentication failed                             |

