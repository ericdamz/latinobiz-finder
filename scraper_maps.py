import time
import random

def scrape_google_maps(estado, categoria):
    time.sleep(random.uniform(1.5, 3.5))  # Simula espera realista
    return [
        ["Restaurante El Sol", "123-456-7890", f"123 Main St, {estado}", "https://maps.google.com", "maps", "Pendiente"],
        ["Taquería Mi Pueblo", "321-654-0987", f"456 Calle Luna, {estado}", "https://maps.google.com", "maps", "Pendiente"]
    ]
