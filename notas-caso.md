# Madrinas Por La Vida — notas del caso

Instagram: https://www.instagram.com/madrinasporlavida/?hl=es
Web (caída): www.madrinasporlavida.com
Contacto: Uruguay, 099 927 132

## Diagnóstico

- El dominio **madrinasporlavida.com quedó sin registrar** (expiró y no se renovó).
  Confirmado con `nslookup` (Non-existent domain) y WHOIS ("this domain has not been
  registered yet"). Riesgo: cualquiera puede comprarlo y suplantar a la organización.
- El Instagram sigue activo y con buen contenido (1994 seguidores a la fecha).

## Contenido recuperado del Wayback Machine

13 capturas entre dic. 2021 y feb. 2025 (`web.archive.org`). La estética visual no se
recuperó bien (sitio con mucho JS que el archivo no reproduce fiel), pero sí el contenido:

- **Organización:** ONG católica fundada por **Marta Grego**, nacida a partir del
  "Llamado Guadalupano" en México. Ayuda a madres jóvenes en riesgo de aborto y
  vulnerabilidad social: apoyo, contención y asesoramiento a mujeres embarazadas.
- **Secciones del sitio:** Quiénes somos, Localidades, Impacto social, Noticias,
  Donaciones, Galería, Donar.
- **Localidades:** Malvín (Montevideo), Aeroparque (Canelones), Artigas, Colombia.
- Cita usada en portada: *"Antes de formarte en el vientre, te elegí..."* (Jeremías 1,5).

Snapshot más completo (texto): `https://web.archive.org/web/20250211004139/https://madrinasporlavida.com/`
Página de misión: `https://web.archive.org/web/20240813021223/https://madrinasporlavida.com/nuestramision`

**Hallazgo clave:** el sitio viejo era **Squarespace**. El `sitemap.xml` archivado
(`https://web.archive.org/web/20240812153835id_/https://madrinasporlavida.com/sitemap.xml`)
lista todas las páginas reales del sitio (noticias, localidades, testimonios, donar, etc.)
y sus imágenes en `images.squarespace-cdn.com/content/v1/5b58e6d7a2772c975945ec1a/...`.
**Esas imágenes siguen 100% en línea** aunque el dominio esté caído (confirmado con
fetch, status 200) — el CDN de Squarespace es independiente del dominio propio. Esto
significa que se puede recuperar el archivo fotográfico completo de la organización en
alta resolución, no solo lo que aparece en el Wayback Machine.

Páginas reales según el sitemap: `/`, `/nuestramision`, `/madrinas`, `/contacto`,
`/malvin`, `/testimonios`, `/patrocinadores`, `/dona`, `/aeroparque`, `/galeria`,
`/artigas`, `/colombia`, `/sauce` (localidad no mencionada en el home), `/noticias`,
`/noticias-1` (con varios artículos históricos 2019–2024).

## Mensaje enviado por WhatsApp (oferta de ayuda voluntaria)

> Hola! Les escribo porque soy desarrollador/diseñador web y estuve viendo el perfil de
> Instagram de Madrinas Por La Vida (@madrinasporlavida), que se ve muy activo y con
> hermoso contenido 💛
>
> Les comento algo importante: noté que la página web que tienen en la bio,
> www.madrinasporlavida.com, no está funcionando. Investigué un poco y el motivo es que
> el dominio (la dirección web) quedó sin registrar — probablemente venció y no se renovó
> a tiempo. Esto significa que ahora mismo cualquier persona podría comprarlo y usarlo,
> incluso para hacerse pasar por la organización, lo cual sería un riesgo para ustedes y
> para quienes quieran donar o contactarlos confiando en ese sitio.
>
> Quería ofrecerles ayuda: me gustaría colaborar de forma gratuita y voluntaria para
> volver a poner la página en funcionamiento, ordenarla mejor y dejarla más prolija y
> agradable visualmente, para que refleje todo el lindo trabajo que hacen y sea fácil de
> usar para quien las visite.
>
> Si les interesa, podemos coordinar una charla breve para entender qué necesitan mostrar
> en la web (información de contacto, cómo ayudar, donaciones, etc.) y me pongo manos a
> la obra. Sin compromiso ni costo, solo con ganas de aportar mi granito de arena a la
> causa 🙏
>
> Quedo atento/a a lo que me digan!

## Archivos en esta carpeta

- `Temas_para_la_llamada_Madrinas_Por_La_Vida.pdf` — guía de temas a tocar en la llamada,
  con identidad de marca de Renueva Smart.
- `generar_pdf.py` — script Python (reportlab) que genera el PDF de arriba. Reutilizable
  para otros casos, ajustando el contenido de `secciones`.
- `borrador-web/index.html` — borrador funcional de la nueva web (una sola página),
  con contenido real recuperado (misión, localidades, fotos originales vía CDN de
  Squarespace) e **identidad visual nueva y propia** (no la de Renueva Smart): terracota
  `#C1523A` + crema `#FBF6EC` + tinta `#2B2420`, tipografías Lora (títulos) y Work Sans
  (cuerpo), ambas de Google Fonts. Pensado para mostrar en la llamada o ajustar después.
  Las fotos están hotlinkeadas directo al CDN de Squarespace (siguen en línea); antes de
  publicar en serio conviene descargarlas y alojarlas en el hosting definitivo.

## Próximos pasos

- [ ] Llamada con la organización (usar el PDF de temas como guía).
- [ ] Definir quién gestionará la compra/renovación del dominio.
- [ ] Conseguir permiso por escrito antes de tocar dominio/hosting reales (formulario
      de autorización de Renueva Smart).
- [ ] Mostrarles `borrador-web/index.html` y ajustar según feedback (contenido,
      identidad visual, secciones que falten: testimonios completos, noticias, donar).
- [ ] Si dan el visto bueno, descargar las fotos del CDN de Squarespace y alojarlas en
      el hosting definitivo (no depender de `images.squarespace-cdn.com` a largo plazo).
