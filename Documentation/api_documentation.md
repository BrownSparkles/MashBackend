# API Documentation for `/ai-categories`

## Endpoint

```
GET /ai-categories
```

## Description

Returns a themed set of MASH game categories using Gemini AI. Each category contains a name and four creative options.

## Query Parameters

| Parameter | Type   | Required | Description                              |
|-----------|--------|----------|------------------------------------------|
| `theme`   | string | No       | Theme for the MASH game. Default: "classic". |

## Success Response

**Code:** `200 OK`  
**Content-Type:** `application/json`

```json
{
  "mash_game_categories": [
    {
      "category": "Home",
      "options": ["Mansion", "Apartment", "Shack", "House"]
    },
    {
      "category": "Partner",
      "options": ["The Dashing Explorer", "The Brilliant Scholar", "The Enigmatic Socialite", "The Steadfast Heir/Heiress"]
    }
    // etc...
  ]
}
```

## Error Responses

| Code | Description              |
|------|--------------------------|
| 400  | Missing or invalid input |
| 500  | Internal server/API error |

## Notes

- The `mash_game_categories` array is always returned if the theme is valid and the AI responds correctly.
- This API is ideal for client-side consumption via JavaScript.