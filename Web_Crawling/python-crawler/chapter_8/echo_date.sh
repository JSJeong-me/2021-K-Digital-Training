echo_date() { 
    echo "command run at -> $(date +\"%Y-%m-%d\ %H:%M:%S\")";
    sleep 5; 
}
echo_date | tee -a ~/echo_date.log