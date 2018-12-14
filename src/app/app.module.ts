import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppComponent} from './app.component';
import {RouterModule, Routes} from '@angular/router';
import {ChartComponent} from './chart/chart.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {MenuComponent} from './menu/menu.component';
import {
    MatButtonModule,
    MatCardModule,
    MatFormFieldModule,
    MatIconModule,
    MatInputModule,
    MatProgressSpinnerModule,
    MatSnackBarModule,
    MatToolbarModule
} from '@angular/material';
import {HttpClientModule} from '@angular/common/http';
import {StorageServiceModule} from 'angular-webstorage-service';
import {FormsModule} from '@angular/forms';
import {Ng2GoogleChartsModule} from 'ng2-google-charts';


export const routes: Routes = [
    {path: '', redirectTo: 'chart/empire', pathMatch: 'full'},
    {path: 'chart/:teamName', component: ChartComponent}
];

@NgModule({
    declarations: [
        AppComponent,
        ChartComponent,
        MenuComponent
    ],
    imports: [
        BrowserModule,
        StorageServiceModule,
        HttpClientModule,
        BrowserAnimationsModule,
        RouterModule.forRoot(routes),
        MatToolbarModule,
        MatButtonModule,
        MatIconModule,
        MatCardModule,
        MatFormFieldModule,
        MatInputModule,
        FormsModule,
        MatSnackBarModule,
        Ng2GoogleChartsModule,
        MatProgressSpinnerModule
    ],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule {
}
