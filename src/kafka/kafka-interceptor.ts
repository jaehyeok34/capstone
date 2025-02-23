import { CallHandler, ExecutionContext, Injectable, Logger, NestInterceptor } from "@nestjs/common";
import { Observable, tap } from "rxjs";
import { KafkaService } from "./kafka.service";

@Injectable()
export class KafkaInterceptor implements NestInterceptor {
    private readonly logger = new Logger(KafkaInterceptor.name); // for
    
    constructor(private readonly kafkaService: KafkaService) {}

    intercept<T extends Array<string>>(context: ExecutionContext, next: CallHandler<T>): Observable<T> | Promise<Observable<T>> {
        this.logger.debug("KafkaInterceptor - intercept");
                
        return next.handle().pipe(
            tap(async(result) => { // result == controller의 반환 값
                await this.kafkaService.send(result);
            })
        );
    }
}

