import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { provideHttpClient } from '@angular/common/http';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule],
  template: `
    <h2>Dashboard</h2>
    <button (click)="trainModel()">Train Model</button>
    <p *ngIf="trainResult">{{ trainResult | json }}</p>
    <hr>
    <button (click)="detectPoint()">Detect Point</button>
    <p *ngIf="detectResult">{{ detectResult | json }}</p>
  `,
  styles: []
})
export class DashboardComponent {
  trainingData: number[][] = [[1,2],[2,3],[3,4],[10,20]];
  testPoint: number[] = [2,3];
  trainResult: any = null;
  detectResult: any = null;

  constructor(private api: ApiService) {}

  trainModel() {
    this.api.train(this.trainingData).subscribe(res => this.trainResult = res);
  }

  detectPoint() {
    this.api.detect(this.testPoint).subscribe(res => this.detectResult = res);
  }
}
