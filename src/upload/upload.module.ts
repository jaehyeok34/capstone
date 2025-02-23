import { Module } from "@nestjs/common";
import { UploadController } from "./upload.controller";
import { UploadLocalStorageService } from "./upload-local-storage.service";
import { KafkaInterceptor, KafkaService } from "src/kafka";

@Module({
    imports: [],
    controllers: [UploadController],
    providers: [
        {
            provide: 'STORAGE_SERVICE',
            useClass: UploadLocalStorageService
        },
        KafkaInterceptor,
        KafkaService
    ]
})
export class UploadModule {}