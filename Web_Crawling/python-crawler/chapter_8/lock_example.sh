#!/bin/bash
function main_command() {
   echo '명령어를 실행 중입니다.';
   sleep 30;
}

# 프로세스 ID를 출력할 파일 이름
PIDFILE=/tmp/lock_example.pid

# 프로세스 ID를 출력할 파일이 존재할 때
if [ -f $PIDFILE ];then
   # 프로세스 ID를 변수 PID에 저장
   PID=$(cat $PIDFILE);

   # ps 명령어를 사용해서 변수 PID의 프로세스 ID를 가진 프로세스가 존재하는지 확인하기
   ps -p $PID > /dev/null 2>&1;

   # 위 명령어의 실행 결과가 0이라면 프로세스가 존재한다는 의미
   if [ $? -eq 0 ];then
      echo "이미 실행 중입니다. PID: $PID";
      exit 1;
   # 그렇지 않은 경우 프로세스 ID를 출력한 파일은 존재하지만, 프로세스가 존재하지 않는다는 의미
   else
      echo "$PIDFILE 는 존재하지만 프로세스가 실행 중이지 않습니다.";
      echo "상태를 확인해서 문자가 있다면 $PIDFILE 를 제거하고 다시 실행해주세요.";
      exit 1;
   fi
fi

# 프로세스 ID를 파일 이름 PIDFILE에 출력
echo $$ > $PIDFILE;
echo "명령어를 실행합니다. 프로세스 ID: $(cat $PIDFILE)";

# 다음 main_command를 실제로 실행하고 싶은 명령어로 변경해주세요.
main_command;
# 명령어 실행이 종료됐다면 프로세스 ID를 출력한 파일도 함께 제거합니다.
rm $PIDFILE;
