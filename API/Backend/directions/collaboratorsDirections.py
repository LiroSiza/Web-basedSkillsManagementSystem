
 #################################################################
 #           Rutas para un futuro manejar colaboradores          #
 #################################################################

from flask import Blueprint, request, jsonify
import Backend.globalInfo.ResponseMessages as ResponseMessages
import Backend.functions.collaboratorsFunctions as collaboratorsFunctions

# Define the blueprint for colaborator-related routes
colaboratorBP = Blueprint('collabBP', __name__, url_prefix='/api/collaborator')

@colaboratorBP.get('/')
def getCollaborators():
    """
    Obtener todos los colaboradores
    ---
    tags:
      - Collaborators
    responses:
      200:
        description: Lista de colaboradores obtenida exitosamente
      472:
        description: No se encontraron colaboradores
      500:
        description: Error interno del servidor
    """
    try:
        collaboratorsInfo = collaboratorsFunctions.getAllCollaborators()
        #print("Collaborators Data:", collaboratorsInfo)

        if not collaboratorsInfo:
            return jsonify(ResponseMessages.err472)

        for collaborator in collaboratorsInfo:  # We now that collaboratorsInfo is a list
            if '_id' in collaborator:
                collaborator['_id'] = str(collaborator['_id'])

        return jsonify(ResponseMessages.succ200, collaboratorsInfo), 200

    except Exception as e:
        print(f"Error fetching collaborators: {e}")
        return jsonify(ResponseMessages.err500)
    
@colaboratorBP.get('/<collaboratorId>')
def getCollaboratorsById(collaboratorId):
    """
    Obtener un colaborador por su ID
    ---
    tags:
      - Collaborators
    parameters:
      - name: collaboratorId
        in: path
        type: string
        required: true
        description: ID del colaborador a obtener
    responses:
      200:
        description: Colaborador encontrado
      203:
        description: ID inválido o no proporcionado
      472:
        description: No se encontró colaborador
      500:
        description: Error interno del servidor
    """
    try:
        if not collaboratorId:
            return jsonify(ResponseMessages.err203)
        
        collaboratorInfo = collaboratorsFunctions.getCollaboratorById(collaboratorId)
        #print("Collaborator Data:", collaboratorInfo)

        if not collaboratorInfo:
            return jsonify(ResponseMessages.err472)
        if '_id' in collaboratorInfo:
            collaboratorInfo['_id'] = str(collaboratorInfo['_id'])

        return jsonify(ResponseMessages.succ200, collaboratorInfo), 200

    except Exception as e:
        print(f"Error fetching collaborators: {e}")
        return jsonify(ResponseMessages.err500)

@colaboratorBP.post('/')
def postCollaborator():
    """
    Crear un nuevo colaborador
    ---
    tags:
      - Collaborators
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              strName:
                type: string
                description: Nombre del colaborador
              strLastnames:
                type: string
                description: Apellidos del colaborador
              strRol:
                type: string
                description: Rol del colaborador
            required:
              - strName
              - strLastnames
              - strRol
    responses:
      200:
        description: Colaborador creado exitosamente
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
        
        if 'strName' not in requestData or 'strLastnames' not in requestData or 'strRol' not in requestData:
            return jsonify(ResponseMessages.err203)

        print("Request Data for POST Collaborator:", requestData)
        return collaboratorsFunctions.postCollaborator(requestData['strName'], requestData['strLastnames'], requestData['strRol'])
    except Exception as e:
        print(f"Error processing POST collaborator request: {e}")
        return jsonify(ResponseMessages.err500)
    
@colaboratorBP.put('/')
def putCollaborator():
    """
    Actualizar un colaborador existente
    ---
    tags:
      - Collaborators
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
              strName:
                type: string
                description: Nombre
              strLastnames:
                type: string
                description: Apellidos
              strRol:
                type: string
                description: Rol
            required:
              - _id
              - strName
              - strLastnames
              - strRol
    responses:
      200:
        description: Colaborador actualizado exitosamente
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
        
        if '_id' not in requestData or 'strName' not in requestData or 'strLastnames' not in requestData or 'strRol' not in requestData:
            return jsonify(ResponseMessages.err203)
        print("Request Data for PUT Collaborator:", requestData)
        return collaboratorsFunctions.putCollaborator(requestData['_id'], requestData['strName'], requestData['strLastnames'], requestData['strRol'])
    except Exception as e:
        print(f"Error processing PUT collaborator request: {e}")
        return jsonify(ResponseMessages.err500)
    
@colaboratorBP.delete('/<collaboratorId>')
def deleteCollaboratorById(collaboratorId):
    """
    Eliminar un colaborador por su ID
    ---
    tags:
      - Collaborators
    parameters:
      - name: collaboratorId
        in: path
        type: string
        required: true
        description: ID del colaborador a eliminar
    responses:
      200:
        description: Colaborador eliminado exitosamente
      203:
        description: ID inválido o no proporcionado
      472:
        description: No se encontró colaborador para eliminar
      500:
        description: Error interno del servidor
    """
    try:
        if not collaboratorId:
            return jsonify(ResponseMessages.err203)

        deleteResult = collaboratorsFunctions.deleteCollaboratorById(collaboratorId)
        print("Delete Result direction:", deleteResult)

        # Verifica si algo fue eliminado
        if deleteResult is None or deleteResult.deleted_count == 0:
            return jsonify(ResponseMessages.err472)

        result_data = {"deleted_count": deleteResult.deleted_count}
        return jsonify(ResponseMessages.succ200, result_data), 200

    except Exception as e:
        print(f"Error processing DELETE collaborator request for {collaboratorId}: {e}")
        return jsonify(ResponseMessages.err500), 500
