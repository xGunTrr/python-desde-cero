# Informática desde cero

## ¿Qué es Git?
Gestor de versiones para que nuestras aplicaciones se mantengan correctamente administradas.

## ¿Qué es GitHub?

### ¿Cómo instalar Git?

- Windows
1. Entramos a la página oficial de git `https://git-scm.com/`
2. Le damos click en `Install for windows`

- Linux
1. Entramos a la terminal y escribimos (debian)
```
sudo apt install git -y
```

### Primeros pasos
#### Configuración inicial de git
Cada que instalemos git deberemos configurarlo para que sepa quienes somos con nuestro usuario e email
```
git config --global user.name "tuUsuario"
git config --global user.email "tuCorreo"
```

#### Cómo clonar un repositorio
Clonaremos un repositorio cada que necesitemos trabajar en un proyecto externo.
```
git clone <url_del_repositorio>
```

#### Cómo subir mis archivos al github
```
git push origin main
```

#### Cómo descargar los archivos desde github
```
git pull origin main
```

#### Git add y Git commit
Para revisar el estado de nuestro proyecto (archivos y directorios)
```
git status
```

Nos sirve para que nuestro archivo deje de ser un borrador y pase a ser parte del proyecto.
```
git add <nombre_archivo>
```

Nos sirve para crear una versión de nuestro código.
```
git commit -m <comentario>
```

Como revisar nuestro historial de código
```
git log
```