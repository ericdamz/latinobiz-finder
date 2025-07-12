import time
import random

def scrape_paginas_amarillas(estado, categoria):
    time.sleep(random.uniform(1.5, 3.5))  # Simula espera realista
    return [
        ["Peluquería Latina", "987-654-3210", f"789 Avenida Sol, {estado}", "https://paginasamarillas.com", "amarillas", "Pendiente"],
        ["Consultorio Hispano", "654-321-9870", f"1010 Blvd Centro, {estado}", "https://paginasamarillas.com", "amarillas", "Pendiente"]
    ]
