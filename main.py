import webview
import random
import json
import os

# Model AI (symulacja wykrywania oszustw)
class AIModel:
    def __init__(self):
        self.sensitivity = 0.5  # Domyślna czułość (50%)

    def predict_transaction(self, amount, location, time):
        """Symulacja analizy transakcji z uwzględnieniem czułości"""
        fraud_probability = random.random()
        risk = "Podejrzana 🚨" if fraud_probability < self.sensitivity else "Bezpieczna ✅"
        return {"status": risk, "amount": amount, "location": location, "time": time}

    def set_sensitivity(self, sensitivity):
        self.sensitivity = float(sensitivity)
        return {"message": f"Czułość zmieniona na {self.sensitivity}"}

# API do obsługi komunikacji z interfejsem
class API:
    def __init__(self):
        self.model = AIModel()
        self.history = []

    def check_transaction(self, amount, location, time):
        result = self.model.predict_transaction(float(amount), location, time)
        self.history.append(result)
        return result

    def get_history(self):
        return json.dumps(self.history[-10:])

    def set_sensitivity(self, sensitivity):
        return self.model.set_sensitivity(sensitivity)

api = API()

# Wczytanie pliku HTML
html_path = os.path.abspath("index.html")

# Upewnienie się, że ścieżka do CSS jest poprawna
css_path = os.path.abspath("styles.css")

# Wczytanie HTML i dynamiczne dodanie ścieżki do CSS
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read().replace('styles.css', f"file:///{css_path}")

# Tworzenie okna PyWebview z określoną rozdzielczością
webview.create_window("Analiza Transakcji", html=html_content, js_api=api, width=1280, height=720)
webview.start()
