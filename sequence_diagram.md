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
