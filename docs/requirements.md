# Requerimientos Funcionales

## Gestión de Estilos de Ventana

- El programa debe manejar diferentes estilos de ventana: O, XO, OXXO, OXO y otros tipos de ventanas, autorizasas por Gerencia.
- Cada estilo implica un número diferente de "naves"  y su disposición.

## Cálculo de Costos

- El costo de una ventana depende del ancho, alto, estilo de ventana, tipo de acabado del aluminio, y tipo de vidrio.
- **Acabados de aluminio**: Pulido, Lacado Brillante, Lacado Mate, y Anodizado, cada uno con un precio específico por metro lineal.
- **Tipos de vidrio**: Transparente, Bronce, Azul, cada uno con un precio específico por cm², y el vidrio puede ser esmerilado por un costo adicional.

## Cálculo Detallado de Costos

- **Marco de la Nave**: Se calcula basado en el perímetro de cada nave. Se descuentan las esquinas que tienen medidas específicas y un costo por esquina.
- **Vidrio**: El vidrio es 1.5 cm más pequeño que las dimensiones de la nave de cada lado y se calcula por área en cm².
- **Esquinas**: Cada esquina tiene un costo fijo, y cada nave requiere 4 esquinas.
- **Chapas**: Cada nave tipo "X" requiere una chapa con un costo fijo.

## Control de Precios y Actualizaciones

- El programa debe permitir la actualización de precios de los materiales para construir una ventana.
- El programa debe mostrar los precios actuales al usuario.

## Cotización de Ventanas

- El programa debe permitir ingresar dimensiones de las ventanas, tipo de vidrio, tipo de acabado, y estilo de ventana.
- El programa debe calcular automáticamente el costo total de una o varias ventanas según los detalles proporcionados.

## Manejo de Descuentos

- Si la cantidad de ventanas es mayor a 100, se debe aplicar un descuento del 10% al costo total.
