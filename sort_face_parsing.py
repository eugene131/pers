import re

f = open("/home/eugene131/personal/out.txt","r")

text = f.read().split('\n')
print(text)
f.close()
def extract_number(element):
    # 정규 표현식을 사용하여 텍스트에서 숫자 값을 추출합니다.
    numbers = re.findall(r'\d+', element)
    # 숫자 값을 정수로 변환하여 반환합니다.
    return int(numbers[0]) if numbers else 0


text = sorted(text, key=extract_number)
print(text)

f = open('/home/eugene131/personal/out.txt', "w")
for i in text:
  f.write(i+"\n")