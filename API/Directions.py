from Backend.app import app
from Backend.directions.collaboratorsDirections import colaboratorBP
from Backend.directions.skillsDirections import cskillsBP

# Register the blueprint for collaborator routes
app.register_blueprint(colaboratorBP)
app.register_blueprint(cskillsBP)

if __name__ == "__main__":
    app.run(debug=True)