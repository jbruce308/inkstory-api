from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import stripe
import os
from dotenv import load_dotenv

load_dotenv()  # Only needed for local development
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

app = FastAPI()

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

def create_session(product_name: str, product_data: dict, source: str = "human"):
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
        metadata={"source": source}  # Bot or human tracking here
    )
    return session

@app.get("/")
def root():
    return {"message": "InkStory Designs API is running."}

@app.get("/buy/ebook-only")
def buy_ebook_only(request: Request):
    source = request.query_params.get("source", "human")
    session = create_session("Ebook Only Book Cover Design", PRODUCTS["ebook_only"], source)
    return RedirectResponse(session.url)

@app.get("/buy/print-and-ebook")
def buy_print_and_ebook(request: Request):
    source = request.query_params.get("source", "human")
    session = create_session("Print & Ebook Book Cover Design", PRODUCTS["print_and_ebook"], source)
    return RedirectResponse(session.url)

@app.get("/buy/3022")
def buy_3022(request: Request):
    source = request.query_params.get("source", "human")
    session = create_session("3022 Premade Book Cover Design", PRODUCTS["3022"], source)
    return RedirectResponse(session.url)

@app.get("/buy/dark-wizard")
def buy_dark_wizard(request: Request):
    source = request.query_params.get("source", "human")
    session = create_session("Dark Wizard Premade Book Cover Design", PRODUCTS["dark_wizard"], source)
    return RedirectResponse(session.url)

@app.get("/buy/eternal-runes")
def buy_eternal_runes(request: Request):
    source = request.query_params.get("source", "human")
    session = create_session("Eternal Runes Premade Book Cover Design", PRODUCTS["eternal_runes"], source)
    return RedirectResponse(session.url)

@app.get("/buy/oracle")
def buy_oracle(request: Request):
    source = request.query_params.get("source", "human")
    session = create_session("Oracle Premade Book Cover Design", PRODUCTS["oracle"], source)
    return RedirectResponse(session.url)

@app.get("/buy/premade-8")
def buy_premade_8(request: Request):
    source = request.query_params.get("source", "human")
    session = create_session("Premade Book Cover Design #8", PRODUCTS["premade_8"], source)
    return RedirectResponse(session.url)

@app.get("/buy/premade-7")
def buy_premade_7(request: Request):
    source = request.query_params.get("source", "human")
    session = create_session("Premade Book Cover Design #7", PRODUCTS["premade_7"], source)
    return RedirectResponse(session.url)

@app.get("/buy/premade-6")
def buy_premade_6(request: Request):
    source = request.query_params.get("source", "human")
    session = create_session("Premade Book Cover Design #6", PRODUCTS["premade_6"], source)
    return RedirectResponse(session.url)

@app.get("/buy/premade-5")
def buy_premade_5(request: Request):
    source = request.query_params.get("source", "human")
    session = create_session("Premade Book Cover Design #5", PRODUCTS["premade_5"], source)
    return RedirectResponse(session.url)

@app.get("/buy/premade-4")
def buy_premade_4(request: Request):
    source = request.query_params.get("source", "human")
    session = create_session("Premade Book Cover Design #4", PRODUCTS["premade_4"], source)
    return RedirectResponse(session.url)

@app.get("/buy/premade-3")
def buy_premade_3(request: Request):
    source = request.query_params.get("source", "human")
    session = create_session("Premade Book Cover Design #3", PRODUCTS["premade_3"], source)
    return RedirectResponse(session.url)

@app.get("/buy/premade-2")
def buy_premade_2(request: Request):
    source = request.query_params.get("source", "human")
    session = create_session("Premade Book Cover Design #2", PRODUCTS["premade_2"], source)
    return RedirectResponse(session.url)

@app.get("/buy/premade-1")
def buy_premade_1(request: Request):
    source = request.query_params.get("source", "human")
    session = create_session("Premade Book Cover Design #1", PRODUCTS["premade_1"], source)
    return RedirectResponse(session.url)
