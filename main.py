# f = open("first.txt", "w", encoding="utf-8") #*파일 열기_파일명, 모드(W-쓰기모드), 변환규칙)
# #* python main.py로 실행해야 메모장에 내용 반영
# # encoding=utf-8을 추가해야 글자가 깨지지 않음(올바르게 변환 가능하도록 규칙 지정)
# # (UTF-8: 전 세계 모든 문자를 담은 국제 표준 사전)

# f.write("내용 쓰기")

# f.close()

#* -----------------------여기까지  w "내용 쓰기" 

f = open("first.txt", "a", encoding="utf-8") #a로 내용을 추가하겠다.
f.write("내용 추가\n")  #\n을 사용 - 한 줄 여백을 둔 뒤 내용 추가
f.close()

#* -----------------------여기까지  a "내용 추가" - ((중복 발생)) 
#>>파일 내용을 읽은 뒤 삭제할 부분만 빼서 남은 내용을 덮어쓰면 해결 된다고 함

f = open("first.txt", "r", encoding="utf-8")
look = f.read() #read를 통해 읽고, 변수에 저장한다.
print(look) #look라는 변수를 보겠다.
f.close()
