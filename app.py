from flask import Flask, render_template
from monday_api import get_board_items

app = Flask(__name__)

@app.route("/")
def home():

    deals = get_board_items(5030484791)
    workorders = get_board_items(5030483475)

    deal_items = deals["data"]["boards"][0]["items_page"]["items"]
    work_items = workorders["data"]["boards"][0]["items_page"]["items"]

    total_deals = len(deal_items)
    total_workorders = len(work_items)

    return render_template(
        "index.html",
        deals=deals,
        workorders=workorders,
        total_deals=total_deals,
        total_workorders=total_workorders
    )
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)