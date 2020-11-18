# Tractors: get

Sends back the details of a tractor identified by its ID

## HTTP Request

```text
GET /api/tractors/<id>
```

## Request parameters

In the request URL, provide the following query parameters with values.

| Parameter | Type    | Description                |
|:----------|:--------|:---------------------------|
| id        | integer | id of the tractor to query |

## Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:

```text
{
  "make": string,
  "model": string,
  "price": integer,
  "year": string,
  "condition": string,
  "hours": integer,
  "engine_power": integer,
  "documents_valid": string
  "documents_type": string,
  "description": string,
  "image_url": string,
  "fuel_type": string,
  "equipment": [
      string
  ]
}
```

| Property name   | Value   | Description                                         |
|:----------------|:--------|:----------------------------------------------------|
| make            | string  | Manufacturer's name                                 |
| model           | string  | Model                                               |
| price           | integer | Price                                               |
| year            | string  | Year of manufacture, date format (YYYY-MM-DD)       |
| condition       | string  | Condition                                           |
| hours           | integer | Opering hours                                       |
| engine_power    | integer | Maximum performane in kWh                           |
| documents_valid | string  | Validity of the documents, date format (YYYY-MM-DD) |
| documents_type  | string  | Type of the Documents                               |
| description     | string  | Longer description                                  |
| image_url       | string  | URL of the tractor's image                          |
| fuel_type       | string  | Fuel type                                           |
| equipment[]     | list    | Equipment list (string)                             |

Otherwise the following structure is returned:

```text
{
  "error_code": integer
}
```

| Property name | Value   | Description                         |
|:--------------|:--------|:------------------------------------|
| error_code    | integer | See the table below for the details |

| Error code | Description                            |
|:-----------|:---------------------------------------|
| 1          | The provided tractor ID does not exist |
