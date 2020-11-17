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
  "email": string,
  "password": string,
  "displayname": string
}
```

| Parameter   | Type   | Description      |
|:------------|:-------|:-----------------|
| email       | string | e-mail address   |
| password    | string | password         |
| displayname | string | name of the user |

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
| 1          | The provided e-mail address is already in use |
