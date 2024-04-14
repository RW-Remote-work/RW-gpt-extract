#!/bin/sh
basedir=$2
basedir=${basedir:="/home/work/avatar-cms"}
port=$3
port=${port:="9209"}
spcrl="/home/work/supervisor/bin/supervisorctl"
grep_str=$4
grep_str=${grep_str:="avatar-cms"}

startup()
{
	$spcrl status|grep -E "${grep_str}"|${basedir}/bin/python ${basedir}/src/restart_supervisor.py &
        ${basedir}/bin/python app.py --port=$port
}

shutdown()
{
	pid=`netstat -nlp 2>/dev/null|grep ${port}|grep LISTEN|grep 0.0.0.0|awk '{print \$NF}'|awk -F"/" '{print \$1}'`
	kill -9 $pid
        sleep 5
        is_run_port=`(sleep 1;)|telnet 127.0.0.1 $port 2>/dev/null|grep Escape -c`
        if [  $is_run_port -eq 0 ];
        then
                echo "stop success!"
                exit 0
        else
                echo "stop fail!"
                exit 123
        fi
}

case "$1" in
        start)
                startup
                ;;
        stop)
                shutdown
                ;;
        restart)
                shutdown
                startup
                ;;

esac
exit
