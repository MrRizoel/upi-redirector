from flask import Flask, redirect, request

app = Flask(__name__)

@app.route("/upi_pay", methods=["GET"])
def redirect_to_upi_payment():
    flink = ""
    upi = request.args.get("upi")
    if upi_payment_link:
        id = upi.split('-')
        upi_payment_link = flink.format(id[0], id[1])
        return redirect(upi_payment_link, code=303)
    else:
        return "Invalid UPI payment link", 400

if __name__ == "__main__":
    app.run()
