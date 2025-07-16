# -*- coding: cp1252 -*-
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Response, Header, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.responses import FileResponse
import stripe
import os
from pydantic import BaseModel

class BuyResponse(BaseModel):
    url: str

load_dotenv()  # Only needed for local development

stripe_key = os.environ.get("STRIPE_SECRET_KEY")
print("Stripe key:", stripe_key)  # optional, for debugging only

stripe.api_key = stripe_key

if not stripe.api_key:
    raise ValueError("STRIPE_SECRET_KEY environment variable is not set!")

app = FastAPI()

# Stripe webhook secret - used to verify Stripe event signatures
STRIPE_WEBHOOK_SECRET = "we_1RlIbjDwgsjml47rRhYAKwBM"

# Telegram bot token (replace with your actual token)
TELEGRAM_BOT_TOKEN = "7619157567:AAHbfrWjZSDPw1oQ_h00Of3J6hKNf8w7f78"

# Telegram API URL to send messages through your bot
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.api_route("/", methods=["GET", "HEAD"])
async def root(request: Request):
    if request.method == "HEAD":
        return Response(status_code=200)
    return {"message": "Hello World"}

# Add this route to serve the ai-plugin.json manifest at /.well-known/ai-plugin.json
@app.get("/.well-known/ai-plugin.json")
def serve_plugin_manifest():
    return FileResponse(os.path.join(BASE_DIR, "ai-plugin.json"))

SUCCESS_URL = "https://inkstorydesigns.com/#thanks-for-ordering"
CANCEL_URL = "https://inkstorydesigns.com"

PRODUCTS = {
    "ebook_only": {
        "price_cents": 49900,
        "image_url": None
    },
    "print_and_ebook": {
        "price_cents": 69900,
        "image_url": None
    },
    "3022": {
        "price_cents": 500000,
        "image_url": "https://inkstorydesigns.com/assets/images/image21.jpg?v=0e3cd7da"
    },
    "dark_wizard": {
        "price_cents": 390000,
        "image_url": "https://inkstorydesigns.com/assets/images/image30.jpg?v=0e3cd7da"
    },
    "eternal_runes": {
        "price_cents": 270000,
        "image_url": "https://inkstorydesigns.com/assets/images/image32.jpg?v=0e3cd7da"
    },
    "oracle": {
        "price_cents": 100000,
        "image_url": "https://inkstorydesigns.com/assets/images/image14.jpg?v=0e3cd7da"
    },
    "premade_8": {
        "price_cents": 90000,
        "image_url": "https://inkstorydesigns.com/assets/images/image17.jpg?v=0e3cd7da"
    },
    "premade_7": {
        "price_cents": 110000,
        "image_url": "https://inkstorydesigns.com/assets/images/image16.jpg?v=0e3cd7da"
    },
    "premade_6": {
        "price_cents": 80000,
        "image_url": "https://inkstorydesigns.com/assets/images/image13.jpg?v=0e3cd7da"
    },
    "premade_5": {
        "price_cents": 99000,
        "image_url": "https://inkstorydesigns.com/assets/images/image11.jpg?v=0e3cd7da"
    },
    "premade_4": {
        "price_cents": 90000,
        "image_url": "https://inkstorydesigns.com/assets/images/image12.jpg?v=0e3cd7da"
    },
    "premade_3": {
        "price_cents": 120000,
        "image_url": "https://inkstorydesigns.com/assets/images/image03.jpg?v=0e3cd7da"
    },
    "premade_2": {
        "price_cents": 90000,
        "image_url": "https://inkstorydesigns.com/assets/images/image05.jpg?v=0e3cd7da"
    },
    "premade_1": {
        "price_cents": 60000,
        "image_url": "https://inkstorydesigns.com/assets/images/image04.jpg?v=0e3cd7da"
    },
}

def create_session(product_name: str, product_data: dict, metadata: dict = None):
    stripe_product = {"name": product_name}
    if product_data.get("image_url"):
        stripe_product["images"] = [product_data["image_url"]]

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": stripe_product,
                "unit_amount": product_data["price_cents"],
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url=SUCCESS_URL,
        cancel_url=CANCEL_URL,
        metadata=metadata or {}
    )
    return session

@app.get("/")
def root():
    return {"message": "InkStory Designs API is running."}

# Buy endpoints
@app.get("/buy/ebook-only", response_model=BuyResponse)
def buy_ebook_only(request: Request):
    telegram_user_id = request.query_params.get("telegram_user_id")
    session = create_session(
        "Ebook Only Book Cover Design",
        PRODUCTS["ebook_only"],
        metadata={"telegram_user_id": telegram_user_id} if telegram_user_id else None
    )
    return RedirectResponse(session.url)

@app.get("/buy/print-and-ebook", response_model=BuyResponse)
def buy_print_and_ebook(request: Request):
    telegram_user_id = request.query_params.get("telegram_user_id")
    session = create_session(
        "Print & Ebook Book Cover Design",
        PRODUCTS["print_and_ebook"],
        metadata={"telegram_user_id": telegram_user_id} if telegram_user_id else None
    )
    return RedirectResponse(session.url)

@app.get("/buy/3022", response_model=BuyResponse)
def buy_3022(request: Request):
    telegram_user_id = request.query_params.get("telegram_user_id")
    session = create_session(
        "3022 Premade Book Cover Design",
        PRODUCTS["3022"],
        metadata={"telegram_user_id": telegram_user_id} if telegram_user_id else None
    )
    return RedirectResponse(session.url)

