import pyautogui
import time
import requests

# Obtener el tamaño de la pantalla
screen_width, screen_height = pyautogui.size()

# Función para calcular las coordenadas del centro de la pantalla
def halfScreen():
    percentX = screen_width / 2
    percentY = screen_height / 2
    return percentX, percentY

# URL para abrir en Chrome
url = "https://tvgo.americatv.com.pe/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Función para comprobar si la URL devuelve el código de estado 200
def check_status(url):
    try:
        response = requests.get(url, headers=headers)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"Error comprobando el estado: {e}")
        return False

# Esperar hasta que la URL devuelva el código de estado 200
while not check_status(url):
    print("Esperando que el sitio esté disponible...")
    time.sleep(5)

# Abrir Chrome con la URL especificada
pyautogui.hotkey("win", "r")
time.sleep(2)
# pyautogui.write(f'chrome.exe --start-maximized "{url}"', interval=0.02)
pyautogui.write(f'firefox.exe "{url}"', interval=0.02)
time.sleep(2)
pyautogui.press("enter")
time.sleep(5)

# Rutas de las imágenes
# america_image = "data/america.png"  # Ruta de la imagen de América
ver_en_vivo_image = "data/ver_en_vivo.jpeg"  # Ruta de la imagen del botón "Ver en vivo"

# Esperar un poco antes de buscar el botón de reproducir
time.sleep(10)

# Bucle para hacer clic en el botón de reproducir
while True:
    location = pyautogui.locateOnScreen(ver_en_vivo_image, confidence=0.8)  # Ajustar el nivel de confianza según sea necesario
    if location is not None:
        pyautogui.click(location)
        break
    time.sleep(1)

# Presionar 'f' para entrar en pantalla completa
percentX, percentY = halfScreen()
time.sleep(10)
# Hacer click en el centro de la pantalla
pyautogui.click(percentX, percentY)
time.sleep(3)
pyautogui.press("f")