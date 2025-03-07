import { Injectable, Logger } from "@nestjs/common";
import * as fs from "fs";
import { Metadata } from "./metadata.dto";
import * as path from "path";

@Injectable()
export class MetadataService {

    async getRandomMetadatFromFileSystem(): Promise<Metadata> {
        const dirPath = path.join(__dirname, '../../metadata');
        const files = await fs.promises.readdir(dirPath);

        if (files.length === 0) {
            throw new Error("No metadata files found");
        }

        const randomFile = files[Math.floor(Math.random() * files.length)];
        const filePath = path.join(dirPath, randomFile);

        new Logger(`${MetadataService.name} - getMetadata`).debug(`Reading metadata from file: ${filePath}`);

        const fileContent = await fs.promises.readFile(filePath, 'utf-8');
        const metadata: Metadata = JSON.parse(fileContent);

        return metadata;
    }

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