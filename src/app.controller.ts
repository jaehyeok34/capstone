import { Controller, Get, Logger } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHome(): string {
    return this.appService.getHome();
  }

  @Get("/get-metadata")
  async getMetadata(): Promise<object> {
    const log = new Logger("getMetadata");
    log.debug("getMetadata() called");

    return this.appService.getMetadata();
  }
}
