from fastapi import FastAPI
import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env in local dev (ignored in Render)
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "InkStory Designs API is running."}

@app.post("/create-checkout-session")
def create_checkout_session():
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": "Book Cover Design"
                },
                "unit_amount": 49900,  # $499
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url="https://inkstorydesigns.com/thanks",
        cancel_url="https://inkstorydesigns.com/cancel",
    )
    return {"checkout_url": session.url}
