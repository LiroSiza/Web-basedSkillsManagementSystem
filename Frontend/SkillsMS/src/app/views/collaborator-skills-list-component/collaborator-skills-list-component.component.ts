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
  showModal = false;
  selectedSkill: any = null;
  existingSkillNames: any[] = [];

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

  openModal(skill?: any) {
    this.existingSkillNames = this.skills.map(s => s.strSName); // Skills existentes
    this.selectedSkill = skill || null;  // Modo editar | agregar
    this.showModal = true;
  }

  handleSave(skill: any) {
    if (this.selectedSkill) {
      // EDITAR
      console.log('Editando skill:', skill);
      // Aquí llamas al servicio para actualizar skill (con ID si aplica)
    } else {
      // NUEVO
      console.log('Agregando skill:', skill);
      // Aquí llamas al servicio para crear una nueva skill
      const newSkill = {
        _id : this.collaboratorData.id,
        strSName : skill.strSName,
        strSLevel : skill.strSLevel,
        numSYOE : skill.numSYOE
      }
      this.createSkill(newSkill);
    }
  }

  createSkill(newSkillData: any) {
    console.log(newSkillData);
    this.collaboratorSkillsService.createCollaboratorSkill(newSkillData).subscribe(
      (data) => {
        console.log('New Skill - successfully:', data);
        this.fetchCollaborators();
      },
      (error) => {
        console.error('Error new skill:', error);
      }
    );
  }
}
