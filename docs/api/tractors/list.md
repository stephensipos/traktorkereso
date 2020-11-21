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
  "tractors": [
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
  ]
}
```

| Property name            | Value   | Description                                         |
|:-------------------------|:--------|:----------------------------------------------------|
| tractors                 | list    | List of the results                                 |
| tractors.make            | string  | Manufacturer's name                                 |
| tractors.model           | string  | Model                                               |
| tractors.price           | integer | Price                                               |
| tractors.year            | string  | Year of manufacture, date format (YYYY-MM-DD)       |
| tractors.condition       | string  | Condition                                           |
| tractors.hours           | integer | Opering hours                                       |
| tractors.engine_power    | integer | Maximum performane in kWh                           |
| tractors.documents_valid | string  | Validity of the documents, date format (YYYY-MM-DD) |
| tractors.documents_type  | string  | Type of the Documents                               |
| tractors.description     | string  | Longer description                                  |
| tractors.image_url       | string  | URL of the tractor's image                          |
| tractors.fuel_type       | string  | Fuel type                                           |
| tractors.equipment[]     | list    | Equipment list (string)                             |

Otherwise the following structure is returned:

```text
{
  "error_code": integer
}
```

| Property name | Value   | Description                         |
|:--------------|:--------|:------------------------------------|
| error_code    | integer | See the table below for the details |

| Error code | Description              |
|:-----------|:-------------------------|
| 1          | Invalid query parameters |
