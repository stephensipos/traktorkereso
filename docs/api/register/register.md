# Register: register

Registers a user

## HTTP Request

```text
POST /api/register
```

## Request body

In the request body, provide the following parameters:

| Parameter   | Type   | Description      |
|:------------|:-------|:-----------------|
| email       | string | e-mail address   |
| password    | string | password         |
| displayname | string | name of the user |

## Response

If successful, this method returns an empty response body.

In the case of any errors, the following structure returned:

```text
{
  "errorCode": integer
}
```

| Property name | Value   | Description                                       |
|:--------------|:--------|:--------------------------------------------------|
| errorCode     | integer | 1 - The provided e-mail address is already in use |
