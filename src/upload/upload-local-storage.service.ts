import { Injectable, Logger } from "@nestjs/common";
import { IStorage } from "./storage.interface";
import * as fs from "fs";
import { promisify } from "util";
import * as path from "path";
import * as os from "os";

const writeFileAsync = promisify(fs.writeFile);

@Injectable()
export class UploadLocalStorageService implements IStorage {

    private logger = new Logger(UploadLocalStorageService.name); // for debug
    // private uploadPath = path.join(process.cwd(), 'uploads'); // 현재 프로젝트 기준
    private uploadPath = path.join(os.homedir(), "Documents", "uploads"); // macOS 기준 "문서" 기준

    constructor() {
        if (!fs.existsSync(this.uploadPath)) {
            // 저장 경로가 없다면, 생성(상위 디렉토리까지 생성)
            fs.mkdirSync(this.uploadPath, { recursive: true });

            this.logger.debug("저장 경로 생성함")
        }
    }

    async save(files: Array<Express.Multer.File>): Promise<Array<string>> {
        // 파일(들)을 저장
        const filePaths = await Promise.all(
            files.map(async file => {
                const filePath = path.join(this.uploadPath, `${Date.now()}-${file.originalname}`);
                await writeFileAsync(filePath, file.buffer);

                return filePath;
            })
        );

        this.logger.debug("file uploaded successfully(save)");
        this.logger.debug('file paths: ' + filePaths);

        return filePaths;
    }
}