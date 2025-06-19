import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { _URL_COLLABORATOR_SKILLS } from '../config/config';

@Injectable({
  providedIn: 'root'
})
export class CollaboratorSkillsServiceService {

  constructor(private httpClient: HttpClient) { }

  getAllCollaboratorSkills(collaboratorId: string): Observable<any> {
    return this.httpClient.get(_URL_COLLABORATOR_SKILLS + `/${collaboratorId}`);
  }

  // Esta función realiza una solicitud POST para crear una nueva habilidad asociada a un colaborador
  createCollaboratorSkill(data: any): Observable<any> {
    return this.httpClient.post(_URL_COLLABORATOR_SKILLS + `/`, data, {
      
      // Se especifica el encabezado Content-Type como application/json
      // Esto indica que el cuerpo de la petición está en formato JSON
      // Aunque Angular lo añade automáticamente cuando el body es un objeto, aquí se incluye explícitamente por claridad y compatibilidad
      headers: { 'Content-Type': 'application/json' }

    });
  }

  updateCollaboratorSkill(data: any): Observable<any> {
    return this.httpClient.put(_URL_COLLABORATOR_SKILLS + `/`, data, {
      headers: { 'Content-Type': 'application/json' }
    });
  }

  deleteCollaboratorSkill(id: string, skillName: string): Observable<any> {
    return this.httpClient.delete(_URL_COLLABORATOR_SKILLS + `/${id}` + `/${skillName}`, {
      headers: { 'Content-Type': 'application/json' }
    });
  }
}
