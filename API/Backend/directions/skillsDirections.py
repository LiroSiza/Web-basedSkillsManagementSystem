from flask import Blueprint, request, jsonify
import Backend.globalInfo.ResponseMessages as ResponseMessages
import Backend.functions.skillsFunctions as skillsFunctions

# Define the blueprint for skills-related routes
cskillsBP = Blueprint('cSkillsBP', __name__, url_prefix='/api/collaborator/skills')

@cskillsBP.get('/<collaboratorId>')
def getSkills(collaboratorId):
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
    try:
        requestData = request.get_json()
        if not requestData:
            return jsonify(ResponseMessages.err472)
        
        if '_id' not in requestData or'strSName' not in requestData or 'strSLevel' not in requestData or 'numSYOE' not in requestData:
            return jsonify(ResponseMessages.err203)

        print("Request Data for POST Skill:", requestData)
        return skillsFunctions.postSkill(requestData['_id'], requestData['strSName'], requestData['strSLevel'], requestData['numSYOE'])
    except Exception as e:
        print(f"Error processing POST skill request: {e}")
        return jsonify(ResponseMessages.err500)
    
@cskillsBP.put('/')
def putSkill():
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
    try:
        if not collaboratorId or not strSName:
            return jsonify(ResponseMessages.err203)

        return skillsFunctions.deleteSkill(collaboratorId, strSName)

    except Exception as e:
        print(f"Error processing DELETE skill request: {e}")
        return jsonify(ResponseMessages.err500)


