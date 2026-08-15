# Deploy a este roadmap a Vercel (sin Git, sin repo público)

Esta carpeta solo tiene un archivo: `index.html` (tu roadmap tal cual, con
el checklist, notas y simulador funcionando). Vercel detecta automáticamente
que es un sitio estático — no necesita configuración adicional.

## Requisitos

- Tener Node.js instalado (para tener el comando `npx`)
- Una cuenta gratuita en vercel.com — puedes crearla con solo tu email, no
  necesitas conectar GitHub para nada.

## Desplegar (primera vez)

Abre una terminal, entra a esta carpeta, y corre:

```
cd vercel-deploy
npx vercel
```

Te va a preguntar un par de cosas (login, nombre del proyecto) — acepta
las opciones por defecto apretando Enter en cada una si no estás seguro.
Al final te da un link tipo:

```
https://data-engineering-roadmap.vercel.app
```

Ese es el link que compartes en Reddit, con compañeros, donde sea.

## Actualizar cuando cambies algo

Si más adelante modificas el `index.html` (agregas un tema, corriges algo),
solo corre de nuevo:

```
npx vercel --prod
```

Mismo link de siempre, contenido actualizado.

## Nota sobre el progreso de cada persona

Como esta es la versión web (no la app de escritorio), cada persona que
abra el link guarda su propio progreso en su propio navegador — nadie ve
el progreso de nadie más, y tú tampoco ves el de ellos. Si alguna vez
quieres una versión con autoguardado real en disco, esa es la app de
escritorio (Electron) que armamos por separado — pero para "llegar y usar"
compartiendo un link, esta versión web es la correcta.
