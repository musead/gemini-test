from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="자동 실행 테스트입니다!"
)
print(response.text)
