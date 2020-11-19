# Ratings: post

POST a rating to the specified tractor. Needs valid authentication. The bearer token has to be sent among the header parameters.

## HTTP Request

```text
POST /api/tractors/<ID>/ratings
```

## Request parameters

In the request URL, provide the following query parameters with values.

| Parameter | Type    | Description                     |
|:----------|:--------|:--------------------------------|
| ID        | integer | The ID of the specified tractor |

## Request body

In the request body, provide the following parameters:

```text
{
  "stars": integer,
  "comment" : string
}
```

| Property name | Type    | Description                   |
|:--------------|:--------|:------------------------------|
| stars         | integer | The value of the rating (1-5) |
| comment       | string  | Text review                   |

## Header parameters

| Property name | Type   | Description  |
|:--------------|:-------|:-------------|
| Authorization | string | Bearer token |

## Response

If successful, this method returns an empty response body.

Otherwise, the following structure is returned:

```text
{
  "error_code": integer
}
```

| Property name | Value   | Description                         |
|:--------------|:--------|:------------------------------------|
| error_code    | integer | See the table below for the details |

| Error code | Description                                      |
|:-----------|:-------------------------------------------------|
| 1          | Invalid authentication                           |
| 2          | No tractor exists with the specified ID          |
| 3          | Invalid stars value (have to be between 1 and 5) |
