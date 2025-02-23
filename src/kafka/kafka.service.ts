import { Injectable, Logger } from "@nestjs/common";
import { Kafka, Producer } from "kafkajs";

@Injectable()
export class KafkaService {
    private readonly logger = new Logger(KafkaService.name);
    private readonly producer: Producer;

    constructor() {
        const kafka = new Kafka({
            clientId: 'file-upload-service',
            brokers: ['localhost:9092']
        });

        this.producer = kafka.producer();
    }
    
    private async init() {
        await this.producer.connect();
        this.logger.debug("kafka producer connected");
    }

    async send(filePaths: Array<string>) {
        await this.init();
        await this.producer.send({
            topic: 'upload_files',
            messages: [
                { value: JSON.stringify(filePaths) }
            ]
        });
        
        this.logger.debug("sent data to kafka");
        await this.producer.disconnect();
        this.logger.debug("kafka producer disconnected");
    }
}