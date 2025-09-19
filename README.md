Conclusiones del Proyecto (Mitchel Carrillo Uicab)
La ejecución de este código me permitió pasar de la teoría a la práctica, usando algunas librerias de ciencias de datos de por medio para la materia.

De NumPy a Pandas
Mi elección de usar NumPy y Pandas fueron consideradas ya que a mi parecer eran optimas para cumplir el objetivo, el cual era generar datos aleatorios y adaptarlos a un DataFrame para poder manipularlos de una forma más estructurada e intuitiva.

NumPy fue la herramienta ideal para el primer paso. Es la biblioteca más eficiente para crear un gran volumen de datos numéricos crudos de manera casi instantánea. Actúa como el motor de alto rendimiento que genera la materia prima.

La Estructura Final (Pandas): El propósito final siempre fue tener los datos en un DataFrame. Al convertir el arreglo de NumPy a un DataFrame de Pandas, le añadí una capa de contexto fundamental: etiquetas para las filas (alumnos) y columnas (materias). Esto transformó una simple matriz de números en una tabla de datos comprensible y fácil de manejar.

La lección más importante fue validar que la combinación de estas dos bibliotecas es un estándar en el análisis de datos por una razón. Se aprovecha la velocidad de NumPy para la generación de datos y la claridad de Pandas (df.loc['Alumno_321']) para su manipulación, creando un proceso robusto y legible.

Una Reflexión sobre Recursividad: Fibonacci y "Divide y Vencerás"
Este proyecto también me hizo reflexionar sobre la eficiencia de los algoritmos, como el clásico ejemplo de la recursividad en la secuencia de Fibonacci.

¿Por Qué la Recursividad Falla con Fibonacci?
Una implementación recursiva simple para Fibonacci es terriblemente ineficiente. La razón es el trabajo redundante y superpuesto. Para calcular fib(5), el programa calcula fib(4) y fib(3). Pero para calcular fib(4), vuelve a calcular fib(3) y fib(2). El valor de fib(3) se calcula múltiples veces, y este problema crece exponencialmente. La máquina realiza las mismas operaciones una y otra vez sin necesidad, generando problemas y distintos fallos de ejecucion, arrojando errores como los que decian que a la computadora le resultaba imposible asignar 372 gigas de espacio para siquiera intentar el proceso

¿Cuándo SÍ Sirve la Recursividad?
La recursividad es una herramienta increíblemente poderosa para problemas que se pueden subdividir en grupos independientes y no superpuestos. Funciona bajo la estrategia de "divide y vencerás", sirviendo por ejemplo en:

Algoritmos de ordenamiento (como Merge Sort): Para ordenar una lista, la divides en dos mitades, llamas a la misma función para ordenar cada mitad por separado, y luego unes los resultados. Cada llamada recursiva opera sobre un subconjunto único de los datos.

En estos casos, la recursividad divide un problema grande en problemas más pequeños e idénticos que no se solapan, lo que la convierte en una solución elegante y eficiente. La clave es que las "ramas" de la recursión no necesitan recalcular lo que otras ramas ya hicieron.
