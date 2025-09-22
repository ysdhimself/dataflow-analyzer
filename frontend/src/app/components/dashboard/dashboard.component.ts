import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <h2>Dashboard</h2>
    
    <div>
      <label>Training Data (JSON array of arrays):</label>
      <input [(ngModel)]="trainingInput" placeholder='[[1,2],[2,3]]'>
      <button (click)="trainModel()">Train Model</button>
      <p *ngIf="trainResult">{{ trainResult | json }}</p>
    </div>
    
    <hr>
    
    <div>
      <label>Point to Detect (JSON array):</label>
      <input [(ngModel)]="pointInput" placeholder='[2,3]'>
      <button (click)="detectPoint()">Detect Point</button>
      <p *ngIf="detectResult">{{ detectResult | json }}</p>
    </div>
  `,
  styles: []
})
export class DashboardComponent {
  trainingInput = '[[1,2],[2,3],[3,4],[10,20]]';
  pointInput = '[2,3]';
  trainResult: any;
  detectResult: any;

  constructor(private api: ApiService) {}

  trainModel() {
    try {
      const data = JSON.parse(this.trainingInput);
      this.api.train(data).subscribe(res => this.trainResult = res);
    } catch (err) {
      this.trainResult = { error: 'Invalid JSON format' };
    }
  }

  detectPoint() {
    try {
      const point = JSON.parse(this.pointInput);
      this.api.detect(point).subscribe(res => this.detectResult = res);
    } catch (err) {
      this.detectResult = { error: 'Invalid JSON format' };
    }
  }
}
