import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHome(): string {
    return 'middle server 입니다.';
  }

  getMetadata(): object {
    return {
      title: 'middle server', 
      description: 'middle server 입니다.',
      version: '1.0.0',
    };
  }
}
