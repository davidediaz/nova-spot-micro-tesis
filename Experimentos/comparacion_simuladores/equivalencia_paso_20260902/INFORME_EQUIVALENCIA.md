# Comparación Gazebo–MuJoCo

Configuración común: marcha paso, 32 muestras, 0,18 s/muestra; 11 ciclos. Las medias dinámicas excluyen el ciclo 1 como transitorio.

| Simulador | Avance/ciclo (m) | Roll máx. (°) | Pitch máx. (°) | Altura (m) | Error RMS (rad) | Coincidencia contactos | Margen medio (m) | Margen mínimo (m) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Gazebo | 0.022025 | 1.281788 | 2.483606 | 0.224125 | 0.008412 | 36.183 % | 0.017957 | 0.005139 |
| MuJoCo | 0.001157 | 0.624950 | 1.738599 | 0.220887 | 0.014768 | 0.000 % | 0.074766 | 0.070721 |

Los resultados verifican equivalencia de interfaces y procedimiento, no identidad física. Las diferencias cuantitativas reflejan motores de contacto y parámetros provisionales distintos; el sistema se mantiene denominado **modelo digital configurable**.
