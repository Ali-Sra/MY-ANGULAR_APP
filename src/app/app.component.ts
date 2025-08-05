import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';

import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { ContentComponent } from './content/content.component';
import { AboutComponent } from './about/about.component';
import { ContactComponent } from './contact/contact.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule,
    HttpClientModule,
    HeaderComponent,
    FooterComponent,
    SidebarComponent,
    ContentComponent,
    AboutComponent,
    ContactComponent
  ],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'my-angular-app';

  name = '';
  email = '';
  message = '';
  response = '';

  constructor(private http: HttpClient) {}

  sendMessage() {
    this.http.post<any>('http://localhost:5000/api/contact', {
      name: this.name,
      email: this.email,
      message: this.message
    }).subscribe({
      next: (res) => this.response = res.msg,
      error: () => this.response = 'خطا در ارتباط با سرور'
    });
  }
}
