// Description: Configuration file for the Skills Management System frontend application.

export const _IP = "localhost";
export const _PORT = "5000";
export const _URL_SERVICES_BE = 'http://'+_IP+':'+_PORT+'/api';
export const _URL_COLLABORATOR = _URL_SERVICES_BE + '/collaborator';
export const _URL_COLLABORATOR_SKILLS = _URL_SERVICES_BE + '/collaborator/skills';