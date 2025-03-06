import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHome(): string {
    return 'middle server 입니다.';
  }

  async getMetadata(): Promise<object> {
    const response = await fetch("http://localhost:3001/get-metadata");
    return await response.json();
  }
}