# Tractors: list

Sends back the details of a tractor identified by its ID

## HTTP Request

```text
GET /api/tractors?[make=<make>&model=<model>&condition=<condition>&price_min=<price_min>&price_max=<price_max>&hours_min=<hours_min>&hours_max=<hours_max>]
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
  "id_list": [
    integer
  ]
}
```

| Property name | Value | Description                                                 |
|:--------------|:------|:------------------------------------------------------------|
| id_list       | list  | ID list from the result array. Empty if there is no result. |

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
