# Entrega 3 - Diseño de la experimentación y POC de servicio

## Entrega 3 - Video explicación desarrollo

En el siguiente enlace encontrará el video con los requerimientos solicitados en la entrega 3:
- [Video - Entrega 3](https://uniandes-my.sharepoint.com/:v:/g/personal/j_padilla_uniandes_edu_co/ERqlYuuoMfNLhz1yfFIVFwcBmSHcUkOpIFu1-KxIwbXwUw?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=huwEcU)

## Entrega 3 - Escenarios de calidad

En la carpeta <code>docs</code> del repositorio se encuentra un archivo .pdf con nombre <strong>Entrega 3 - Escenarios de Calidad</strong> donde se documenta por cada atributo de calidad 3 escenarios de calidad los cuales son: Escalabilidad, Disponibilidad y Configurabiliad/Extensibilidad. Tambien el documento esta disponible en el siguiente enlace para una mejor visualización:

- [Documento - Entrega 3](https://uniandes-my.sharepoint.com/:p:/g/personal/j_padilla_uniandes_edu_co/ETVk5NSPeEhJl95tI7QC2S8BlmiZJg9NpB_JtF3LAc-JyA?e=F1EmUi)

<strong>Importante:</strong> Para el experimento se utilizó como base el escenario de calidad #4 correspondiente al atributo de calidad de disponiblidad para la implementación de los servicios de la arquitectura de solución siguiendo los <strong>principios de DDD</strong> y una aruitectura basada en <strong>eventos</strong>.

## Entrega 3 - Estructura del proyecto

La estructura del proyecto esta basada de la siguiente forma:

- src: En este directorio encuentra el código fuente del proyecto como se describea continuación utilizando una arquitectura hexagonal:
  - SaludTech
    - api
    - config
    - modulos
      - gestor_archivos
        - aplicación
        - dominio
        - infraestructura
    - seedwork
      - aplicacion
      - dominio
      - infraestructura
      - presentacion
  - Anonimizador
- docs: Directorio con los archivos correspondiente de documentación.
- .gitignore: Archivo con la definición de archivos que se deben ignorar en el repositorio GIT.
- .gitpod.yml: Archivo que define las tareas/pasos a ejecutar para configurar su workspace en Gitpod.
- docker-compose.yml: Archivo que define el entorno de contenedores para Apache Pulsar, configurando servicios esenciales como ZooKeeper, BookKeeper y un broker para gestionar la mensajería distribuida.
- README.md: La documentación del proyecto de SaludTech.
- requirements.txt: Archivo con los requerimientos para el correcto funcionamiento del proyecto librerias Python.

<strong>Importante:</strong> A nivel de código se puede evidenciar el uso de entidades, objetos valor, seedwork, servicios, módulos, agregaciones, fabricas, repositorio, puertos, adpatadores, persistencia en base de datos sql y comunicación entre módulos por medio de eventos y comandos usando el patrón CQS.

## Entrega 3 - Ejecución del proyecto

> [!NOTE]  
> Se necesita para correr el proyecto tener instalado pip == 22.2.2 y python 3.10.7

A continuación, se describen los pasos para correr el proyecto:

1. Correr los siguientes comandos para crear el directorio data, en caso de que no exista:
   ```bash
    sudo mkdir -p ./data/zookeeper ./data/bookkeeper
    sudo chown -R 10000 data
   ```
2. Ejecutar el manejador de contenedoras con el siguiente comando: `docker compose up` para inicia Apache Pulsar y sus dependencias asociadas.
3. Instalar las dependencias con `pip install -r requirements.txt` necesarias para el proyecto.
4. Ejecutar aplicación SaludTech con el siguiente comando: `flask --app src/saludTech/api/ run` este corre en el puerto 5000.
5. En otra terminal ejecutar el anonimizador con el siguiente comando: `python /src/anonimizador/main.py`.
6. Abrir postman y realizar una péticion de tipo POST a la url `localhost:5000/imagen_medica` y mandar el objeto para la ejecución correcta.
   ```bash
    { 
       "url": "www.imagen-medica.com",
       "metadata": {
          "tipo": "rayos-x"
          "formato": "lateral femur"
       }
    }
   ```
