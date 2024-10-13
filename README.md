Comic Collection Manager

Descripción

El Comic Collection Manager es una aplicación web desarrollada en Django que permite a los usuarios gestionar su colección de cómics. Los usuarios pueden agregar cómics a su catálogo personal, crear colecciones personalizadas y clasificar los cómics según diferentes categorías. La aplicación está diseñada para facilitar el seguimiento de los cómics que poseen, permitiendo una fácil organización y visualización.

Funcionalidades

Gestión de cómics: Los usuarios pueden agregar, editar y eliminar cómics de su colección personal.
Creación de colecciones personalizadas: Los usuarios pueden crear múltiples colecciones para organizar sus cómics, y agregar cómics a esas colecciones.

Autenticación de usuarios: Los usuarios pueden registrarse, iniciar sesión y tener acceso a sus colecciones personales.
Modelos principales.

User: Los usuarios registrados pueden crear y gestionar sus colecciones.

Comic: Cada cómic tiene un título, autor, editorial, y  un campo para el número de entrega.

Colección: Un usuario puede tener múltiples colecciones, y cada colección contiene varios cómics.

Instalación

Clona el repositorio:


bash
Copy code
git clone https://github.com/lramer/Entrega_final_Python_60070_Ramer_Laura.git
cd Entrega_final_Python_60070_Ramer_Laura

Crea y activa un entorno virtual:

bash
Copy code
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate

Instala las dependencias:

bash
Copy code
pip install -r requirements.txt

Configura las migraciones y la base de datos:

bash
Copy code
python manage.py migrate

Inicia el servidor:

bash
Copy code
python manage.py runserver

Accede a la aplicación en el navegador:


Copy code
http://localhost:8000/inicio/

Uso

Regístrate o inicia sesión para empezar a gestionar tu colección de cómics.
Agrega nuevos cómics y organiza tus colecciones personalizadas.


Licencia
Este proyecto está bajo la licencia MIT. Para más información, consulta el archivo LICENSE.