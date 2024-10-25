def show_menu():
    print("작업 관리 애플리케이션")
    print("1. 할 일 추가")
    print("2. 할 일 목록 보기")
    print("3. 할 일 완료")
    print("4. 할 일 삭제")
    print("5. 종료")
    print()

def main():
    while True:
        show_menu()
        choice = input("원하는 작업을 선택하세요 (1~5): ")

        if choice == '1':
            
        elif choice == '2':

        elif choice == '3':    

        elif choice == '4':    

        elif choice == '5':

        else:
            print("잘못된 입력입니다. 1번부터 5번까지 기능 중 하나를 선택해주세요")    


if __name__ == '__main__':
    main()