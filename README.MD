# Entrega 3 - Diseño de la experimentación y POC de servicio

## Entrega 3 - Video explicación desarrollo

En el siguiente enlace encontrará el video con los requerimientos solicitados en la entrega 3:
- [Video - Entrega 3](https://uniandes-my.sharepoint.com/:v:/g/personal/j_padilla_uniandes_edu_co/ERqlYuuoMfNLhz1yfFIVFwcBmSHcUkOpIFu1-KxIwbXwUw?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=huwEcU)

## Entrega 3 - Escenarios de calidad

En la carpeta <code>docs</code> del repositorio se encuentra un archivo .pdf con nombre <strong>Entrega 3 - Escenarios de Calidad</strong> donde se documenta por cada atributo de calidad 3 escenarios de calidad los cuales son: Escalabilidad, Disponibilidad y Configurabiliad/Extensibilidad.

<strong>Importante:</strong> Para el experimento se utilizó como base el escenario de calidad #4 correspondiente al atributo de calidad de disponiblidad para la implementación de los servicios de la arquitectura de solución siguiendo los <strong>principios de DDD</strong> y una aruitectura basada en <strong>eventos</strong>.

## Entrega 3 - Estructura del proyecto

## Entrega 3 - Ejecución del proyecto

> [!NOTE]  
> Se debe tener instalado pip == 22.2.2 y python 3.10.7

## Como correr el proyecto

1. Correr los siguientes comandos para crear el directorio data, en caso de que no exista
   ```bash
    sudo mkdir -p ./data/zookeeper ./data/bookkeeper
    sudo chown -R 10000 data
   ```
2. Correr `docker compose up` lo cual inicia pulsar y sus dependencias
3. Instalar las dependencias con `pip install -r requirements.txt`
4. Correr el api con `flask --app src/saludTech/api/ run`. Este corre en el puerto 5000
5. En otra terminal correr el anonimizador con `python /src/anonimizador/main.py`
