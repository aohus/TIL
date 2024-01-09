## sysbench를 이용한 mysql 성능테스트

프로젝트에서 복잡한 쿼리를 하기 시작해서 table별 index를 추가하려고합니다. index를 추가하는 것이 얼만큼 효과가 있는지 측정해보았습니다. 우선 실서버에 올리기 전에 로컬 서버(mac)에서 쿼리의 속도를 측정했습니다.

- 로컬 서버 환경은 mac 노트북입니다.
- 성능테스트는 sysbench를 이용합니다. 처음에 mysql 설치와 함께 제공되는 mysqlslab을 고려했으나, throuput, latency를 함께 보기 위해 좀 더 다양한 기능이 있는 sysbench를 이용하기로 했습니다.
- DB는 mysql innodb 입니다. mysql은 도커 컨테이너 위에 실행하였습니다. dev 서버를 ec2 free-tier 인스턴스를 이용할 예정이라 컨테이너 자원을 dev 서버 조건과 동일한 cpus 1, memory 2g로 제한하였습니다.

### 1. 설치
```bash
brew install sysbench
```

### 2. MySQL 데이터베이스 및 사용자 설정
- MySQL 서버가 설치되어 있고 실행 중인지 확인합니다.
- 쿼리를 요청할 테이블이 이미 존재하는지 확인합니다.
- `sysbench`는 MySQL 서버에 연결하기 위해 사용자 이름, 비밀번호, 호스트, 포트, 데이터베이스 이름을 알아야 합니다.
- 연결 정보는 `sysbench` 스크립트에 포함되어야 합니다.

### 3. 쿼리 실행 스크립트 생성
`sysbench`는 사용자 정의 쿼리를 실행하기 위해 Lua 스크립트를 사용합니다. 원하는 위치에 .lua file을 생성하고 다음과 같이 스크립트를 작성합니다.

```
-- query.lua
function event()
   con:query("SELECT COALESCE(SUM(amount), 0) AS amount FROM wallet WHERE user_id = %d AND transaction_type = 'DEPOSIT' AND deleted IS NULL")
end
```

### 4. 성능테스트 실행
```bash
sysbench /path/query.lua --mysql-host=[호스트] --mysql-port=[포트] --mysql-user=[사용자 이름] --mysql-password=[비밀번호] --mysql-db=[데이터베이스 이름] --time=60 --threads=4 --report-interval=10 run
```

이 명령은 스크립트 `query.lua`를 사용하여 60초 동안 쿼리를 실행하고, 10초 간격으로 보고서를 생성하며, 4개의 스레드를 사용합니다.



## References
https://www.percona.com/blog/creating-custom-sysbench-scripts/