# FoodDeliverySystem
소프트웨어공학 개인 실습 과제 1

# 일상 속 소프트웨어 시스템: 음식 배달 앱

## 1. 시퀀스 다이어그램

### Mermaid 코드
sequenceDiagram
    actor User
    participant App as 앱 인터페이스
    participant Payment as 결제 게이트웨이
    participant Notification as 알림 서비스

    User->>App: 앱 실행
    App->>User: 메뉴 목록 표시
    User->>App: 음식 선택
    App->>User: 장바구니 확인 요청
    User->>App: 주문 진행
    App->>Payment: 결제 요청
    Payment->>User: 결제 정보 입력
    User->>Payment: 결제 완료
    Payment->>App: 결제 성공 알림
    App->>Notification: 주문 완료 데이터 전송
    Notification->>User: SMS/푸시 알림 전송

### 시퀀스 다이어그램 이미지  
![시퀀스 다이어그램](sequence_diagram.png)

## 2. 샘플코드

### Python 코드
class PaymentGateway:
    def process_payment(self, amount: float) -> bool:
        try:
            print(f"[결제] {amount}원 처리 중...")
            return True
        except Exception as e:
            print(f"[에러] 결제 실패: {e}")
            return False

class NotificationService:
    def send_order_confirmation(self, user_id: str):
        print(f"[알림] {user_id}님, 주문이 완료되었습니다!")

class FoodDeliveryApp:
    def __init__(self):
        self.payment = PaymentGateway()
        self.notification = NotificationService()

    def browse_menu(self):
        print("메뉴 목록 표시")

    def add_to_cart(self, item: str):
        print(f"장바구니 추가: {item}")

    def checkout(self, user_id: str, total: float):
        if self.payment.process_payment(total):
            self.notification.send_order_confirmation(user_id)
            return True
        else:
            print("[알림] 결제 실패로 주문이 취소되었습니다.")
            return False

\# 사용자 시나리오
if __name__ == "__main__":
    app = FoodDeliveryApp()
    app.browse_menu()
    app.add_to_cart("떡볶이 세트")
    app.checkout("hyojun20210843", 15000)

### 코드 구조
- `PaymentGateway`: 결제 처리
- `NotificationService`: 알림 전송
- `FoodDeliveryApp`: 주문 프로세스 관리

## 3. 모듈 평가

- **PaymentGateway 클래스**  
  결제 처리만 담당합니다. 결제와 관련된 기능이 이 클래스에만 모여 있습니다.

- **NotificationService 클래스**  
  주문이 완료되었을 때 사용자에게 알림을 보내는 역할만 담당합니다. 알림과 관련된 기능이 이 클래스에만 모여 있습니다.

- **FoodDeliveryApp 클래스**  
  메뉴 표시, 장바구니 추가, 결제 요청, 알림 전송 등 전체 주문 과정을 관리합니다.

### 응집도
- 각 모듈이 한 가지 역할에 집중하여, 관련된 기능이 한 곳에 잘 모여 있습니다.

### 결합도
- 각 모듈이 필요한 정보만 주고받으며, 서로 깊게 연결되어 있지 않습니다.  
  그래서 한 모듈을 수정해도 다른 모듈에는 영향을 거의 주지 않습니다.

### 결론
- 이러한 구조 덕분에 프로그램이 이해하기 쉽고,  
  유지보수나 확장이 필요할 때도 편리합니다.

---

## 4. 참고 파일 링크

- [시퀀스 다이어그램 코드 전체 보기](./sequence_diagram.md)
- [샘플 코드 전체 보기](./food_delivery_app.py)
- [모듈 평가 전체 보기](./module_evaluation.md)

---

> 잘못된 점이나 수정할 부분이 있으면 언제든 말씀해 주세요!
