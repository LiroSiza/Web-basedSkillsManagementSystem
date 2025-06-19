import { Component, EventEmitter, Input, input, Output } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-modal-skills-component',
  templateUrl: './modal-skills-component.component.html',
  styleUrl: './modal-skills-component.component.scss'
})
export class ModalSkillsComponentComponent {

  @Input() data: any;
  @Input() existingSkills: string[] = [];
  @Output() onClose = new EventEmitter<void>();
  @Output() onSave = new EventEmitter<any>();
  showModal = true;
  title = 'Agregar Skill';
  originalData: any;
  // En un futuro se obtendrán de la base de datos
  nameOptions = [
    '.Net',
    'React Native',
    'PHP',
    'Angular',
    'Ionic',
    'Python',
    'SQL',
    'MongoDB',
    'Flutter',
    'Swift',
    'Otro'
  ];

  levelOptions = ['Básico', 'Intermedio', 'Avanzado'];

  option1 = '';
  option2 = '';
  quantity = 0;

  ngOnInit() {
    if (this.data) {
      // Editar
      this.option1 = this.data.strSName;
      this.option2 = this.data.strSLevel;
      this.quantity = this.data.numSYOE;
      this.originalData = {
        strSName: this.option1,
        strSLevel: this.option2,
        numSYOE: this.quantity
      };
    } else {
      // Agregar - valores por defecto
      this.option1 = '';
      this.option2 = '';
      this.quantity = 0;
    }
  }

  getFilteredSkillOptions(): string[] {
    return this.nameOptions.filter(
      skill => !this.existingSkills.includes(skill)
    );
  }

  save() {
    const skill = {
      strSName: this.option1,
      strSLevel: this.option2,
      numSYOE: this.quantity
    };
    this.onSave.emit(skill);
    this.closeModal();
  }

  hasChanges(): boolean {
    return (
      this.option1 !== this.originalData?.strSName ||
      this.option2 !== this.originalData?.strSLevel ||
      this.quantity !== this.originalData?.numSYOE
    );
  }

  closeModal() {
    this.onClose.emit();
  }
}
