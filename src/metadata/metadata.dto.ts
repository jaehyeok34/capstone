import { IsArray, IsEnum, IsOptional, IsString } from "class-validator";

export class Metadata {

    @IsString()
    imageName: string;

    @IsString()
    containerName: string;

    @IsEnum(["command", "daemon", "api"])
    executionMode: "command" | "daemon" | "api";

    @IsArray()
    command: string[];

    @IsOptional()
    @IsArray()
    volumes?: {
        hostPath: string;
        containerPath: string;
    }[];

    @IsOptional()
    @IsArray()
    inputTypes: string[];

    @IsString()
    outputType: string;

    @IsString()
    description: string;
}