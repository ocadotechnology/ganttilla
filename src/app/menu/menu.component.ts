import {Component, OnInit} from '@angular/core';
import {StaticFileService} from '../services/static-file.service';

@Component({
    selector: 'app-menu',
    templateUrl: './menu.component.html',
    styleUrls: ['./menu.component.css']
})
export class MenuComponent implements OnInit {
    menu = [];

    constructor(
        private fileService: StaticFileService
    ) {}

    ngOnInit() {
        this.fileService.getFile('menu.json').subscribe(menu => {
            this.menu = menu;
        });
    }

}
