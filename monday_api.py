import requests
from config import *

URL = "https://api.monday.com/v2"

headers = {
    "Authorization": MONDAY_API_TOKEN,
    "Content-Type": "application/json"
}


def get_board_items(board_id):

    query = f"""
    {{
      boards(ids: {board_id}) {{
        name
        items_page {{
          items {{
            id
            name
            column_values {{
              id
              text
            }}
          }}
        }}
      }}
    }}
    """

    response = requests.post(
        URL,
        json={"query": query},
        headers=headers
    )

    return response.json()