@app.get("/buy/dark-wizard", response_model=BuyResponse)
def buy_dark_wizard(request: Request):
    telegram_user_id = request.query_params.get("telegram_user_id")
    session = create_session(
        "Dark Wizard Premade Book Cover Design",
        PRODUCTS["dark_wizard"],
        metadata={"telegram_user_id": telegram_user_id} if telegram_user_id else None
    )
    return RedirectResponse(session.url)

@app.get("/buy/eternal-runes", response_model=BuyResponse)
def buy_eternal_runes(request: Request):
    telegram_user_id = request.query_params.get("telegram_user_id")
    session = create_session(
        "Eternal Runes Premade Book Cover Design",
        PRODUCTS["eternal_runes"],
        metadata={"telegram_user_id": telegram_user_id} if telegram_user_id else None
    )
    return RedirectResponse(session.url)

@app.get("/buy/oracle", response_model=BuyResponse)
def buy_oracle(request: Request):
    telegram_user_id = request.query_params.get("telegram_user_id")
    session = create_session(
        "Oracle Premade Book Cover Design",
        PRODUCTS["oracle"],
        metadata={"telegram_user_id": telegram_user_id} if telegram_user_id else None
    )
    return RedirectResponse(session.url)

@app.get("/buy/premade-8", response_model=BuyResponse)
def buy_premade_8(request: Request):
    telegram_user_id = request.query_params.get("telegram_user_id")
    session = create_session(
        "Premade Book Cover Design #8",
        PRODUCTS["premade_8"],
        metadata={"telegram_user_id": telegram_user_id} if telegram_user_id else None
    )
    return RedirectResponse(session.url)

@app.get("/buy/premade-7", response_model=BuyResponse)
def buy_premade_7(request: Request):
    telegram_user_id = request.query_params.get("telegram_user_id")
    session = create_session(
        "Premade Book Cover Design #7",
        PRODUCTS["premade_7"],
        metadata={"telegram_user_id": telegram_user_id} if telegram_user_id else None
    )
    return RedirectResponse(session.url)

@app.get("/buy/premade-6", response_model=BuyResponse)
def buy_premade_6(request: Request):
    telegram_user_id = request.query_params.get("telegram_user_id")
    session = create_session(
        "Premade Book Cover Design #6",
        PRODUCTS["premade_6"],
        metadata={"telegram_user_id": telegram_user_id} if telegram_user_id else None
    )
    return RedirectResponse(session.url)

@app.get("/buy/premade-5", response_model=BuyResponse)
def buy_premade_5(request: Request):
    telegram_user_id = request.query_params.get("telegram_user_id")
    session = create_session(
        "Premade Book Cover Design #5",
        PRODUCTS["premade_5"],
        metadata={"telegram_user_id": telegram_user_id} if telegram_user_id else None
    )
    return RedirectResponse(session.url)

@app.get("/buy/premade-4", response_model=BuyResponse)
def buy_premade_4(request: Request):
    telegram_user_id = request.query_params.get("telegram_user_id")
    session = create_session(
        "Premade Book Cover Design #4",
        PRODUCTS["premade_4"],
        metadata={"telegram_user_id": telegram_user_id} if telegram_user_id else None
    )
    return RedirectResponse(session.url)

@app.get("/buy/premade-3", response_model=BuyResponse)
def buy_premade_3(request: Request):
    telegram_user_id = request.query_params.get("telegram_user_id")
    session = create_session(
        "Premade Book Cover Design #3",
        PRODUCTS["premade_3"],
        metadata={"telegram_user_id": telegram_user_id} if telegram_user_id else None
    )
    return RedirectResponse(session.url)

@app.get("/buy/premade-2", response_model=BuyResponse)
def buy_premade_2(request: Request):
    telegram_user_id = request.query_params.get("telegram_user_id")
    session = create_session(
        "Premade Book Cover Design #2",
        PRODUCTS["premade_2"],
        metadata={"telegram_user_id": telegram_user_id} if telegram_user_id else None
    )
    return RedirectResponse(session.url)

@app.get("/buy/premade-1", response_model=BuyResponse)
def buy_premade_1(request: Request):
    telegram_user_id = request.query_params.get("telegram_user_id")
    session = create_session(
        "Premade Book Cover Design #1",
        PRODUCTS["premade_1"],
        metadata={"telegram_user_id": telegram_user_id} if telegram_user_id else None
    )
    return RedirectResponse(session.url)

# Stripe Webhook for Telegram Thank-You Message
@app.post("/stripe-webhook")
async def stripe_webhook(request: Request, stripe_signature: str = Header(None)):
    payload = await request.body()

    try:
        event = stripe.Webhook.construct_event(
            payload, stripe_signature, STRIPE_WEBHOOK_SECRET
        )
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid Stripe signature")

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        telegram_user_id = session.get("metadata", {}).get("telegram_user_id")

        if telegram_user_id:
            message = (
                "Thank you for your order!\n\n"
                "Next fill out a book cover order form here https://inkstorydesigns.com/#book-cover-design-order-form\n\n"
                "We're getting started on your book cover now. We'll email it you within 3–5 days after it is finished.\n\n"
                "If you have any questions, just reply here."
            )

            async with httpx.AsyncClient() as client:
                telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
                await client.post(
                    telegram_url,
                    json={"chat_id": telegram_user_id, "text": message}
                )

    return {"status": "success"}
