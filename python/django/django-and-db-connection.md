# django 에서 db connection 관리
Django와 MySQL을 함께 사용할 때, 기본적으로 Django는 내장된 Connection Pooling 메커니즘을 제공하지 않는다. Django의 ORM은 각 요청에 대해 데이터베이스 연결을 열고 요청이 완료되면 연결을 닫는다. Django가 "long-lived" 연결을 유지하지 않고, 연결을 필요할 때마다 생성하고 해제하는 방식을 사용한다는 것을 의미한다. 그렇다고 연결 오버헤드를 방치하는 것은 아니고 Persistent Connection 방식을 적용하여 DB 쿼리를 처음 만들 때 DB 커넥션을 열고 이 연결을 열린 상태로 유지하고 후속 요청에서 이 연결을 재사용할 수 있다.

## 연결 오버헤드를 해결하는 방법

#### 1. **Django-DB-Connection-Pool**
Django에서 Connection Pooling을 사용할수도 있다. Django 내장 기능이 아닐 뿐, 외부 라이브러리를 활용하면 된다. `django-db-connection-pool`은 Django 애플리케이션에 대해 Connection Pooling을 제공하는 라이브러리이다. 이 라이브러리는 `SQLAlchemy`의 연결 풀 기능을 사용하여 작동한다.

설정 및 구현 고려사항
- Connection Pooling을 사용할 때, 최대 연결 수, 연결 유효 시간, 대기 시간 등과 같은 풀 관련 설정에 주의를 기울여야 합니다.
- Connection Pooling은 애플리케이션과 데이터베이스 서버 간의 네트워크 오버헤드를 줄이고, 연결 생성 및 해제에 대한 비용을 줄일 수 있습니다.
- 데이터베이스 서버의 `max_connections` 설정과 Connection Pool의 크기를 적절히 조절하여 서버 과부하를 피해야 합니다.
    
#### 2. **persistent-db-connections**
Django의 `persistent-db-connections` 설정을 활성화하여 Django의 기본 데이터베이스 연결을 재사용할 수도 있다. 이는 Django 1.6부터 도입된 기능이다. 전통적인 Connection Pooling과는 다르며, 단지 요청 간에 데이터베이스 연결을 유지하는 방식이다.



https://seungho-jeong.github.io/technology/computer-science/django-db-connections/

