import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { _URL_COLLABORATOR } from '../config/config';

@Injectable({
  providedIn: 'root'
})
export class CollaboratorsServiceService {

  constructor(private httpClient: HttpClient) { }

  // This method fetches the list of collaborators from the API
  // and returns a promise that resolves to the list of collaborators.
  getAllCollaborators(): Observable<any> {
    return this.httpClient.get(_URL_COLLABORATOR);
  }

}
