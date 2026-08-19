# Publicar este proyecto en GitHub

1. Crear en GitHub un repositorio vacío, por ejemplo `nova-spot-micro-tesis`.
   No agregar README, `.gitignore` ni licencia desde la página web porque ya
   existen localmente.
2. Desde la raíz del proyecto ejecutar:

```bash
cd ~/Documentos/Cuadrupedo
git remote add origin https://github.com/TU_USUARIO/nova-spot-micro-tesis.git
git branch -M main
git push -u origin main
```

3. Compartir con el profesor el enlace del repositorio. Para cada semana,
   actualizar `Github/PROGRESO_SEMANAL.md`, revisar los cambios y ejecutar:

```bash
git add Github/PROGRESO_SEMANAL.md
git commit -m "docs: actualizar progreso semanal"
git push
```

No subir contraseñas, claves, bolsas rosbag2 grandes, `build/`, `install/`,
`log/` ni entornos virtuales.
