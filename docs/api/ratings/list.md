# Ratings: list

Returns all ratings written for the specified tractor.

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
  "ratings": [
    {
      "tractor_id": integer,
      "username": string,
      "stars": integer,
      "comment": string
    }
  ]
}
```

| Property name      | Value   | Description                                                  |
|:-------------------|:--------|:-------------------------------------------------------------|
| ratings            | list    | List of ratings. Empty if there is no raing for the tractor. |
| ratings.tractor_id | integer | Tractor ID                                                   |
| ratings.username   | string  | Username                                                     |
| ratings.stars      | integer | Value of the rating (1-5)                                    |
| ratings.comment    | string  | Comment                                                      |

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
