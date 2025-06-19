import { Component } from '@angular/core';
import { CollaboratorSkillsServiceService } from '../../services/collaborator-skills-service.service';
import { ActivatedRoute, RouterLinkActive } from '@angular/router';
import Swal from 'sweetalert2';


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
        //console.log('Skills fetched successfully:', this.skills);
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
    const newSkill = {
      _id : this.collaboratorData.id,
      strSName : skill.strSName,
      strSLevel : skill.strSLevel,
      numSYOE : skill.numSYOE
    }
    if (this.selectedSkill) {
      // EDITAR
      //console.log('Editando skill:', skill);
      this.updateSkill(newSkill);
    } else {
      // NUEVO
      //console.log('Agregando skill:', skill);
      this.createSkill(newSkill);
    }
  }

  deleteCollaboratorSkill(skill: any) {
    Swal.fire({
      title: '¿Estás seguro?',
      text: `¿Deseas eliminar la skill "${skill.strSName}"?`,
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#F9A825',
      cancelButtonColor: '#60C8CB',
      confirmButtonText: 'Sí, eliminar',
      cancelButtonText: 'Cancelar'
    }).then((result) => {
      if (result.isConfirmed) {
        this.selectedSkill = skill;
        this.deleteSkill(this.collaboratorData.id, this.selectedSkill.strSName);
        this.selectedSkill = null;
      }
    });
  }


  createSkill(newSkillData: any) {
    //console.log(newSkillData);
    this.collaboratorSkillsService.createCollaboratorSkill(newSkillData).subscribe(
      (data) => {
        //console.log('New Skill - successfully:', data);
        this.fetchCollaborators();
        Swal.fire(
          'Agregada',
          'La skill ha sido agregada correctamente.',
          'success'
        );
      },
      (error) => {
        console.error('Error new skill:', error);
        Swal.fire({
          icon: 'error',
          title: 'Error',
          text: 'No se creó la skill correctamente.'
        });
      }
    );
  }

  updateSkill(newSkillData: any) {
    //console.log(newSkillData);
    this.collaboratorSkillsService.updateCollaboratorSkill(newSkillData).subscribe(
      (data) => {
        //console.log('Updated Skill - successfully:', data);
        this.fetchCollaborators();
        Swal.fire(
          'Actualizada',
          'La skill ha sido actualizada correctamente.',
          'success'
        );
      },
      (error) => {
        console.error('Error update skill:', error);
        Swal.fire({
          icon: 'error',
          title: 'Error',
          text: 'No se actualizó la skill correctamente.'
        });
      }
    );
  }

  deleteSkill(idCollaborator: string, skillName: string) {
    //console.log("Info delete: ", idCollaborator + skillName);
    this.collaboratorSkillsService.deleteCollaboratorSkill(idCollaborator, skillName).subscribe(
      (data) => {
        //console.log('Deleted Skill - successfully:', data);
        this.fetchCollaborators();
        Swal.fire(
          'Eliminada',
          'La skill ha sido eliminada correctamente.',
          'success'
        );
      },
      (error) => {
        console.error('Error delete skill:', error);
        Swal.fire({
          icon: 'error',
          title: 'Error',
          text: 'No se eliminó la skill correctamente.'
        });
      }
    );
  }
}
