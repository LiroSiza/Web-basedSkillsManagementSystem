import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar-component',
  templateUrl: './navbar-component.component.html',
  styleUrl: './navbar-component.component.scss'
})
export class NavbarComponentComponent {

  constructor(private router: Router){}

  logout(){
    this.router.navigate(['/auth']);
  }
}
