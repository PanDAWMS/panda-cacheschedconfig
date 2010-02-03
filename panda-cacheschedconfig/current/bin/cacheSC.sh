#! /bin/sh
#
# Cache schedconfig data for sites
#
if [ -f /opt/cacheschedconfig/etc/sysconfig/cacheschedconfig-sysconfig ]; then
    source /opt/cacheschedconfig/etc/sysconfig/cacheschedconfig-sysconfig
fi

# Get panda server environment
source $SVRPATH/etc/sysconfig/panda_server-sysconfig

if [ ! -d $CACHEPATH ]; then
    mkdir -p $CACHEPATH
fi

# Clear out stale queues - that's anything older than a day for me
# but only do this if there are at least 100 fresh queues (protection against
# failure of this script so that at least we keep old data)
fresh=$(find $CACHEPATH -type f -mmin -60 | wc -l)
if [ $fresh -gt "100" ]; then
    find $CACHEPATH -type f -mtime +1 -print0 | xargs --null rm -f
else
    echo "Warning - no fresh queue data found"
fi

# Test if we have any running instances and kill them
pids=$(ps auxw | grep $CACHESCBIN/cacheSchedConfig.py | awk '{print $2}')
if [ -n "$pids" ]; then
    echo "Found old instances of script running - killing $pids..."
    kill $pids
fi

# Run script
python $CACHESCBIN/cacheSchedConfig.py --output=$CACHEPATH


