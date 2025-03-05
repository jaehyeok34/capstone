import { Injectable } from '@nestjs/common';
import { resolve } from 'path';

@Injectable()
export class AppService {
  getHome(): string {
    return 'middle server 입니다.';
  }

  async getMetadata(): Promise<object> {
    return new Promise(resolve => {
      setTimeout(() => {
        resolve({
          name: 'middle server',
          version: '1.0.0',
          description: 'middle server 입니다.',
        });
      }, 5000);
    });
  }
}
