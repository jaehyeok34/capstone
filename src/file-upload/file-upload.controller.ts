import { Controller, Post, UploadedFiles, UseInterceptors } from "@nestjs/common";
import { FilesInterceptor } from "@nestjs/platform-express";
import { FileUploadService } from "./file-upload.service";

@Controller("file")
export class FileUploadController {
    constructor(private readonly fileUploadService: FileUploadService) {}

    @Post("upload")
    @UseInterceptors(FilesInterceptor("files"))
    uploadFile(@UploadedFiles() files: Array<Express.Multer.File>): object {
        return this.fileUploadService.saveLocal(files);
        // return this.fileUploadService.saveKafka(files);
    }
}