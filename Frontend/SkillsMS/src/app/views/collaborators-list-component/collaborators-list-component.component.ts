import { Component } from '@angular/core';
import { CollaboratorsServiceService } from '../../services/collaborators-service.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-collaborators-list-component',
  templateUrl: './collaborators-list-component.component.html',
  styleUrl: './collaborators-list-component.component.scss'
})
export class CollaboratorsListComponentComponent {
  collaborators: any[] = [];

  constructor(private collaboratorsService: CollaboratorsServiceService, private router: Router) {}

  ngOnInit() {
    this.fetchCollaborators();
  }

  fetchCollaborators() {
    this.collaboratorsService.getAllCollaborators().subscribe(
      (data) => {
        this.collaborators = data[1];
        //console.log('Collaborators fetched successfully:', this.collaborators);
      },
      (error) => {
        console.error('Error fetching collaborators:', error);
      }
    );
  }

  showSkills(collaborator: any) {
    this.router.navigate(['/skills'], { queryParams: { id: collaborator._id, strName: collaborator.strName, strLastnames: collaborator.strLastnames, strRol: collaborator.strRol } });
    //console.log(`Ver skills de ${collaboratorId}`);
  }
}
