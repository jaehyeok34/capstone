from agent import Agent


if __name__ == "__main__":
    agent = Agent()

    result = agent.save_metadata({"name": "metadata1", "value": "value1"}) 
    if not result:
        print("메타데이터 저장 실패")