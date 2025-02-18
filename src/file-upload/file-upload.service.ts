import { Injectable, Logger } from "@nestjs/common";
import * as path from 'path';
import * as fs from 'fs';
import { Kafka } from 'kafkajs';

@Injectable()   
export class FileUploadService {
    saveLocal(files: Array<Express.Multer.File>): object {
        // 프로젝트 루트 디렉토리의 uploads 경로를 생성
        const uploadsDir = path.join(process.cwd(), 'uploads');

        // uploads 디렉토리가 존재하는지 확인 후, 없으면 생성
        if (!fs.existsSync(uploadsDir)) {
            fs.mkdirSync(uploadsDir);
        }

        // 파일을 하나씩 순회하며 저장
        files.forEach(file => {
            const filePath = path.join(uploadsDir, file.originalname);
            fs.writeFileSync(filePath, file.buffer);
        });

        const logger = new Logger(FileUploadService.name);
        logger.log(`File uploaded successfully(saveLocal) - ${files.length} files`);

        return {
            message: "File uploaded successfully(saveLocal)",
            fileCount: files.length
        }
    }

    saveKafka(files: Array<Express.Multer.File>): object {
        // Kafka 인스턴스를 생성하고, 클라이언트 ID와 브로커 주소 설정
        const kafka = new Kafka({
            clientId: 'file-upload-service',
            brokers: ['localhost:9092'],
        });

        // 프로듀서 생성
        const producer = kafka.producer();

        (async () => {
            // 프로듀서 연결
            await producer.connect();

            // 각 파일을 Kafka 메시지 형식으로 변환
            // 메시지의 key 없이 라운드로빈 방식으로 전송
            const messages = files.map(file => ({
                key: file.originalname,
                value: JSON.stringify({
                    filename: file.originalname,
                    content: file.buffer.toString('base64')
                })
            }));

            // 'upload_files' 토픽으로 메시지들을 전송합니다.
            await producer.send({
                topic: 'upload_files',
                messages
            });

            // 전송 완료 후 프로듀서 연결을 종료합니다.
            await producer.disconnect();
        })();

        const logger = new Logger(FileUploadService.name);
        logger.log(`File uploaded successfully(saveKafka) - ${files.length} files`);
        
        return {
            message: "File uploaded successfully(saveKafka)",
            fileCount: files.length
        }
    }
}