# Ratings: get

Returns the parameters of a rating

## HTTP Request

```text
GET /api/tractors/<ID>/ratings/<user_id>
```

## Request parameters

In the request URL, provide the following query parameters with values.

| Parameter | Type    | Description                              |
|:----------|:--------|:-----------------------------------------|
| ID        | integer | The ID of the specified tractor          |
| user_id   | integer | The ID of the user the rating belongs to |

## Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:

```text
{
  "id": integer,
  "tractor_id": integer,
  "stars": integer
}
```

| Property name | Value   | Description               |
|:--------------|:--------|:--------------------------|
| id            | integer | id of the rating          |
| tractor_id    | integer | Tractor ID                |
| stars         | integer | Value of the rating (1-5) |

Otherwise the following structure is returned:

```text
{
  "errorCode": integer
}
```

| Property name | Value   | Description                         |
|:--------------|:--------|:------------------------------------|
| errorCode     | integer | See the table below for the details |

| Error code | Description                                               |
|:-----------|:----------------------------------------------------------|
| 1          | There is no tractor with the specified ID                 |
| 2          | There is no rating with the specified tractor and user ID |
