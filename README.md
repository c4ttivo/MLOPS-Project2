![alt text](https://github.com/c4ttivo/MLOpsTaller1/blob/main/mlopstaller1/imgs/logo.png?raw=true)

# MLOps - Proyecto 2
## Autores
*    Daniel Crovo (dcrovo@javeriana.edu.co)
*    Carlos Trujillo (ca.trujillo@javeriana.edu.co)

## Profesor
*    Cristian Diaz (diaz.cristian@javeriana.edu.co)

## Arquitectura

![alt text](https://github.com/c4ttivo/MLOPS-Project2/blob/main/img/architecture.png?raw=true)

### Descripción de componentes

La solución está compuesta por los siguientes contenedores:

*	**Airflow**: Orquestador para gestionar y programar los flujos de trabajo, relacionados con la recolección de datos, entrenamiento de modelos y registro de experimentos en MLFlow.
*	**MLflow**: Registro de experimentos, seguimiento de métricas y almacenamiento de modelos. Configurado para usar **Minio** para el almacenamiento de objetos y **MySQL** como base de datos para la metadata.
*	**Minio**: Almacen de objetos compatible con S3.
*	**MySQL**: Se encuentran dos servicios, uno de apoyo a MLflow (mysql) y otro para el almacenamiento de la recolección de datos (modeldb).
*	**Inference**: Servicio de FastAPI que consume el modelo entrenado y almacenado en MLflow y que permite hacer inferencias.


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
# sudo docker-compose up
```
En este paso se descarga las imágenes de acuerdo con lo especificado en el archivo docker-compose.yml.

<img src="https://github.com/c4ttivo/MLOPS-Project2/blob/main/img/console.png?raw=true" width="50%" height="50%" />

Una vez finalizada la creación de los contenedores, se debe poder ingresar a las aplicaciones de cada contenedor a través de las siguientes URLs:

http://10.43.101.155:8083/ </br>
<img src="https://github.com/c4ttivo/MLOPS-Project2/blob/main/img/minio.png?raw=true" width="50%" height="50%" /> </br>
http://10.43.101.155:8082/ </br>
<img src="https://github.com/c4ttivo/MLOPS-Project2/blob/main/img/mlflow.png?raw=true" width="50%" height="50%" /> </br>
http://10.43.101.155:8080/ </br>
<img src="https://github.com/c4ttivo/MLOPS-Project2/blob/main/img/airflow.png?raw=true" width="50%" height="50%" /> </br>

## Configuración

Los siguientes pasos permiten realizar la configuración del ambiente luego de ser desplegado.

1.	Dado que la VM está en Linux, se requiere establecer la siguiente variable.
```
	# echo -e "AIRFLOW_UID=$(id -u)" > .env
```	
2.	A continuación se debe configurar el bucket de S3, con el nombre **mlflows3** requerido por **MLflow**.

## Predicción

A través de la interfaz de FastAPI, es posible hacer predicciones usando el modelo almacenado y etiquetado @produccion.

http://10.43.101.155/docs </br>

![alt text](https://github.com/c4ttivo/MLOPS-Project2/blob/dev/img/inference.png?raw=true)

