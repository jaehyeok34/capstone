import { Module } from '@nestjs/common';
import { MetadataModule } from './metadata';

@Module({
  imports: [MetadataModule],
})
export class AppModule {}
