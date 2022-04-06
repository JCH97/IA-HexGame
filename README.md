- José Carlos Hernández Piñera
- Miguel Alejandro Asin Barthelemy

### Problema.

​	Se tiene un tablero hexagonal de NxN en el cual juegan dos jugadores poniendo una ficha blanca o negra en dependencia del jugador al que le toque, gana el jugador que primero logre hacer un camino que conecte los laterales (Blanco) o la parte superior con la inferior (Negro)



### Reglas.

> - Inicialmente el tablero está vacío.
> - A cada jugador se le asigna un color de fichas y dos laterales opuestos del tablero que tendrá que intentar conectar con sus fichas siguiendo las reglas del juego.
> - Los jugadores van colocando fichas por turnos sobre el tablero en casillas desocupadas.
> - Gana el primer jugador que consigue formar una línea de sus fichas que conecte sus dos laterales.
> - No son posibles los empates.
> - Como el primer jugador tiene ventaja, se jugarán 2 partidas una con cada color de fichas.



### Modelación

​	Para la modelación del problema se maneja una estructura arborea,  representando la raíz de la misma el estado de inicio de un juego y sus nodos estados validos del tablero mientras que las aristas son movimientos o jugadas legales, en los que se llega de un estado del juego (nodo padre) hacia otro estado del juego (nodo hijo) después de aplicar el movimiento. El árbol representa la información completa del juego ya que tiene el conjunto completo de todas las posiciones del tablero. En un árbol de juego, un juego o partido es un único camino comenzando desde la raíz (estado inicial) y termina un una nodo hoja. Las representaciones de un tablero en los nodos hojas son llamados *tablero terminal*. Cada nivel del árbol representa las opciones de jugada de un jugador para ese turno. 

​	Minimax es un algoritmo recursivo el cual se usa para elegir un movimiento óptimo para un jugador asumiendo que el oponente también jugara de manera óptima. Como su nombre sugiere, su meta es minimizar la pérdida máxima (minimizar el peor escenario).

​	Una búsqueda minimax es una búsqueda exhaustiva en profundidad del árbol que se menciona arriba que devuelve un valor *"score"*. Una búsqueda minimax tiene dos fases llamadas fase de maximización y fase de minimización, respectivamente. La fase de maximización ocurre en todas las posiciones del tablero donde el primer jugador tiene el turno y la fase de minimización ocurre en todas las posiciones del tablero donde el segundo jugador tiene el turno. La fase de maximización devuelve el mayor *score* asignado a los sucesores mientras que la fase de minimización devuelve el valor más pequeño asignado a los sucesores.

​	Al buscar el árbol completo se crea un jugador que nuca pierde pues conoce completa todos los resultados posibles. Para este problema en particular se implementó la poda _alpha-beta_, puesto que para este juego normalmente se usan tableros de 11x11 y por tanto no es una opción viable generar todos los posibles escenarios.

​	Esta poda aplicada reduce significativamente el tiempo de decisión de la jugada en comparación con el minimax clásico.



### Heurística

​ Una idea inicial para afrontar el problema de construir la heurística consiste en contar la cantidad de piezas de un mismo jugador que están conectadas; para ello se almacena en un `set` las casillas ocupadas por el jugador, luego para cada una, se buscan los vecinos que también sean ocupadas por el jugador.

​	Despues de obtener la cantidad de casillas conectadas pertenecientes a cada jugador, se define entonces la función heurística como la diferencia entre las casillas conectadas por ambos jugadores (como dicho valor puede tener un valor absoluto mayor que 1, se normaliza dividiendo enter el máximo de ambas cantidades).

​ Con dicha heurística se establece una función que permite valorar un estado dado del tablero en cada hoja del árbol de desición para posteriormente establecer un valor más exacto que el minimax para cada nodo de dicho árbol.

### Ejecución

Para correr el algoritmo, basta con ejecutar el archivo `tourney.py` con:
Windows:
```
py tourney.py
```
o
Linux:
```
python3 tourney.py
```
Se iniciará una simulación de un todo contra todos y una vez terminado se dará un ranking con el total de victorias para cada algoritmo utilizado en el jugador artificial
