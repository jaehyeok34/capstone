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

    @Post("upload")
    @UsePipes(new ValidationPipe())
    async uploadMetadata(@Body() metadata: Metadata): Promise<string> {
        new Logger(`${MetadataController.name} - uploadMetadata`).debug(metadata);
        await this.metadataService.saveMetadataToFile(metadata);
        
        return "metadata uploaded successfully";
    }
}