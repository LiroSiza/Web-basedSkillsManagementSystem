
 #################################################################
 #   Manejo de rutas para las habilidades de los colaboradores   #
 #################################################################

from flask import Blueprint, request, jsonify
import Backend.globalInfo.ResponseMessages as ResponseMessages
import Backend.functions.skillsFunctions as skillsFunctions

# Define the blueprint for skills-related routes
cskillsBP = Blueprint('cSkillsBP', __name__, url_prefix='/api/collaborator/skills')

@cskillsBP.get('/<collaboratorId>')
def getSkills(collaboratorId):
    """
    Obtener todas las habilidades de un colaborador
    ---
    tags:
      - Skills
    parameters:
      - name: collaboratorId
        in: path
        type: string
        required: true
        description: ID del colaborador para obtener sus habilidades
    responses:
      200:
        description: Habilidades obtenidas exitosamente
      203:
        description: Parámetro inválido o no proporcionado
      472:
        description: No se encontraron habilidades
      500:
        description: Error interno del servidor
    """
    try:
        if not collaboratorId:
            return jsonify(ResponseMessages.err203)

        skills = skillsFunctions.getSkillsByCollaborator(collaboratorId)
        
        if skills is None:
            return jsonify(ResponseMessages.err472)

        return jsonify(ResponseMessages.succ200, skills), 200

    except Exception as e:
        print(f"Error fetching collaborator skills: {e}")
        return jsonify(ResponseMessages.err500)
    

@cskillsBP.get('/<collaboratorId>/<strSName>')
def getSkill(collaboratorId, strSName):
    """
    Obtener una habilidad específica de un colaborador
    ---
    tags:
      - Skills
    parameters:
      - name: collaboratorId
        in: path
        type: string
        required: true
        description: ID del colaborador
      - name: strSName
        in: path
        type: string
        required: true
        description: Nombre de la habilidad
    responses:
      200:
        description: Habilidad obtenida exitosamente
      203:
        description: Parámetros inválidos o no proporcionados
      472:
        description: No se encontró la habilidad
      500:
        description: Error interno del servidor
    """
    try:
        if not collaboratorId or not strSName:
            return jsonify(ResponseMessages.err203)

        skill = skillsFunctions.getSkillByCollaborator(collaboratorId, strSName)
        
        if skill is None:
            return jsonify(ResponseMessages.err472)

        return jsonify(ResponseMessages.succ200, skill), 200

    except Exception as e:
        print(f"Error fetching collaborator skills: {e}")
        return jsonify(ResponseMessages.err500)


@cskillsBP.post('/')
def postSkill():
    """
    Crear una nueva habilidad para un colaborador
    ---
    tags:
      - Skills
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              _id:
                type: string
                description: ID del colaborador
              strSName:
                type: string
                description: Nombre de la habilidad
              strSLevel:
                type: string
                description: Nivel de la habilidad
              numSYOE:
                type: integer
                description: Años de experiencia
            required:
              - _id
              - strSName
              - strSLevel
              - numSYOE
    responses:
      200:
        description: Habilidad creada exitosamente
      203:
        description: Parámetros incompletos
      472:
        description: Datos inválidos
      500:
        description: Error interno del servidor
    """
    try:
        requestData = request.get_json()
        if not requestData:
            return jsonify(ResponseMessages.err472)
        
        if '_id' not in requestData or 'strSName' not in requestData or 'strSLevel' not in requestData or 'numSYOE' not in requestData:
            return jsonify(ResponseMessages.err203)

        print("Request Data for POST Skill:", requestData)
        return skillsFunctions.postSkill(requestData['_id'], requestData['strSName'], requestData['strSLevel'], requestData['numSYOE'])
    except Exception as e:
        print(f"Error processing POST skill request: {e}")
        return jsonify(ResponseMessages.err500)
    
@cskillsBP.put('/')
def putSkill():
    """
    Actualizar una habilidad existente de un colaborador
    ---
    tags:
      - Skills
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              _id:
                type: string
                description: ID del colaborador
              strSName:
                type: string
                description: Nombre de la habilidad
              strSLevel:
                type: string
                description: Nivel de la habilidad
              numSYOE:
                type: integer
                description: Años de experiencia
            required:
              - _id
              - strSName
              - strSLevel
              - numSYOE
    responses:
      200:
        description: Habilidad actualizada exitosamente
      203:
        description: Parámetros incompletos
      472:
        description: Datos inválidos
      500:
        description: Error interno del servidor
    """
    try:
        requestData = request.get_json()
        if not requestData:
            return jsonify(ResponseMessages.err472)
        
        if '_id' not in requestData or 'strSName' not in requestData or 'strSLevel' not in requestData or 'numSYOE' not in requestData:
            return jsonify(ResponseMessages.err203)
        print("Request Data for PUT Skill:", requestData)
        return skillsFunctions.putSkill(requestData['_id'], requestData['strSName'], requestData['strSLevel'], requestData['numSYOE'])
    except Exception as e:
        print(f"Error processing PUT skill request: {e}")
        return jsonify(ResponseMessages.err500)
    
    
@cskillsBP.delete('/<collaboratorId>/<strSName>')
def deleteSkill(collaboratorId, strSName):
    """
    Eliminar una habilidad de un colaborador
    ---
    tags:
      - Skills
    parameters:
      - name: collaboratorId
        in: path
        type: string
        required: true
        description: ID del colaborador
      - name: strSName
        in: path
        type: string
        required: true
        description: Nombre de la habilidad a eliminar
    responses:
      200:
        description: Habilidad eliminada exitosamente
      203:
        description: Parámetros inválidos o no proporcionados
      500:
        description: Error interno del servidor
    """
    try:
        if not collaboratorId or not strSName:
            return jsonify(ResponseMessages.err203)

        return skillsFunctions.deleteSkill(collaboratorId, strSName)

    except Exception as e:
        print(f"Error processing DELETE skill request: {e}")
        return jsonify(ResponseMessages.err500)
