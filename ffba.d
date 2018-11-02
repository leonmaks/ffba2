#! /bin/sh
### BEGIN INIT INFO
# Provides:          ffba
# Required-Start:    $local_fs $remote_fs $network $syslog $named
# Required-Stop:     $local_fs $remote_fs $network $syslog $named
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# X-Interactive:     true
# Short-Description: Start/stop FFBA Test web server
### END INIT INFO

# Author: Le Ma

script_name=`basename $0`
NAME=${script_name%.*}

USER=ffba
GROUP=ffba
PID_FILE="/run/$NAME.pid"

USER_HOME=/home/ffba
WORK_DIR=$USER_HOME/wsp/ffba2
LOG_DIR=$USER_HOME/wsp/log
LOGFILE="$LOG_DIR/$NAME.log"
ERRFILE="$LOG_DIR/$NAME-err.log"

PYTHON=$USER_HOME/prod/bin/python
GUNICORN=$USER_HOME/prod/bin/gunicorn

IP=127.0.0.1
PORT=8800
WORKERS=5
#WORKERS=25 #12 CPU server

CHDIR_CMD="cd $WORK_DIR"
GUNICORN_RUN_CMD="$PYTHON $GUNICORN --user=$USER --group=$GROUP --daemon --workers=$WORKERS --bind=unix:/tmp/$NAME.sock --pid=$PID_FILE --name=$NAME --error-logfile $ERRFILE --log-file=$LOGFILE --log-level=debug wsgi"

. $CONFIG_DIR/$CONFIG_FILE

# Load the VERBOSE setting and other rcS variables
. /lib/init/vars.sh

# Define LSB log_* functions.
# Depend on lsb-base (>= 3.2-14) to ensure that this file is present
# and status_of_proc is working.
. /lib/lsb/init-functions

#
# Start the daemon/service
#
do_start() {
	# Return
	#   0 if daemon has been started
	#   1 if daemon was already running
	#   2 if daemon could not be started
	if [ -e $PID_FILE ]; then
		echo "$NAME is already running; ingoring start command"
		return 1
	fi
	#echo "cd $WORK_DIR"
	cd $WORK_DIR
	echo "$GUNICORN_RUN_CMD"
	#nohup sudo -u $USER -s /bin/bash -c "$GUNICORN_RUN_CMD" &
	$GUNICORN_RUN_CMD
	if [ $? = 0 ]; then
			echo "$NAME started"
		return 0
	else
			echo "$NAME could not be started"
		return 2
	fi
}

#
# Function that stops the daemon/service
#
do_stop() {
	# Return
	#   0 if daemon has been stopped
	#   1 if daemon was already stopped
	#   2 if daemon could not be stopped
	#   other if a failure occurred
	if [ -f $PID_FILE ]; then
		#echo "`cat $PID_FILE`"
		PID=`cat $PID_FILE`
		#echo "rm $PID_FILE"
		rm $PID_FILE
		#echo "kill -15 $PID"
		kill -15 $PID
		if [ $? = 0 ]; then
			echo "$NAME stopped"
			return 0
		else
			echo "$NAME could not be stopped"
			return 2
		fi
	else
		echo "$NAME is not running"
		return 1
	fi
}

do_reload() {
	if [ -f $PID_FILE ]; then
		PID=`cat $PID_FILE`
		kill -HUP $PID
		return $?
	fi
	return 2
}

case "$1" in
	start)
		[ "$VERBOSE" != no ] && log_daemon_msg "Starting $NAME" "$NAME"
		do_start
		case "$?" in
			0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
			2) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
		esac
		;;

	stop)
		[ "$VERBOSE" != no ] && log_daemon_msg "Stopping $NAME" "$NAME"
		do_stop
		case "$?" in
			0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
			2) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
		esac
		;;

	restart)
		log_daemon_msg "Restarting $NAME" "$NAME"
		do_stop
		case "$?" in
			0|1) do_start
			case "$?" in
				0) log_end_msg 0 ;;
				1) log_end_msg 1 ;; # Old process is still running
				*) log_end_msg 1 ;; # Failed to start
			esac
			;;
		*)
			# Failed to stop
			log_end_msg 1 ;;
		esac
		;;

	reload)
		log_daemon_msg "Reloading $DESC" "$NAME"
		do_reload
		case "$?" in
			0) log_end_msg 0 ;;
			*) log_end_msg 1 ;;
		esac
		;;

	*)
		echo $"Usage: $prog {start|stop|restart|reload}"
		RETVAL=2
esac

exit $RETVAL
