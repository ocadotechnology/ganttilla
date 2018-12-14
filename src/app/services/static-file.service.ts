import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

export class Goal {
    title: string;
    category: string;
    start_date: string;
    end_date: string;
    description: string;
    link: string;
    swimlane: string;
}

@Injectable({
    providedIn: 'root'
})
export class StaticFileService {

    constructor(private http: HttpClient) {
    }

    getFile(filename: string): Observable<Goal[]> {
        return this.http.get<Goal[]>(`./assets/${filename}`);
    }
}
