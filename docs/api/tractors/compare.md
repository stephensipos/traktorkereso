# Tractors: compare

Performs a compation between the selected tractors, provided by an ID list. 

## HTTP Request

```text
GET /api/compare
```

## Request parameters

In the request URL, provide the following query parameters with values.

| Parameter | Type | Description                           |
|:----------|:-----|:--------------------------------------|
| tractors  | list | List of tractors to compare (integer) |

## Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:

```text
{
  "tractors": [
    {
      "parameters" : {
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
      },
      "mark" : {
        "price": boolean,
        "year": boolean,
        "hours": boolean,
        "engine_power": boolean,
        "documents_valid": boolean
      }
    }
  ]
}
```

| Property name                         | Value   | Description                                                |
|:--------------------------------------|:--------|:-----------------------------------------------------------|
| tractors[]                            | list    | List of tractors                                           |
| tractors[].parameters                 | object  | Parameters of the tractor                                  |
| tractors[].parameters.make            | string  | Manufacturer's name                                        |
| tractors[].parameters.model           | string  | Model                                                      |
| tractors[].parameters.price           | integer | Price                                                      |
| tractors[].parameters.year            | string  | Year of manufacture, date format (YYYY-MM-DD)              |
| tractors[].parameters.condition       | string  | Condition                                                  |
| tractors[].parameters.hours           | integer | Opering hours                                              |
| tractors[].parameters.engine_power    | integer | Maximum performane in kWh                                  |
| tractors[].parameters.documents_valid | string  | Validity of the documents, date format (YYYY-MM-DD)        |
| tractors[].parameters.documents_type  | string  | Type of the Documents                                      |
| tractors[].parameters.description     | string  | Longer description                                         |
| tractors[].parameters.image_url       | string  | URL of the tractor's image                                 |
| tractors[].parameters.fuel_type       | string  | Fuel type                                                  |
| tractors[].parameters.equipment[]     | list    | Equipment list (string)                                    |
| tractors[].mark.price                 | boolean | Marked if this tractor is the best based on this parameter |
| tractors[].mark.year                  | boolean | Marked if this tractor is the best based on this parameter |
| tractors[].mark.hours                 | boolean | Marked if this tractor is the best based on this parameter |
| tractors[].mark.engine_power          | boolean | Marked if this tractor is the best based on this parameter |
| tractors[].mark.documents_valid       | boolean | Marked if this tractor is the best based on this parameter |

Otherwise the following structure is returned:

```text
{
  "error_code": integer
}
```

| Property name | Value   | Description                         |
|:--------------|:--------|:------------------------------------|
| error_code    | integer | See the table below for the details |

| Error code | Description           |
|:-----------|:----------------------|
| 1          | Invalid list provided |
