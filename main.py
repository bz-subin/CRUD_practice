# f = open("first.txt", "w", encoding="utf-8") #*파일 열기_파일명, 모드(W-쓰기모드), 변환규칙)
# #* python main.py로 실행해야 메모장에 내용 반영
# # encoding=utf-8을 추가해야 글자가 깨지지 않음(올바르게 변환 가능하도록 규칙 지정)
# # (UTF-8: 전 세계 모든 문자를 담은 국제 표준 사전)

# f.write("내용 쓰기")

# f.close()

# #* -----------------------여기까지  w "내용 쓰기" 

# f = open("first.txt", "a", encoding="utf-8") #a로 내용을 추가하겠다.
# f.write("내용 추가\n")  #\n을 사용 - 한 줄 여백을 둔 뒤 내용 추가
# f.close()

# #* -----------------------여기까지  a "내용 추가" - ((중복 발생)) 
#*>>파일 내용을 읽은 뒤 삭제할 부분만 빼서 남은 내용을 덮어쓰면 해결 된다고 함

# f = open("first.txt", "r", encoding="utf-8")
# look = f.read() #read를 통해 읽고, 변수에 저장한다.
# print(look) #look라는 변수를 보겠다.
# f.close()
# # #* -----------------------여기까지  r 입력 부분 읽기(look)


#<모드가 r이 아니면, print를 못 하나?>

# f = open("first.txt", "w", encoding="utf-8")
# look = f.read()
# print(look)
# f.close
# # 오류 : io.UnsupportedOperation: not readable
# # io : 입출력 / 입출력 중에 할 수 없는 일. 읽기가 안 되는 상태

# # #* -----------------------여기까지  w(x)
#삭제할 부분만 빼기

f = open("first.txt", "r", encoding="utf-8")
r_one_line = f.readlines() # 한 줄 씩 읽은걸(가져온걸) / r_one_line(한줄씩 읽는)에 넣겠다.

keep_line = []  #유지할 부분만 고르겠다.

# 여러줄을 검사해야하기 때문에 반복(for) 사용.

look = r_one_line.replace("내용추가","") #일정 부분만 걸러주는 함수(찾을거, 바꿀거)
print(look)
close()

# 오류 : AttributeError: 'list' object has no attribute 'replace'
# replace는 문자열 전용이기 때문에 list에서는 쓸 수 없다.

# for passed_line in r_one_line  # passed_line(전달 라인)에 r_one_line가 있다면 반복.
# # r_one_line를 한 줄 씩 passed_line에 옮기는데, 다 넘겨서 r_one_line가 비게 된다면 반복 중지
#     if passed_line != 내용추가
#     #만약에, passed_line에 "삭제할 부분"이 없다면 keep_line에 추가한다.
