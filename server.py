from flask import Flask, jsonify, request

app = Flask(__name__)

leads = []

def responder(msg):
    msg = msg.lower()

    if "preço" in msg or "valor" in msg:
        return "Entendi! Posso te mandar uma proposta melhor."

    if "quero" in msg or "site" in msg:
        return "Perfeito! Posso te mostrar como ficaria seu site."

    return "Olá! Posso te explicar como funciona."

@app.route("/")
def home():
    return "🔥 Jarvis rodando no GitHub (precisa rodar localmente)"

@app.route("/lead", methods=["POST"])
def lead():
    data = request.json or {}
    msg = data.get("message", "")

    reply = responder(msg)

    leads.append({"message": msg, "reply": reply})

    return jsonify({"reply": reply})

@app.route("/leads")
def get_leads():
    return jsonify(leads)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
    server.py
