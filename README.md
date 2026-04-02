# Respuestas conceptuales:
## 1. 
Las contraseñas deben ser hasheadas por seguridad: en caso de haber alguna vulnerabilidad en el sistema si las contraseñas fueran almacenadas como texto plano quienes realicen el ataque pueden acceder fácilmente a las contraseñas. En cambio al hashearlas las contraseñas se convierten en strings que son únicos y a partir de los cuales no se puede revertir para conocer la contraseña.

## 2.
En nuestro caso SQLite es ideal porque no necesitamos servers, si no que se puede usar el almacenamiento local sin necesidad de configuración. SQLite se puede usar más que nada en proyectos chicos como es nuestro caso. 
