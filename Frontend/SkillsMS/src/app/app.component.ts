import { Component } from '@angular/core';
import { NavigationEnd, Router } from '@angular/router';
import { filter } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'SkillsMS';
  
  // Variable booleana para controlar si se muestra o no el navbar.
  // Por defecto se muestra (true).
  showNavbar = true;

  constructor(private router: Router) {
    // Nos suscribimos a los eventos del router (como cambios de rutas)
    this.router.events
      .pipe(
        // Filtramos para solo procesar eventos del tipo NavigationEnd,
        // que indican que una navegación se ha completado exitosamente.
        filter(event => event instanceof NavigationEnd)
      )
      .subscribe(event => {
        // Forzamos el tipo del evento a NavigationEnd, ya que TypeScript no lo infiere automáticamente.
        const navEnd = event as NavigationEnd;

        // Evaluamos si la ruta resultante después de redireccionamientos comienza con "/auth"
        // Si comienza con "/auth", ocultamos el navbar (false); si no, lo mostramos (true).
        this.showNavbar = !navEnd.urlAfterRedirects.startsWith('/auth');
      });
  }


}
