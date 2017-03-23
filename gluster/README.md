# gluster

Documenting a way of creating persistent storage for Docker containers with GlusterFS containers.
**Note:** This is a quick example.  Make sure you read up on security, changing the default password, and review the original Dockerfile.  I'll be experimenting with running this out on AWS soon and should be able to tighten it up further.

### Get the latest Gluster container:
[Get the latest container:](https://github.com/gluster/gluster-containers) 
```
docker pull gluster/gluster-centos
```

### Make the persistent data folders on each host:
``` 
sudo mkdir -p /gluster/logs /gluster/data /gluster/config /gluster/mnt
```

### Start a GlusterFS container on each host:
```
docker run -d \
   --name gluster \
   --privileged \
   --net=host \
   -v /gluster/data:/gluster \
   -v /gluster/logs:/var/log/glusterfs \
   -v /gluster/config:/var/lib/glusterd \
   -v /gluster/mnt:/gluster/mnt \
   gluster/gluster-centos
```

### Probe the hosts in the cluster:
For each container on each host you'll want to execute this to get them aware of the other peers.  If running out on AWS these steps could be orchestrated through the init system on the hosts so you don't have to log into each machine.
```
gluster peer probe 1.1.1.1
```

### Now create your volume and start it:
```
gluster volume create media replica 3 transport tcp 172.30.0.185:/gluster/data  172.30.0.186:/gluster/data 172.30.0.30:/
gluster volume start media
```

In this example I'm replicating across each of three servers but depending on your needs you could: distributed striped, distributed, replicated, distributed striped replicated, ... know what and why.

### Mount the volume
The docs made a big deal out of mounting the volume.  I suspect if you were doing anything other than replicating that would become very important.

You'll want to do this on each host, using its internal ip:
```
mount -t glusterfs 172.30.0.186:/media /gluster/mnt
```


From one of the hosts testing with a write statement to the volume:
```
echo "testing, 1,2,3..." >> /gluster/mnt/test.txt
```

And from another host you should be able to read/write to the same document.  One could then launch containers on any host with a mount to /gluster/mnt to store data.  Then it would have access to the data no matter which node it was launched on. 

