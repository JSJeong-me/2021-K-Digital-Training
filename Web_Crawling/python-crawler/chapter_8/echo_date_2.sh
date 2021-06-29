function echo_date() {
   echo "command run at -> $(date +\"%Y-%m-%d\ %H:%M:%S\")";
}
(
while true
do
   echo_date >> ~/echo_date.log;
   sleep 300;
done
) &
disown
echo $! > ~/echo_date.pid
