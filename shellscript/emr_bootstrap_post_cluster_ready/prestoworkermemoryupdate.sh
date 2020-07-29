#!/bin/bash
  
set -x -e

is_master=$(cat /emr/instance-controller/lib/info/instance.json | jq .isMaster)

if [ $is_master != "true" ]
then

CUSTOM_SCRIPT=$(cat <<EOF
#!/bin/bash
set -x -e
while [ "\$(sed '/localInstance {/{:1; /}/!{N; b1}; /nodeProvision/p}; d' /emr/instance-controller/lib/info/job-flow-state.txt | sed '/nodeProvisionCheckinRecord {/{:1; /}/!{N; b1}; /status/p}; d' | awk '/SUCCESSFUL/' | xargs)" != "status: SUCCESSFUL" ];
do
  sleep 1
done

##Script to update Presto worker memory

newmemoryvalue='-Xmx20622714968'
newpernodevalue='query.max-memory-per-node=10311357484B'
newtotalpernodevalue='query.max-total-memory-per-node=12373628981B'

sudo sed -e 's/^-Xmx*/#&/g' -i /etc/presto/conf/jvm.config
sudo sed -i "3i \$newmemoryvalue" /etc/presto/conf/jvm.config
sudo sed -e 's/^query.max-memory-per-node/#&/g' -e 's/^query.max-total-memory-per-node/#&/g' -i /etc/presto/conf/config.properties
sudo sed -i -e "7i \$newpernodevalue" -e "8i \$newtotalpernodevalue" /etc/presto/conf/config.properties
sudo stop presto-server
sudo start presto-server

##Script to update Presto worker memory

exit 0
EOF
)
echo "${CUSTOM_SCRIPT}" | tee -a /tmp/prestoworkermemoryupdate.sh
chmod u+x /tmp/prestoworkermemoryupdate.sh
/tmp/prestoworkermemoryupdate.sh > /tmp/prestoworkermemoryupdate.log 2>&1 &

fi

exit 0
