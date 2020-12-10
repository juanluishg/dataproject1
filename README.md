# Dataproject 1 - Karimun Jawa

## Instrucciones de uso

1. Entrar a https://juanluishg.typeform.com/to/kSAaM7eb y realizar el cuestionario.
2. Entrar en https://datastudio.google.com/reporting/d382cf32-f13f-4782-8f74-b7816a95beca , clickar sobre el actualizar y se visualizarán los datos.



## Proceso

1. Se generan las repuestas del typeform (cuestionario) realizadas por el usuario y pasan a Zapier.
2. Zapier conecta el typeform con la base de datos PostgreSQL, que se ejecuta en nuestra instancia de Google Cloud.
3. El código python está corriendo continuamente en la instancia de Google Cloud y cada cinco segundos ejecuta el algoritmo de emparejamiento de clientes con ciudades.
4. Esta ciudad se guarda en una columna de la tabla clientes asociada al cliente que ha realizado el cuestionario.
5. Desde Google DataStudio se visualizan los datos tanto de las ciudades como de los clientes, para así conocer la ciudad indicada.


<img src="https://raw.githubusercontent.com/juanluishg/dataproject1/main/Arquitectura.png"/>
