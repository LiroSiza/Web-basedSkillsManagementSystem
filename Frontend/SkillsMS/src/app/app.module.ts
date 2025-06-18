import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponentComponent } from './core/navbar-component/navbar-component.component';
import { ModalSkillsComponentComponent } from './shared/modal-skills-component/modal-skills-component.component';
import { AuthComponentComponent } from './auth/auth-component/auth-component.component';
import { CollaboratorsListComponentComponent } from './views/collaborators-list-component/collaborators-list-component.component';
import { CollaboratorSkillsListComponentComponent } from './views/collaborator-skills-list-component/collaborator-skills-list-component.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { MatTabsModule } from '@angular/material/tabs';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';;
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';


@NgModule({
  declarations: [
    AppComponent,
    NavbarComponentComponent,
    ModalSkillsComponentComponent,
    AuthComponentComponent,
    CollaboratorsListComponentComponent,
    CollaboratorSkillsListComponentComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatCardModule,
    MatTabsModule,
    ReactiveFormsModule,
    HttpClientModule,
    MatIconModule
  ],
  providers: [
    provideAnimationsAsync()
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
