# Ratings: list

Returns all ratings of the specified tractor.

## HTTP Request

```text
GET /api/tractors/<ID>/ratings
```

## Request parameters

In the request URL, provide the following query parameters with values.

| Parameter | Type    | Description                     |
|:----------|:--------|:--------------------------------|
| ID        | integer | The ID of the specified tractor |

## Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:

```text
{
  "ids": [
    integer
  ]
}
```

| Property name | Value | Description                                                  |
|:--------------|:------|:-------------------------------------------------------------|
| ids   | list  | List of user IDs who posted rating for the specified tractor |

Otherwise the following structure is returned:

```text
{
  "errorCode": integer
}
```

| Property name | Value   | Description                         |
|:--------------|:--------|:------------------------------------|
| errorCode     | integer | See the table below for the details |

| Error code | Description                               |
|:-----------|:------------------------------------------|
| 1          | There is no tractor with the specified ID |
