![alt text](https://github.com/c4ttivo/MLOpsTaller1/blob/main/mlopstaller1/imgs/logo.png?raw=true)

# MLOps - Proyecto 2
## Autores
*    Daniel Crovo (dcrovo@javeriana.edu.co)
*    Hugo Poveda (h.poveda@javeriana.edu.co)
*    Carlos Trujillo (ca.trujillo@javeriana.edu.co)

## Profesor
*    Cristian Diaz (diaz.cristian@javeriana.edu.co)

## Arquitectura

![alt text](https://github.com/c4ttivo/MLOPS-Project2/blob/main/img/architecture.png?raw=true)

## Instrucciones
Clone el repositorio de git usando el siguiente comando en la consola de su sistema operativo:


```
# git clone https://github.com/c4ttivo/MLOPS-Project2.git
```

Una vez ejecutado el comando anterior aparece el folder MLOPS-Project2. Luego es necesario ubicarse en el directorio de trabajo en el que se encuentra el archivo docker-compose.yml.


```
# cd MLOPS-Project2/
```

Ahora es necesario construir los contenedores


```
# sudo docker-compose run
```
En este paso se descarga las imágenes de acuerdo con lo especificado en el archivo docker-compose.yml.

<img src="https://github.com/c4ttivo/MLOPS-Project2/blob/main/img/console.png?raw=true" width="50%" height="50%" />

Una vez finalizada la creación de los contenedores, se debe poder ingresar a las aplicaciones de cada contenedor a través de las siguientes URLs:

http://10.43.101.155:8083/ </br>
<img src="https://github.com/c4ttivo/MLOPS-Project2/blob/main/img/minio.png?raw=true" width="50%" height="50%" />
http://10.43.101.155:8082/ </br>
<img src="https://github.com/c4ttivo/MLOPS-Project2/blob/main/img/mlflow.png?raw=true" width="50%" height="50%" />
http://10.43.101.155:8080/ </br>
<img src="https://github.com/c4ttivo/MLOPS-Project2/blob/main/img/airflow.png?raw=true" width="50%" height="50%" />



![alt text](https://github.com/c4ttivo/MLOpsTaller1/blob/main/mlopstaller1/imgs/fastapi.png?raw=true)

