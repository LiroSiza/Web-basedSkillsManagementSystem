import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-auth-component',
  templateUrl: './auth-component.component.html',
  styleUrl: './auth-component.component.scss'
})
export class AuthComponentComponent {

  constructor(private router: Router) { }

  loginForm = new FormGroup({
    email: new FormControl('', [Validators.required, Validators.email]),
    password: new FormControl('', [Validators.required, Validators.minLength(6)])
  });
  registerForm = new FormGroup({
    name: new FormControl('', [Validators.required, Validators.minLength(2)]),
    email: new FormControl('', [Validators.required, Validators.email]),
    password: new FormControl('', [Validators.required, Validators.minLength(6)])
  });

  onSubmit() {
    if (this.loginForm.valid) {
      //console.log('Formulario Login válido', this.loginForm.value);
      // call an authentication service
      const email = this.loginForm.value.email;
      Swal.fire({
        icon: 'success',
        title: '¡Bienvenido!',
        text: `Has iniciado sesión como ${email}`,
        confirmButtonColor: '#60C8CB'  // Usa tu color principal
      });
      this.registerForm.markAsUntouched(); 
      this.router.navigate(['/collaborators']); // Navigate to the collaborators list on successful login
    } else {
      //console.log('Formulario Login inválido'); // Mark all controls as touched to show validation errors
      this.loginForm.markAllAsTouched(); 
    }

    if (this.registerForm.valid) {
      //console.log('Formulario Register válido', this.registerForm.value);
      this.registerForm.reset();
      this.loginForm.markAsUntouched(); 
      Swal.fire({
        icon: 'warning',
        title: 'En desarrollo',
        confirmButtonColor: '#60C8CB'  // Usa tu color principal
      });
    } else {
      //console.log('Formulario Register inválido');
      this.registerForm.markAllAsTouched(); 
    }
  }
}
