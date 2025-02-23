# Entrega 3 - Diseño de la experimentación y POC de servicio

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
