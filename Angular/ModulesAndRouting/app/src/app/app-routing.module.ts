import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { GlobalLoaderComponent } from './core/global-loader/global-loader.component';
import { ListComponent } from './user/list/list.component';

const routes: Routes = [
  {
    path: '',
    pathMatch:'full',
    redirectTo: '/home'
  },
  {
    path: 'user-list',
    component: ListComponent
  },
  {
    path: 'home',
    component: GlobalLoaderComponent
  }
];

// @NgModule({
//   imports: [RouterModule.forRoot(routes)],
//   exports: [RouterModule]
// })

export const AppRoutingModule = RouterModule.forRoot(routes);
