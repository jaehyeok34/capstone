import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHome(): string {
    return "Kafka Server RESTful API";
  }
}
