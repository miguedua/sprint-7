# Sprint 7 – Proyecto Final de la aplicacion   

Descripción del Proyecto
Este proyecto es una aplicación web interactiva desarrollada con Streamlit, creada como parte del Sprint 7 del bootcamp de análisis de datos.
Su objetivo es permitir la visualización dinámica y exploratoria de datos del archivo vehicles_us.csv, el cual contiene información sobre vehículos en Estados Unidos.
La aplicación ofrece una interfaz intuitiva donde el usuario puede elegir qué tipo de gráfico desea visualizar, facilitando el análisis de las variables sin necesidad de escribir código.

⚙️ Funcionalidades principales
Carga de datos:
El programa lee el archivo vehicles_us.csv y lo convierte en un DataFrame de pandas para su análisis.
Interfaz interactiva:
A través de casillas de verificación (checkboxes), el usuario puede seleccionar el tipo de visualización que desea explorar:
✅ Histograma: muestra la distribución de cualquier columna seleccionada.
✅ Diagrama de dispersión: permite comparar dos variables numéricas entre sí.
Visualizaciones con Plotly:
Los gráficos se generan con Plotly Express, lo que proporciona visualizaciones interactivas y atractivas.
Diseño adaptable:
Si el usuario no selecciona ninguna opción, la aplicación muestra un mensaje informativo que invita a comenzar la exploración.
