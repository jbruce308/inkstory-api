
# InkStory Book Cover API

This API allows you to order professional book cover designs via simple HTTP requests.

## Base URL

```
https://inkstory-api.onrender.com/
```

## Endpoints

### Root

- **GET /**  
  Returns a simple message to confirm the API is running.

  **Response:**  
  ```json
  { "message": "InkStory Designs API is running." }
  ```

### Plugin Manifest

- **GET /.well-known/ai-plugin.json**  
  Returns the AI plugin manifest JSON file.

### Buy Endpoints

Each endpoint creates a Stripe checkout session for a specific book cover design product and redirects you to the Stripe payment page.

- **GET /buy/ebook-only**  
  Buy the Ebook Only Book Cover Design ($499.00)

- **GET /buy/print-and-ebook**  
  Buy the Print & Ebook Book Cover Design ($699.00)

- **GET /buy/3022**  
  Buy the 3022 Premade Book Cover Design ($5000.00)

- **GET /buy/dark-wizard**  
  Buy the Dark Wizard Premade Book Cover Design ($3900.00)

- **GET /buy/eternal-runes**  
  Buy the Eternal Runes Premade Book Cover Design ($2700.00)

- **GET /buy/oracle**  
  Buy the Oracle Premade Book Cover Design ($1000.00)

- **GET /buy/premade-8**  
  Buy the Premade Book Cover Design #8 ($900.00)

- **GET /buy/premade-7**  
  Buy the Premade Book Cover Design #7 ($1100.00)

- **GET /buy/premade-6**  
  Buy the Premade Book Cover Design #6 ($800.00)

- **GET /buy/premade-5**  
  Buy the Premade Book Cover Design #5 ($990.00)

- **GET /buy/premade-4**  
  Buy the Premade Book Cover Design #4 ($900.00)

- **GET /buy/premade-3**  
  Buy the Premade Book Cover Design #3 ($1200.00)

- **GET /buy/premade-2**  
  Buy the Premade Book Cover Design #2 ($900.00)

- **GET /buy/premade-1**  
  Buy the Premade Book Cover Design #1 ($600.00)

## Success & Cancel URLs

- **Success:** https://inkstorydesigns.com/#thanks-for-ordering  
- **Cancel:** https://inkstorydesigns.com

## Usage Notes

- Stripe checkout URLs are temporary and valid for the session only.
- All prices are in USD and cents (e.g., 49900 = $499.00).
- Make sure your Stripe API key is set in the environment variable `STRIPE_SECRET_KEY`.
- API uses FastAPI and can be run locally or deployed on platforms like Render.

## Example Request

```bash
curl -i https://inkstory-api.onrender.com/buy/ebook-only
```

This will respond with a redirect (HTTP 307) to the Stripe checkout page URL.

---

For more information or support, contact InkStory Designs.
