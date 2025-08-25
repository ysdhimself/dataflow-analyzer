import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://127.0.0.1:5000';

  constructor(private http: HttpClient) {}

  train(data: number[][]): Observable<any> {
    return this.http.post(`${this.baseUrl}/train`, { series: data });
  }

  detect(point: number[]): Observable<any> {
    return this.http.post(`${this.baseUrl}/detect`, { point });
  }
}
