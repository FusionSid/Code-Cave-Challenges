import os

import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, session

from currencies import supported_currencies

app = Flask(__name__)
load_dotenv()

API_URL = "https://api.apilayer.com/currency_data/convert"
API_KEY = os.environ["API_KEY"]


@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == "POST":
        amount = request.form.get("amount")
        from_currency = request.form.get("from")
        to_currency = request.form.get("to")

        if amount is None or from_currency is None or to_currency is None:
            return render_template(
                "index.html",
                currency_list=[f"{v} ({k})" for k, v in supported_currencies.items()],
                alert_value='<div id="alert-box" class="flex p-4 mb-4 bg-red-100 rounded-lg dark:bg-red-200" role="alert">',
                error="You must give all 3 values (amount, from and to) lmao skill issue",
            )

        try:
            amount = float(amount)
        except ValueError:
            return render_template(
                "index.html",
                currency_list=[f"{v} ({k})" for k, v in supported_currencies.items()],
                alert_value='<div id="alert-box" class="flex p-4 mb-4 bg-red-100 rounded-lg dark:bg-red-200" role="alert">',
                error="Amount must be a number dumbass! just get good tbh",
            )

        from_currency = (from_currency.split("(")[1]).replace(")", "")
        to_currency = (to_currency.split("(")[1]).replace(")", "")

        headers = {"apikey": API_KEY}
        url = f"{API_URL}?to={to_currency}&from={from_currency}&amount={amount}"
        api_response = requests.get(url, headers=headers).json()

        if api_response["success"] == False:
            return render_template(
                "index.html",
                currency_list=[f"{v} ({k})" for k, v in supported_currencies.items()],
                alert_value='<div id="alert-box" class="flex p-4 mb-4 bg-red-100 rounded-lg dark:bg-red-200" role="alert">',
                error="Api had a skill issue :(",
            )

        total = api_response["result"]
        total_html_hidden = """
        <div class="mb-10">
            <h1 class="block text-gray-700 text-sm font-bold mb-2 text-xl">Total: {}</h1>
        </div>
        """.format(
            total
        )
        return render_template(
            "index.html",
            currency_list=[f"{v} ({k})" for k, v in supported_currencies.items()],
            alert_value='<div id="alert-box" class="flex p-4 mb-4 bg-red-100 rounded-lg dark:bg-red-200 hidden" role="alert">',
            total_result=total_html_hidden,
        )

    return render_template(
        "index.html",
        currency_list=[f"{v} ({k})" for k, v in supported_currencies.items()],
        alert_value='<div id="alert-box" class="flex p-4 mb-4 bg-red-100 rounded-lg dark:bg-red-200 hidden" role="alert">',
    )


app.run()
