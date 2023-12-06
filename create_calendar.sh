#!/bin/bash

# 디렉토리 설정
DIRECTORY="."
EXCLUDE_DIRS=(".git" "img")

# 현재 연도와 월 설정
YEAR=$(date +"%Y")
MONTH=$(date +"%m")

# 해당 월의 마지막 날짜 가져오기
LAST_DAY=$(cal $MONTH $YEAR | awk 'NF {DAYS=$NF} END {print DAYS}')

# Markdown 파일 초기화
echo "## ${YEAR}.${MONTH} 달력" > calendar.md
echo "" >> calendar.md

# 달력 헤더 추가
echo "| 일 | 월 | 화 | 수 | 목 | 금 | 토 |" >> calendar.md
echo "|----|----|----|----|----|----|----|" >> calendar.md

# 달력의 첫 번째 주 시작 요일 계산
FIRST_DAY=$(date -j -f "%Y-%m-%d" "$YEAR-$MONTH-01" +"%u")
FIRST_DAY=$((FIRST_DAY-1))

# 달력 줄 초기화
WEEK="|"

# 첫 주 시작 전까지 공백 추가
for (( i=0; i<FIRST_DAY; i++ )); do
    WEEK+="    |"
done

# 각 날짜에 대한 파일 정보 수집
for DAY in $(seq -w 1 $LAST_DAY); do
    # 다음 날짜 계산
    NEXT_DAY=$(date -j -v+1d -f "%Y-%m-%d" "$YEAR-$MONTH-$DAY" +"%Y-%m-%d")

    # 해당 날짜의 파일 목록 생성
    # find 명령어에 제외할 디렉토리 조건 추가
    EXCLUDE_CONDITIONS=$(printf " -type d -name %s -prune -o " "${EXCLUDE_DIRS[@]}")
    FILES=$(find $DIRECTORY $EXCLUDE_CONDITIONS -type f -newermt "$YEAR-$MONTH-$DAY" ! -newermt "$NEXT_DAY" -print)

    # FILES=$(find $DIRECTORY -type d -name "$EXCLUDE_DIR" -prune -o -newermt "$YEAR-$MONTH-$DAY" ! -newermt "$NEXT_DAY" -type f)

    # 파일 목록을 Markdown 리스트로 변환
    FILE_LIST=""
    for FILE in $FILES; do
        FILE_LIST+="<br>[$(basename $FILE)]($FILE)"
    done

    # 달력에 날짜와 파일 목록 추가
    WEEK+="$DAY: $FILE_LIST |"

    # 주가 끝나면 달력에 추가하고 새 주 시작
    if [ $(date -j -f "%Y-%m-%d" "$YEAR-$MONTH-$DAY" +"%u") -eq 6 ]; then
        echo "$WEEK" >> calendar.md
        WEEK="|"
    fi
done

# 마지막 주 추가
echo "$WEEK" >> calendar.md

