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

## 🚀 uso basico

```bash
python3 -m gendiff.scripts.cli tests/fixtures/archivo1.yml tests/fixtures/archivo2.yml
python3 -m gendiff.scripts.cli tests/fixtures/file1.json tests/fixtures/file2.json




🎬 Demo Asciinema
Ver https://asciinema.org/a/rGG1v0DitnjcafuVkDnzO8TSU

Herramienta en Python para comparación de ambos archivos (uno en YAML y otro en JSON) con el resultado en formato plain y stylish. .

🚀 Uso básico
Comparación de dos archivos YAML:
python3 -m gendiff.scripts.cli tests/fixtures/archivo1.yml tests/fixtures/archivo2.yml 
python3 -m gendiff.scripts.cli tests/fixtures/archivo1.yml tests/fixtures/archivo2.yml --format stylish o plain o json

Comparación de dos archivos JSON:
python3 -m gendiff.scripts.cli tests/fixtures/file1.json tests/fixtures/file2.json 
python3 -m gendiff.scripts.cli tests/fixtures/file1.json tests/fixtures/file2.json --format plain o stylish o json
🎨 Ejemplo de salida

Formato stylish (por defecto)
Código
{
  common: {
    + follow: false
      setting1: Value 1
    - setting2: 200
    - setting3: true
    + setting3: null
    + setting4: blah blah
    + setting5: {
          key5: value5
      }
      setting6: {
          doge: {
            - wow: 
            + wow: so much
          }
          - key: value
          + ops: vops
      }
  }
  group1: {
    - baz: bas
    + baz: bars
    - nest: {
          key: value
      }
    + nest: str
  }
  - group2: {
        abc: 12345
    }
  + group3: {
        fee: 100500
    }
}

Formato plain
Código
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]


formato json
{
    "host": {
        "status": "unchanged",
        "value": "hexlet.io"
    },
    "proxy": {
        "status": "removed",
        "value": "123.234.53.22"
    },
    "timeout": {
        "status": "changed",
        "old_value": 50,
        "new_value": 20
    },
    "verbose": {
        "status": "added",
        "value": true
    }
}