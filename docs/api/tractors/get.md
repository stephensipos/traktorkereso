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
  "year": integer,
  "condition": string,
  "hours": integer,
  "engine_power": integer,
  "documents_valid": string
  "documents_type": string,
  "description": string,
  "image_url": string,
  "equipment": [
      string
  ]
}
```

| Property name   | Value   | Description                                         |
|:----------------|:--------|:----------------------------------------------------|
| manufacturer    | string  | Manufacturer's name                                 |
| model           | string  | Model                                               |
| price           | string  | Price                                               |
| year            | string  | Year of manufacture                                 |
| condition       | integer | Condition                                           |
| hours           | string  | Opering hours                                       |
| engine_power    | integer | Maximum performane in kWh                           |
| documents_valid | string  | Validity of the documents, date format (YYYY-MM-DD) |
| documents_type  | string  | Type of the Documents                               |
| description     | string  | Longer description                                  |
| imageUrl        | string  | URL of the tractor's image                          |
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
| 1          | The provided tractor id does not exist |
