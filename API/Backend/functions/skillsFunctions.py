from flask import jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId # Import ObjectId for MongoDB document IDs
import Backend.globalInfo.Keys as Keys
import Backend.globalInfo.ResponseMessages as ResponseMessages

# Initialize MongoDB connection if not already done - No Auth
if Keys.dbconn == None:
    mongoConnection = MongoClient(Keys.strConnection)   # Client
    Keys.dbconn = mongoConnection[Keys.strDBConnection] # Database
    dbConnSMS = Keys.dbconn['collaborators']            # Collection
else:
    dbConnSMS = Keys.dbconn['collaborators']            # Collection


def getSkillsByCollaborator(colaboratorId):
    try:
        response = dbConnSMS.find_one({ "_id": ObjectId(colaboratorId) }, { "skills": 1, "_id": 0 })  # Fetch only the skills field
        print("Response from DB (GET SKILLS):", response)
        
        if response is None or "skills" not in response:
            return None  # Return None if no skills found

        return response["skills"]
    
    except Exception as e:
        print(f"Error fetching skills: {e}")
        return None
    

def getSkillByCollaborator(colaboratorId, strSName):
    try:
        response = dbConnSMS.find_one(
            { "_id": ObjectId(colaboratorId), "skills.strSName": strSName },
            { "skills.$": 1, "_id": 0 }  # Fetch only the specific skill matching strSName
        )

        print("Response from DB (GET SKILL):", response)

        if not response or "skills" not in response:
            return None  # Return None if no skill found

        return response["skills"][0]  # Return the first matching skill

    except Exception as e:
        print(f"Error fetching skill: {e}")
        return None


def postSkill(collaboratorID, strSName, strSLevel, numSYOE):  # Actually a PUT
    try:
        newSkill = {
            "strSName": strSName,
            "strSLevel": strSLevel,
            "numSYOE": numSYOE
        }
        print("New Skill Data:", newSkill)

        result = dbConnSMS.update_one(
            { "_id": ObjectId(collaboratorID) },
            { "$push": { "skills": newSkill } }
        )

        print("Update Result:", result.raw_result)

        if result.modified_count > 0:
            return jsonify(ResponseMessages.succ200), 200
        else:
            return jsonify(ResponseMessages.err472)

    except Exception as e:
        print(f"Error inserting skill: {e}")
        return jsonify(ResponseMessages.err500)

    
def putSkill(collaboratorId, strSName, strSLevel, numSYOE):
    try:
        print("Updating skill:", strSName)
        result = dbConnSMS.update_one(
            {"_id": ObjectId(collaboratorId),"skills.strSName": strSName},
            {
                "$set": {
                    "skills.$.strSLevel": strSLevel, # Update first matching skill's level
                    "skills.$.numSYOE": numSYOE      # Update first matching skill's years of experience
                }
            }
        )
        print("Update Result:", result.raw_result)
        if result.modified_count > 0:
            return jsonify(ResponseMessages.succ200), 200
        else:
            return jsonify(ResponseMessages.err472)
    except Exception as e:
        print(f"Error updating skill: {e}")
        return jsonify(ResponseMessages.err500)
    
    
def deleteSkill(collaboratorId, strSName):
    try:
        result = dbConnSMS.update_one(
            { "_id": ObjectId(collaboratorId) },
            { "$pull": { "skills": { "strSName": strSName } } }
        )

        print("Delete Skill Result:", result.raw_result)

        if result.modified_count > 0:
            return jsonify(ResponseMessages.succ200), 200
        else:
            return jsonify(ResponseMessages.err472)
    except Exception as e:
        print(f"Error deleting skill: {e}")
        return jsonify(ResponseMessages.err500)
