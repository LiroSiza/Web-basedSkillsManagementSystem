from flask import Blueprint, request, jsonify
import Backend.globalInfo.ResponseMessages as ResponseMessages
import Backend.functions.collaboratorsFunctions as collaboratorsFunctions

# Define the blueprint for colaborator-related routes
colaboratorBP = Blueprint('collabBP', __name__, url_prefix='/api/collaborator')

# Route to get all colaborators
@colaboratorBP.get('/')
def getCollaborators():
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
