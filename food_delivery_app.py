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

# 사용자 시나리오
if __name__ == "__main__":
    app = FoodDeliveryApp()
    app.browse_menu()
    app.add_to_cart("떡볶이 세트")
    app.checkout("hyojun20210843", 15000)
