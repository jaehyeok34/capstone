import { Controller, Inject, Post, UploadedFiles, UseInterceptors } from "@nestjs/common";
import { FilesInterceptor } from "@nestjs/platform-express";
import { IStorage } from "./storage.interface";

@Controller("upload")
export class UploadController {
    constructor(
        @Inject('STORAGE_SERVICE') private readonly storageService: IStorage
    ) {}

    /**
     * 파일 업로드 end-point(POST /upload)
     * FilesInterceptor를 사용하여 업로드된 파일을 처리
     * 
     * @param files 
     * @returns 
     */
    @Post()
    @UseInterceptors(FilesInterceptor("files"))
    async uploadFiles(@UploadedFiles() files: Array<Express.Multer.File>): Promise<object> {
        const filePaths = await this.storageService.save(files);

        return {
            message: "파일 업로드 성공",
            filePaths
        }
    }
}