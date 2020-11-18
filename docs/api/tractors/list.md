# Tractors: list

Performs a query and sends back a list with tractor ids.

## HTTP Request

```text
GET /api/tractors
```

## Request parameters

In the request URL, provide the following query parameters with values.

| Parameter | Type    | Description             |
|:----------|:--------|:------------------------|
| make      | string  | The manufacturer's name |
| model     | string  | Model                   |
| condition | string  | Condition               |
| price_min | integer | Minimum price           |
| price_max | integer | Maximum price           |
| hours_min | integer | Minimum operating hours |
| hours_max | integer | Maximum operating hours |

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

| Property name | Value | Description                                                         |
|:--------------|:------|:--------------------------------------------------------------------|
| ids           | list  | Tractor ID list from the result array. Empty if there is no result. |

Otherwise the following structure is returned:

```text
{
  "errorCode": integer
}
```

| Property name | Value   | Description                         |
|:--------------|:--------|:------------------------------------|
| errorCode     | integer | See the table below for the details |

| Error code | Description              |
|:-----------|:-------------------------|
| 1          | Invalid query parameters |
