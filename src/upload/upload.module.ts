import { Module } from "@nestjs/common";
import { UploadController } from "./upload.controller";
import { UploadLocalStorageService } from "./upload-local-storage.service";

@Module({
    imports: [],
    controllers: [UploadController],
    providers: [
        {
            provide: 'STORAGE_SERVICE',
            useClass: UploadLocalStorageService
        }
    ]
})
export class UploadModule {}