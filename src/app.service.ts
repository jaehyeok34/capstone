import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return 'Hello World!';
  }

  getMetadata(): object {
    return {
      "imageName": "ubuntu:22.04",
      "containerName": "test-container"
    };
  }
}
