# Ratings: delete

Delete the authenticated users rating from the specified tractor. Needs valid authentication. The bearer token has to be sent among the header parameters.

## HTTP Request

```text
DELETE /api/tractors/<ID>/ratings
```

## Request parameters

In the request URL, provide the following query parameters with values.

| Parameter | Type    | Description                     |
|:----------|:--------|:--------------------------------|
| ID        | integer | The ID of the specified tractor |

## Request body

Do not supply a request body with this method.

## Header parameters

| Property name | Type   | Description  |
|:--------------|:-------|:-------------|
| Authorization | string | Bearer token |

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

| Error code | Description                             |
|:-----------|:----------------------------------------|
| 1          | Invalid authentication                  |
| 2          | No tractor exists with the specified ID |
| 3          | No rating is available to delete.       |
