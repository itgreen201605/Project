# 다음은 파이선에 대한 소감을 나타내는 프로그램입니다.
print("재미있는 파이선")

# 교수님이 과제를 추가 했습니다. 위의 코드에 선을 그리는 코드를 추가 해야 합니다.
def line():
    print("-"*80)
print("재미있는 파이선")
line()

# 교수님이 또 과제를 추가했습니다. 글자가 있는곳만 선을 그리랍니다.
def line(count):
    print("-" * count)
print("재미있는 파이선")
line(15)

# 교수님이 또 과제를 추가했습니다. 원하는 글자로 선을 그리랍니다.
def line(char,count):
    print(char * count)
print("재미있는 파이선")
line('~',15)

