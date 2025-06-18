import { Component } from '@angular/core';
import { CollaboratorSkillsServiceService } from '../../services/collaborator-skills-service.service';
import { ActivatedRoute, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-collaborator-skills-list-component',
  templateUrl: './collaborator-skills-list-component.component.html',
  styleUrl: './collaborator-skills-list-component.component.scss'
})
export class CollaboratorSkillsListComponentComponent {
  
  collaboratorData: any; // Declare collaboratorId to store the ID from query parameters
  skills: any[] = []; // Initialize skills as an empty array

  constructor(
    private collaboratorSkillsService: CollaboratorSkillsServiceService,
    private route: ActivatedRoute // Import ActivatedRoute to access query parameters
  ) {}

  ngOnInit() {
    this.route.queryParams.subscribe(params => {
      const data = {
        id : params['id'],
        name : params['strName'],
        lastnames : params['strLastnames'],
        rol : params['strRol']
      }
      this.collaboratorData = data; // Assign the ID to collaboratorId
      //console.log(`Collaborator Id: ${id}`);
    });
    this.fetchCollaborators();
  }

  fetchCollaborators() {
    this.collaboratorSkillsService.getAllCollaboratorSkills(this.collaboratorData.id).subscribe(
      (data) => {
        this.skills = data[1];
        console.log('Skills fetched successfully:', this.skills);
      },
      (error) => {
        console.error('Error fetching skills:', error);
      }
    );
  }
}
