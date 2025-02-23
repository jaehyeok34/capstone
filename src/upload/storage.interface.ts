/**
 * IStorage - 파일 저장을 위한 기본 메서드 정의
 */
export interface IStorage {
  /**
   * 업로드된 파일을 저장하는 메서드.
   * @param files Array<Express.Multer.File>
   * @returns 저장된 파일 경로 혹은 저장 결과
   */
  save(files: Array<Express.Multer.File>): Promise<Array<String>>; 
}
