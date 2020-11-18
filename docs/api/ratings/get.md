# Ratings: get

Returns the details of a rating for a specific tractor written by a user.

## HTTP Request

```text
GET /api/tractors/<ID>/ratings/<username>
```

## Request parameters

In the request URL, provide the following query parameters with values.

| Parameter | Type    | Description                                |
|:----------|:--------|:-------------------------------------------|
| ID        | integer | The ID of the specified tractor            |
| username  | string  | Username of the user the rating belongs to |

## Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:

```text
{
  "tractor_id": integer,
  "username": string,
  "stars": integer,
  "comment": string
}
```

| Property name | Value   | Description               |
|:--------------|:--------|:--------------------------|
| tractor_id    | integer | Tractor ID                |
| username      | string  | Username                  |
| stars         | integer | Value of the rating (1-5) |
| comment       | string  | Comment                   |

Otherwise the following structure is returned:

```text
{
  "errorCode": integer
}
```

| Property name | Value   | Description                         |
|:--------------|:--------|:------------------------------------|
| errorCode     | integer | See the table below for the details |

| Error code | Description                                                |
|:-----------|:-----------------------------------------------------------|
| 1          | There is no tractor with the specified ID                  |
| 2          | There is no rating with the specified tractor and username |
