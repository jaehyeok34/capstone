import { Body, Controller, Get, Logger, Post, UsePipes, ValidationPipe } from "@nestjs/common";
import { MetadataService } from "./metadata.service";
import { Metadata } from "./metadata.dto";

@Controller("metadata")
export class MetadataController {

    constructor(private readonly metadataService: MetadataService) {}

    @Get()
    getInfo(): string {
        new Logger(`${MetadataController.name} - getInfo`).debug("Getting metadata from the server");

        return this.metadataService.getInfo();
    }

    @Get("get-random")
    async getRandomMetadata(): Promise<Metadata> {
        new Logger(`${MetadataController.name} - getMetadata`).debug("Getting metadata from the server");

        return await this.metadataService.getRandomMetadatFromFileSystem();
    }

    @Post("upload")
    @UsePipes(new ValidationPipe())
    async uploadAndSaveToFile(@Body() metadata: Metadata): Promise<string> {
        new Logger(`${MetadataController.name} - uploadMetadata`).debug(metadata);
        await this.metadataService.saveMetadataToFile(metadata);
        
        return "metadata uploaded successfully";
    }
}