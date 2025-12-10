### Hexlet tests and linter status:
[![Actions Status](https://github.com/dayanholguinmarin/python-project-174/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/dayanholguinmarin/python-project-174/actions)


[![Maintainability](https://qlty.sh/gh/dayanholguinmarin/projects/python-project-174/maintainability.svg)](https://qlty.sh/gh/dayanholguinmarin/projects/python-project-174)


[![Code Coverage](https://qlty.sh/gh/dayanholguinmarin/projects/python-project-174/coverage.svg)](https://qlty.sh/gh/dayanholguinmarin/projects/python-project-174)


[![Test Coverage](https://api.codeclimate.com/v1/badges/<qltcp_uASIkfIzAo9koPko>/test_coverage)](https://codeclimate.com/github/<Dayanholguinmarin>/<python-project-174>/test_coverage)

# Gendiff

Herramienta en Python para comparar archivos JSON y mostrar sus diferencias de manera clara y organizada.

---


## 🚀 Instalación

Clona el repositorio y entra en la carpeta del proyecto:

```bash
git clone https://github.com/tuusuario/python-project-174.git
cd python-project-174


## 🎬 Demo Asciinema

[Ver demostración en Asciinema]( https://asciinema.org/connect/a05baada-d74f-4f49-8f62-509619878e10)


📚 Documentación adicional
El resultado se muestra en orden alfabético por claves.

Los símbolos indican:

- valor eliminado o cambiado.

+ valor agregado.

Sin símbolo: valor sin cambios.


# Calculadora de diferencias (gendiff)

Herramienta en Python para comparar archivos de configuración en formato **JSON** y **YAML**.

---

## 🚀 Uso básico

```bash
python3 -m gendiff.scripts.cli tests/fixtures/archivo1.yml tests/fixtures/archivo2.yml
python3 -m gendiff.scripts.cli tests/fixtures/file1.json tests/fixtures/file2.json