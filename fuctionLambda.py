# Importamos el paquete de utilidades JSON, ya que trabajaremos con un objeto JSON.
import json
# Importar el SDK de AWS (para Python, el nombre del paquete es boto3)
import boto3
# Importar time
import time
# Importar paquetes para ayudarnos con las fechas y el formato de las fechas.

# Crea un objeto DynamoDB utilizando el SDK de AWS
dynamodb = boto3.resource('dynamodb')
# Utiliza el objeto DynamoDB para seleccionar nuestra tabla
table = dynamodb.Table('HelloWorldDatabase')

# Definir la función del controlador que el servicio Lambda utilizará como punto de entrada
def lambda_handler(event, context):
    # Obtener la hora GMT actual
    gmt_time = time.gmtime()
    
    # Almacenar la hora actual en un formato legible para humanos en una variable.
    # Formatear el string de hora GMT
    now = time.strftime('%a, %d %b %Y %H:%M:%S +0000', gmt_time)
    
    # Extraer valores del objeto de evento que obtuvimos del servicio Lambda y almacenarlos en una variable
    name = event['firstname'] + ' ' + event['lastname']
    
    # Escribir el nombre y la hora en la tabla DynamoDB usando el objeto que instanciamos y guardar la respuesta en una variable
    response = table.put_item(
        Item={
            'ID': name,
            'LatestGreetingTime': now
        }
    )
    
    # Devolver un objeto JSON con el formato correcto
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda, ' + name)
    }