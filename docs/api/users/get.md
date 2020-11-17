# Users: get

Gets a user's data by user_id

## HTTP Request

```text
GET /api/users/<user_id>
```

## Request parameters

In the request URL, provide the following query parameters with values.

| Parameter | Type   | Description                   |
|:----------|:-------|:------------------------------|
| username  | string | username of the user to query |

## Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:

```text
{
  "username": string,
  "email": string,
  "firstName": string,
  "lastName": string
}
```

| Parameter | Type   | Description            |
|:----------|:-------|:-----------------------|
| username  | string | Username               |
| email     | string | E-mail address         |
| firstName | string | First name of the user |
| lastName  | string | Last name of the user  |

Otherwise the following structure is returned:

```text
{
  "errorCode": integer
}
```

| Property name | Value   | Description                         |
|:--------------|:--------|:------------------------------------|
| errorCode     | integer | See the table below for the details |

| Error code | Description                                 |
|:-----------|:--------------------------------------------|
| 1          | There is no user with the provided username |
