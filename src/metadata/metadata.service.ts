import { Injectable, Logger } from "@nestjs/common";
import * as fs from "fs";
import { Metadata } from "./metadata.dto";
import * as path from "path";

@Injectable()
export class MetadataService {

    getInfo(): string {
        return "Metadata Server";
    }


    async saveMetadataToFile(metadata: Metadata): Promise<void> {
        const dirPath = path.join(__dirname, '../../metadata');
        const filePath = path.join(dirPath, `${metadata.imageName}.json`);

        if (!fs.existsSync(dirPath)) {
            fs.mkdirSync(dirPath);
        }

        new Logger(`${MetadataService.name} - saveMetadataToFile`).debug(`Saving metadata to file: ${filePath}`);

        await fs.promises.writeFile(filePath, JSON.stringify(metadata));
    }
}