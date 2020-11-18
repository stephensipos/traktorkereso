# Ratings: list

POST a rating to the specified tractor.

## HTTP Request

```text
POST /api/tractors/<ID>/ratings/<user_id>
```

## Request parameters

In the request URL, provide the following query parameters with values.

| Parameter | Type    | Description                     |
|:----------|:--------|:--------------------------------|
| ID        | integer | The ID of the specified tractor |
| user_id   | integer | The ID of the user              |

## Request body

In the request body, provide the following parameters:

```text
{
  "stars": integer
}
```

| Property name | Type    | Description                   |
|:--------------|:--------|:------------------------------|
| stars         | integer | The value of the rating (1-5) |


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
| error_code    | integer | See the table below for the details |

| Error code | Description                               |
|:-----------|:------------------------------------------|
| 1          | There is no tractor with the specified ID |
| 2          | Invalid user ID                           |
| 3          | Invalid stars value                       |
