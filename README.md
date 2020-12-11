# Dataproject 1 - Karimun Jawa

## Video Explicativo

[Video Youtube](https://www.youtube.com/watch?v=c4Fv_oO_Vm4)

## Instrucciones de uso

1. Entrar a [TypeForm](https://juanluishg.typeform.com/to/kSAaM7eb) y realizar el cuestionario.
2. Entrar en [Google DataStudio](https://datastudio.google.com/reporting/d382cf32-f13f-4782-8f74-b7816a95beca) , clickar sobre el actualizar y se visualizarán los datos.


## Proceso

1. Se generan las repuestas del Typeform (cuestionario) realizadas por el usuario y pasan a Zapier.
2. Zapier conecta el Typeform con la base de datos PostgreSQL, que se ejecuta en nuestra instancia de Google Cloud.
3. El código Python está corriendo continuamente en la instancia de Google Cloud y cada cinco segundos ejecuta el algoritmo de emparejamiento de clientes con ciudades.
4. Esta ciudad se guarda en una columna de la tabla clientes asociada al cliente que ha realizado el cuestionario.
5. Desde Google DataStudio se visualizan los datos tanto de las ciudades como de los clientes, para así conocer la ciudad indicada.



## Arquitectura

<img src="https://raw.githubusercontent.com/juanluishg/dataproject1/main/Arquitectura.png"/>

### Justificación 

- **TypeForm**: Se trata de un portal para crear formularios de una manera muy sencilla. Se ha elegido esta opción debido a su baja complejidad y mejor diseño frente a otras alternativas como podría ser Google Form.
- **Zapier**: Se trata de una herramienta que, para nuestro caso de uso, permite unir nuestra fuente de datos, typeform, con un almacén de datos, es decir, una base de datos. Se eligió esta herramienta debido a su facilidad a la hora su configuración. Pues ya está preparada para unir typeform con postgresSQL.
- **PostgresSQL**: Base de datos relacional donde vamos a almacenar tanto los datos de los clientes como de las ciudades. Decidimos escoger una base de datos SQL, ya que la estructura de los clientes será siempre la misma, ya que el formulario no varía, por lo que se podía definir un esquema de la tabla inicial, y en cuanto a la tabla de los datos de las ciudades es similar, ya que de todas las ciudades almacenamos las mismas variables con el mismo formato.
- **Talend**: Para la ingestión de datos de nuestras fuentes de datos de las ciudades hemos elegido talend, ya que nos permite conectar CSV's y API's a la base de datos SQL. La principal razón de la elección de Talend frente a NIFI, es la posibilidad de extraer los esquemas de las variables de los csv y de la base de datos, lo que facilita su conexión. Además Talend ofrece distintos complementos como son el FilterRow o ConvertType, para de nuestros CSV's de entrada poder extraer solo la información deseada y tener toda la información de cada variable en el mismo formato para así poder guardarla en la base de datos SQL.
- **Python**: Como procesador de los datos y lenguaje donde programar el algoritmo de elección de ciudades para los clientes se ha elegido Python ya que es el que mas ampliamente se ha visto en clase.
- **Google Data Studio**:  Para mostrar los datos finales hemos elegido data studio ya que de una forma sencilla y vistosa se pueden mostrar los datos que tenemos almacenados en PostgresSQL. Podemos poner algunos gráficos de lo datos de las ciudades que justifican la elección de esa ciudad por parte de nuestro algoritmo. Así como enseñar al usuario que ciudad es la mas adecuada para él.
- **Google Cloud**: Hemos elegido google cloud para tener ejecutando constantemente tanto la base de datos, como el gestor de bases de datos(PGAdmin) y el código python. Su elección es debido a que ha sido el que se ha visto en clase y con el cual nos sentíamos cómodos para trabajar.
- **Docker**: se han implementado tres docker, uno para la base de datos, otro para el gestor y otro para ejecutar el algoritmo. Se ha decidido así ya que era una forma de realizar el despliegue y la configuración de manera automática. Así además, este sistema se convierte en escalable, ya que ante un aumento de respuestas de los clientes, se pueden desplegar más contenedores de la parte que se necesite escalar en ese momento.

## Esquema de la Base de Datos

<img src="https://raw.githubusercontent.com/juanluishg/dataproject1/main/Esquema_Datos.png"/>

## Esquema del Github
- [**Data**](https://github.com/juanluishg/dataproject1/tree/main/Data): Carpeta que contiene los csv de los datos de las ciudades utilizados. Estructurados por ciudades
- [**Dockers**](https://github.com/juanluishg/dataproject1/tree/main/Dockers): Carpeta con los DockerFiles y los docker-compose para levantar en docker tanto la base de datos como el proceso python. Estructurados por servicio.
- [**Talend**](https://github.com/juanluishg/dataproject1/tree/main/Talend): Carpeta con los Jobs de Talend exportados. Estructurados por ciudades
- [**analisis.py**](https://github.com/juanluishg/dataproject1/blob/main/analisis.py): Fichero python del proceso python que hace todo el proceso de obtener una ciudad para un cliente

## Anexos

[Google Drive](https://drive.google.com/drive/folders/15XZbsJrT2wsCwGE83Unb_iOQQy_V-x1O?usp=sharing)

[Trello](https://trello.com/b/sGpuxclx/dataproject1)

[PGAdmin](http://34.78.89.69:5050)
  - pgadmin4@pgadmin.org
  - admin
