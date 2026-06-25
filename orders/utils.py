from escpos.printer import Network
import traceback


"""
{
    "table_name": "table 1",
    "total": 3000,
    "items": [
            {'name': 'Momo (Buff)', 'price': 180, 'qty': 1},
            {'name': 'Momo (Veg)', 'price': 160, 'qty': 1},
            {'name': 'Gundruk Dhido Set', 'price': 350, 'qty': 1},
            {'name': 'Chiura with Tarkari', 'price': 160, 'qty': 1},
            {'name': 'Puri Tarkari', 'price': 140, 'qty': 1},
            {'name': 'Dal Bhat Tarkari (Mutton)', 'price': 500, 'qty': 1},
            {'name': 'Thakali Khana Set', 'price': 450, 'qty': 1},
            {'name': 'Momo (Buff)', 'price': 180, 'qty': 1},
            {'name': 'Momo (Chicken)', 'price': 200, 'qty': 1},
            {'name': 'Dal Bhat Tarkari (Veg)', 'price': 280, 'qty': 1},
            {'name': 'Dal Bhat Tarkari (Veg)', 'price': 280, 'qty': 1},
            {'name': 'Momo (Buff)', 'price': 120, 'qty': 1}
    ]
}



"""

def print_restaurant_receipt(order_data):
    """
    Prints a formatted restaurant receipt.

    Args:
        order_data (dict): Contains:
            - order_id
            - table_no
            - items (list)
            - total
    """

    # Connect to printer
    try:
        # p = Network("localhost", 9100, profile="TM-T88III")
        p = Network("172.17.0.3", 9100, profile="TM-T88III")
    except Exception as e:
        print(f"Printer connection failed: {e}")
        return False

    try:
        # =========================
        # Header
        # =========================
        p.set(
            align="center",
            bold=True,
            font="a",
            double_width=True,
            double_height=True,
        )
        p.text("Nepali Restaurant\n")

        p.set(
            align="center",
            bold=False,
            font="a",
            normal_textsize=True,
        )
        p.text(
            f"Table: {order_data['table_name']} \n"
        )
        p.text("Rainbow Galli, Biratnagar\n")
        p.text("Tel: 023-398479\n")
        p.text("-" * 32 + "\n")

        # =========================
        # Items
        # =========================
        p.set(
            align="left",
            bold=True,
            normal_textsize=True,
        )
        p.text("ORDER ITEMS\n")

        p.set(
            align="left",
            bold=False,
            normal_textsize=True,
        )

        for item in order_data["items"]:
            name = item["name"]
            qty = item.get("qty", 1)
            price = item["price"]

            line = f"{qty}x {name}"
            price_text = f"Rs. {price:.2f}"

            padding = max(1, 32 - len(line) - len(price_text))

            p.text(
                f"{line}{'.' * padding}{price_text}\n"
            )

        p.text("-" * 32 + "\n")

        # =========================
        # Total
        # =========================
        p.set(
            align="right",
            bold=True,
            double_width=True,
            double_height=True,
        )
        p.text(f"TOTAL: Rs. {order_data['total']:.2f}\n")

        # =========================
        # Footer
        # =========================
        p.set(
            align="center",
            bold=False,
            normal_textsize=True,
        )

        p.text("\nThank you for dining with us!\n")

        # =========================
        # QR Code
        # =========================
        p.text("\nScan for Feedback:\n")

        try:
            p.qr("https://codeit.com.np/")
            print("QR created")
        except Exception:
            p.text(
                "https://codeit.com.np/\n"
            )

        # =========================
        # Cut
        # =========================
        p.text("\n\n")
        p.cut()

        try:
            p.close()
        except Exception:
            pass

        return True

    except Exception:
        print("Print error:")
        traceback.print_exc()

        try:
            p.close()
        except Exception:
            pass

        return False


# =========================
# Example Usage
# =========================
if __name__ == "__main__":
    sample_order = {
        "order_id": 1024,
        "table_no": 5,
        "items": [
            {
                "name": "Classic Burger",
                "price": 12.50,
                "qty": 2,
            },
            {
                "name": "Cheese Fries",
                "price": 4.50,
                "qty": 1,
            },
            {
                "name": "Coke Zero",
                "price": 2.00,
                "qty": 2,
            },
        ],
        "total": 31.50,
    }

    if print_restaurant_receipt(sample_order):
        print("Receipt sent successfully!")
    else:
        print("Failed to print receipt.")