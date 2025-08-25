import { Component } from '@angular/core';
import { DashboardComponent } from './components/dashboard/dashboard.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [DashboardComponent],
  template: `
    <h1>DataFlow Analyzer</h1>
    <hr>
    <app-dashboard></app-dashboard>
  `,
  styles: []
})
export class AppComponent {
  title = 'DataFlow Analyzer';
}
