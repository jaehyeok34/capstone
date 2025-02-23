import { Module } from '@nestjs/common';
import { UploadModule } from './upload';
import { AppController } from './app.controller';
import { AppService } from './app.service';

@Module({
  imports: [UploadModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
