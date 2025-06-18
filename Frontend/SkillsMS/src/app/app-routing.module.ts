import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthComponentComponent } from './auth/auth-component/auth-component.component';
import { CollaboratorsListComponentComponent } from './views/collaborators-list-component/collaborators-list-component.component';
import { CollaboratorSkillsListComponentComponent } from './views/collaborator-skills-list-component/collaborator-skills-list-component.component';

const routes: Routes = [
  { path: 'auth', component: AuthComponentComponent },
  { path: 'collaborators', component: CollaboratorsListComponentComponent },
  { path: 'skills', component: CollaboratorSkillsListComponentComponent },
  { path: '', redirectTo: 'auth', pathMatch: 'full' },  // Redirect to auth on empty path
  { path: '**', redirectTo: 'auth' }  // Redirect to auth for any unknown paths

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
