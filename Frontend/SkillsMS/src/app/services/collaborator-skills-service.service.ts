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
}
