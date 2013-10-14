#! /bin/sh

### BEGIN INIT INFO
# Provides:		read-ultra
# Required-Start:	$syslog
# Required-Stop:	$syslog
# Default-Start:	2 3 4 5
# Default-Stop:		0 1 6
# Short-Description:	Read Ultrasonic and switch on relay when triggered
### END INIT INFO

set -e

test -x /usr/local/bin/read_ultrasonic.py || exit 0

umask 022

. /lib/lsb/init-functions

export PATH="${PATH:+$PATH:}/usr/sbin:/sbin:/usr/local/bin"

case "$1" in
  start)
	log_daemon_msg "Starting GPIO ultrasonic reader" "read_ultrasonic.py" || true
	if start-stop-daemon --start --quiet --oknodo --pidfile /var/run/ultrasonic.pid --background --make-pidfile --exec /usr/local/bin/read_ultrasonic.py; then
	    log_end_msg 0 || true
	else
	    log_end_msg 1 || true
	fi
	;;
  stop)
	log_daemon_msg "Stopping Ultrasonic" "read-ultra" || true
	if start-stop-daemon --stop --quiet --retry TERM/30/KILL/5 --oknodo --pidfile /var/run/ultrasonic.pid; then
	    log_end_msg 0 || true
	else
	    log_end_msg 1 || true
	fi
	pkill -9 read_ultrasonic
	;;

  restart)
	log_daemon_msg "Restarting ultrasonic detector" "read_ultrasonic.py" || true
	start-stop-daemon --stop --quiet --oknodo --retry 30 --pidfile /var/run/ultrasonic.pid
	if start-stop-daemon --start --quiet --oknodo --pidfile /var/run/ultrasonic.pid --make-pidfile --background --exec /usr/local/bin/read_ultrasonic.py ; then
	    log_end_msg 0 || true
	else
	    log_end_msg 1 || true
	fi
	pkill -9 read_ultrasonic
	;;

  status)
	status_of_proc -p /var/run/ultrasonic.pid /usr/local/bin/read_ultrasonic.py read_ultrasonic.py && exit 0 || exit $?
	;;

  *)
	log_action_msg "Usage: /etc/init.d/read-ultra.sh {start|stop|restart|status}" || true
	exit 1
esac

exit 0

