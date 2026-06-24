from rag_agent import rag_query

question = input("Question: ")

answer = rag_query(question)

print("\nAnswer:")
print(answer)