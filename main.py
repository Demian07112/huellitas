from colorama import Fore
import questionary
from questionary import Style
import json
import msvcrt
from tabulate import tabulate
import os

from src.utils import TERMINAL_WIDTH


datos = {}

with open("./src/databases/dogs.json", "r") as file:
    datos = json.load(file)





DOGGO_ASCCI = """
░▄▀▄▀▀▀▀▄▀▄░░░░░░░░░
░█░░░░░░░░▀▄░░░░░░▄░
█░░▀░░▀░░░░░▀▄▄░░█░█
█░▄░█▀░▄░░░░░░░▀▀░░█
█░░▀▀▀▀░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░░░░█
░█░░▄▄░░▄▄▄▄░░▄▄░░█░
░█░▄▀█░▄▀░░█░▄▀█░▄▀░
░░▀░░░▀░░░░░▀░░░▀░░░
"""



def form(doggy):

    """
        {
            "fullname": "",
            "CI": 55555555,
            "phone": "",
            "address": "",
            "payment_method": ""
        }
    """
    print(Fore.BLUE + "\nFormulario de Compra\n")

    fullname = questionary.text("Nombre Completo:").ask()
    CI = questionary.text("Cédula de Identidad:").ask()
    phone = questionary.text("Número de Teléfono:").ask()
    address = questionary.text("Dirección de Envío:").ask()


    user_data = {
        "fullname": fullname,
        "CI": CI,
        "phone": phone,
        "address": address,
        "dog": doggy
    }

    clients = []

    with open("./src/databases/clients.json", "r") as file:
        clients = json.load(file)
        clients.append(user_data)



    with open("./src/databases/clients.json", "w") as file:
        json.dump(clients, file, indent=2)
        

    print(Fore.GREEN + "\n¡Gracias por su compra! Aquí están los detalles de su pedido:\n")

    # TODO borrar los perritos de la base de datos al comprarlos



    pass

def catalogue():

    print(Fore.BLUE + "\nCatálogo de Perritos\n" + Fore.RESET)

    select_style = Style([('highlighted','fg:#000000 bg:#1e90ff bold')])

    choices = [f"{i}: {dog['breed']} - {'Hembra' if dog['sex'] == 'F' else 'Macho'} - ${dog['price']}" for i, dog in enumerate(datos, start=1)]



    option = questionary.select(
        "Seleccione el perrito que desea ver:\n",
        choices=choices,
        style=select_style
    ).ask()


    current_dog = datos[int(option.split(":")[0]) - 1]
    
    print()
    print(Fore.GREEN + f"Has seleccionado:".center(TERMINAL_WIDTH))
    print(Fore.YELLOW + f'{current_dog['breed']} - {'Hembra' if current_dog['sex'] == 'F' else 'Macho'}'.center(TERMINAL_WIDTH))
    print()


    confirmation = questionary.confirm(f'¿Desea comprar la mascota por ${current_dog['price']}?').ask()

    if confirmation:
        form(current_dog)



    
    print(Fore.RESET)


def start():

    os.system('cls' if os.name == 'nt' else 'clear')


    TITLE = 'Bienvenido a mi Tienda Virtual de Perritos'

    print(Fore.BLUE +  f' {TITLE} '.center(TERMINAL_WIDTH, '='))

    for line in DOGGO_ASCCI.splitlines():
        print(Fore.BLUE + line.center(TERMINAL_WIDTH))

    print('\n' + Fore.BLUE + '=' * TERMINAL_WIDTH)

    print(Fore.CYAN + "Presiona Enter para ver el catálogo de perritos...")


    while True:
        key = msvcrt.getch()

        if key == b'\r':
            break
        elif key == b'\x1b' or key == b'\x03':
            print(Fore.RED + "Saliendo..." + Fore.RESET)  
            return

    catalogue()


    print(Fore.RESET)






def main():
    start()
    

main()











