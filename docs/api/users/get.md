# Users: get

Gets a user's data by user_id

## HTTP Request

```text
GET /api/users/<user_id>
```

## Request parameters

In the request URL, provide the following query parameters with values.

| Parameter | Type   | Description                                   |
|:----------|:-------|:----------------------------------------------|
| user_id   | string | user_id (e-mail address) of the user to query |

## Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:

```text
{
  "email": string,
  "displayname": string
}
```

| Property name | Value  | Description   |
|:--------------|:-------|:--------------|
| email         | string | email address |
| displayname   | string | display name  |

Otherwise the following structure is returned:

```text
{
  "errorCode": integer
}
```

| Property name | Value   | Description                             |
|:--------------|:--------|:----------------------------------------|
| errorCode     | integer | 1 - The provided user_id does not exist |
