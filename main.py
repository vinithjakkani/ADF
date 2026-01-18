from fastapi import FastAPI, Response
import datetime
import json

app = FastAPI()

@app.get("/api/v1/orders")
def get_orders():
    #current_hour = datetime.datetime.now().hour
    now=datetime.datetime.now()

    # Simulate corruption during midnight window
    #if current_hour == 1 and current_hour.minute < 10:
    if now.minute < 55:
        corrupted_json = """
        {
          "order_id": 10234,
          "customer": "John Doe",
          "amount": 450.75,
          "currency": "USD",
          "items": [
            {"sku": "SKU123", "qty": 2},
            {"sku": "SKU456", "qty": 1}
          ]
        """  # ❌ Missing closing brace

        return Response(
            content=corrupted_json,
            media_type="application/json"
        )

    # Normal valid response
    valid_json = {
        "order_id": 10235,
        "customer": "Jane Smith",
        "amount": 299.99,
        "currency": "USD",
        "items": [
            {"sku": "SKU789", "qty": 1}
        ]
    }

    return valid_json
