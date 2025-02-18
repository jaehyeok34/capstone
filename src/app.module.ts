import { Module } from '@nestjs/common';
import { FileUploadModule } from './file-upload';

@Module({
  imports: [FileUploadModule],
  controllers: [],
  providers: [],
})
export class AppModule {}
