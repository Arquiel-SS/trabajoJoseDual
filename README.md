# TRABAJO JOSÉ BACKEND 
Este trabajo es una de las dos partes que conforman una entrega entre la asignatura de Entornos de Desarrollo y Lenguaje de Marcas. En esta sección nos encargamos de crear una web sin diseño para priorizar la funcionalidad de backend por un motivo de tiempo dentro del grupo. 

## SECCIONES
#### FORMULARIOS
La web constará de una red de formularios que aparecen como opciones en la raíz del proyecto, donde podremos crear:
* **Integrantes** de un grupo musical (un mismo integrante puede aparecer en varios grupos)
* **Grupos musicales** compuestos por integrantes (si no hay integrantes, no puedes crear grupos)
* **Conciertos**, en los cuales participan grupos musicales (si no hay grupos, no puedes crear conciertos)

Estos 3 puntos son clases de nuestro modelo de base de datos, donde cada uno actúa como una entidad con sus respectivos atributos, almacenándose tras su proceso de creación.

#### FLUJO DE PRESENTACIÓN DE LA INFORMACIÓN
Una vez toda la información se ha creado, se podrá consultar mediante otra opción del menú principal. Este nos devolverá por pantalla toda la información en nuestra BBDD de manera organizada por los 3 grupos (Integrantes, Grupos y Conciertos). 

Aquí tendremos la opción de, además, filtrar por relaciones entre distintas entidades. Por ejemplo, buscar por id de grupo y que salgan todos los conciertos en los que participa ese grupo. Buscar por id de integrante y ver en cuántos grupos participa.

#### Tecnologías utilizadas y procedimiento de la aplicación
Los formularios se crean mediante el uso de Flask y HTML (usando la librería de jinja2). Necesitaremos tener un entorno preparado con dichas dependencias o sino instalarlas manualmente.

Accederemos a la aplicación activando el servidor principal en "app.py", tendremos 6 endpoints disponibles:
- /crear_integrante: Formulario html para crear un integrante
- /crear_grupo: Formulario html para crear un grupo (depende de que haya integrantes)
- /crear_concierto: Formulario html para crear un concierto (depende de que haya grupos)
- /ver_info: Imprimir por pantalla, separado por secciones,todos los integrantes, grupos y conciertos ordenados.
- /integrante/< id >: Acceder desde la url a un ID de integrante y te devuelve en qué grupos participa
- /grupo/< id >: Acceder desde la url a un ID de grupo y te devuelve cuántos conciertos tienen y cuándo son cada uno  