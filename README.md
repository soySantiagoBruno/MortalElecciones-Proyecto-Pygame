# Mortal Elecciones 🎮
![Alt Text](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXRpNzUxampwYXpwbXoybng1MjdxYmhvcHp6a3R3cTNvem8wYTZsdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WFF2A3BRY7UY4beI4e/giphy.gif)


Un juego épico basado en personajes inspirados en figuras públicas, donde se enfrentan en un duelo único. Incluye video introductorio, música de fondo y efectos de sonido. ¡Prepárate para la batalla final!

---

## **Requisitos**

### **Librerías de Python**
- [pygame](https://www.pygame.org/) - Para gráficos, sonido y manejo de eventos del juego.
- [moviepy](https://zulko.github.io/moviepy/) - Para reproducir el video de introducción.

---

## **Instrucciones de Instalación**

### **1. Clonar el repositorio**
```bash
git clone <URL_DEL_REPO>
cd <NOMBRE_DEL_REPO>
```
#### **2. Instalar dependencias**
```bash
python -m pip install --upgrade pip
```
#### **5. Ejecutar el programa**
```bash
python main.py
```
---
## Inspirado en
## Demo

[Firebase deploy](https://prueba-angular-reyesoft.web.app)

## Postman

[Peticiones utilizadas para consumir la API](https://documenter.getpostman.com/view/28664859/2sA3rzJCbR)


## Historias de usuario

- Como usuario, al ingresar al sitio en la ruta `/login`, debo poder ingresar mis datos en un formulario: email y contraseña. Estos datos se corroboran haciendo `POST https://api.saldo.com.ar/bridge/login`.

    Los valores correctos a enviar por POST son `email=admin@saldo.com.ar` y `password=CoolSite`
        Dará error el front-end o ingresará según corresponda.
- Como usuario, si ingreso a la ruta `/login` y ya estoy logueado, debo ser redirigido a `/systems`
- Como usuario, al ingresar a la ruta `/systems` debo poder ver todos los activos que puedo intercambiar en la plataforma saldo.com.ar
- Como usuario, si ingreso a la ruta `/systems` (o cualquier otra distinta a `/login`) y no me encuentro logueado, debo ser redirigido a la página `/login`.
- Como usuario, si ingreso a la ruta `/systems` (o cualquier otra distinta a `/login`) siempre mostrará mi nombre en la parte superior, además de un link a “cerrar sesión”.
- Como usuario, al hacer click en uno de los activos que puedo intercambiar en la plataforma, desea ver sus precios en relación a los demás pares (en vivo, tal cual lo devuelve la API de Saldoar). Esto puede ser en la misma página (/systems) o en otra ruta (por ejemplo, `/systems/:system_id`, en donde system_id es el identificador del activo seleccionado).
- Como usuario, si estoy viendo los precios de un activo específico, deseo poder colapsar o volver a la lista de activos (dependiendo de la implementación por la que se haya optado, sea en la misma página o en una nueva)
- Como usuario, deseo poder desloguearme de la plataforma, siendo redirigido a la página de `/login`.
- Como usuario, al ingresar en cualquier ruta que no esté definida, deseo ser redirigido a `/systems` o `/login`, dependiendo de mi estado de autenticación.

## Tech Stack

**Client:** Angular 18, Bootstrap 5.3


## Demo

[![Demo del juego](https://i.ytimg.com/vi/ATV4SgvDE5c/hqdefault.jpg?sqp=-oaymwE2CPYBEIoBSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB_AmAAtAFigIMCAAQARhlIGUoSzAP&rs=AOn4CLABRuLGFjR1cRqtbQ5auH_-PynZFw)](https://youtu.be/ATV4SgvDE5c "Video demo Mortal Elecciones Pygame")
## Inspiración

Inspirado en el meme de @_martindemarco
[@_martindemarco](https://www.instagram.com/_martindemarco/reel/CyMcocmMZZW/)
