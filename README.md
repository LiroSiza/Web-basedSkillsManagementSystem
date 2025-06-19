# 📊 Skills Management System (SMS)

Sistema web para la **gestión de habilidades técnicas** de colaboradores dentro de una organización. Permite registrar, visualizar y actualizar habilidades por colaborador, facilitando el análisis del nivel técnico del personal.

---

## 🛠️ Tecnologías Utilizadas

### Frontend
- **Angular** 15+
- **TypeScript**
- **Angular Material** – Para los componentes de UI
- **SweetAlert2** – Alertas y confirmaciones
- **RxJS** – Manejo de peticiones reactivas

### Backend
- **Python** (3.11)
- **Flask** – Microframework RESTful
- **Flask-CORS** – Para habilitar CORS entre frontend y backend
- **MongoDB** – Base de datos NoSQL
- **PyMongo** – Conector entre Flask y MongoDB

---

## 🚀 Cómo Ejecutar el Proyecto

### 🔧 Requisitos

- Node.js 18+ y Angular CLI
- Python 3.10+
- MongoDB instalado o acceso a una instancia
- (Opcional) Postman para pruebas de la API

### 📂 Estructura General

```
Web-basedSkillsManagementSystem/
│
├── API/                    # Backend con Flask
│   ├── app.py
│   ├── routes/
│   └── controllers/
│
└── Frontend/               # Aplicación Angular
    ├── src/app/
    └── ...
```

---

### ▶️ Pasos

#### 1. Levantar el Backend

```bash
cd API
python -m venv venvSMS
venvSMS\Scripts\activate   # En Windows
# source venvSMS/bin/activate  # En Linux/macOS
pip install -r requirements.txt
python Directions.py
```

El backend estará disponible en: http://127.0.0.1:5000

#### 2. Levantar el Frontend

```bash
cd Frontend
npm install
ng serve
```

El frontend estará disponible en: http://localhost:4200

---

## 🧪 Endpoints Clave de la API

- `GET /api/collaborators/` – Listar todos los colaboradores
- `PUT /api/collaborator/skills/` – Agregar skill a un colaborador
- `DELETE /api/collaborator/skill/<id>/<skillName>` – Eliminar skill

---

## 🐛 Posibles Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| FormDataRoutingRedirect | Petición POST sin `/` final en la URL | Asegúrate de usar `/api/collaborator/skills/` con la barra al final |
| 500 Internal Server Error | Campos faltantes en el body | Verifica que el JSON contenga `_id`, `strSName`, `strSLevel`, `numSYOE` |
| Letras en `<input type="number">` | HTML permite caracteres como `e` | Usa `min`, `max`, y validación con `pattern` si lo deseas más restrictivo |

---

## 🤝 Contribuciones

¡Contribuciones son bienvenidas! Si deseas colaborar:

1. Haz un fork del repositorio
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`)
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`)
4. Haz push (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

---

## 📃 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo con fines educativos o profesionales.