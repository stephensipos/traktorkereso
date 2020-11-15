# Users: register

Registers a user

## HTTP Request

```text
POST /api/register
```

## Request parameters

In the request URL, provide the following query parameters with values.

| Parameter   | Type   | Description      |
|:------------|:-------|:-----------------|
| email       | string | e-mail address   |
| password    | string | password         |
| displayname | string | name of the user |

## Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:

```json
{
  "user_id": integer,
}
```

| Property name | Value   | Description               |
|:--------------|:--------|:--------------------------|
| user_id       | integer | ID of the registered user |