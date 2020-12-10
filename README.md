# Dataproject 1 - Karimun Jawa

## Instrucciones de uso

1. Entrar a https://juanluishg.typeform.com/to/kSAaM7eb y realizar el cuestionario
2. Entrar en X y visualizar los resultados



## Proceso

1. Se generan las repuestas del typeform y pasan a zapier
2. Zapier conecta el typeform con la base de datos PostgresSQL que se ejecuta en nuestra instancia de Google Cloud.
3. El código python está corriendo continuamente en la instancia de GC y cuando detecte una nueva inserción en la tabla "clientes", ejecuta el algoritmo de emparejamiento de ciudades, que genera como salida una ciudad.
4. Esta ciudad se guarda en una columna de la tabla clientes asociado al cliente que ha realiza el cuestionario.
5. Desde Tableau se visualizan los datos tanto de las ciudades como de los clientes, para así conocer la ciudad indicada.

