# Setting up a Mongodb replicaset in docker-compose with Hidden Members

> Notes
> This is for instructional purposes, obviously in a production environment you would not run multiple mongodb databases on the same host as this will dramatically increase the load on the server as well as providing no redundancy in the event of the host going down.

## Installation

Create a docker-compose file as below, duplicate the service as many times as instances of mongodb you require (min 2)

```
version: '3'
services:
  mongodb1:
   image: 'mongo:latest'
   container_name: 'mongodb1'
   environment:
     - 'MONGO_DATA_DIR=/data/db'
   volumes:
     - './data/db1:/data/db'
   command: 'mongod --replSet "test" --bind_ip 0.0.0.0 --port 27017'
   restart: 'always'
  mongodb2:
   image: 'mongo:latest'
   container_name: 'mongodb2'
   environment:
     - 'MONGO_DATA_DIR=/data/db'
   volumes:
     - './data/db2:/data/db'
   command: 'mongod --replSet "test" --bind_ip 0.0.0.0 --port 27017'
   restart: 'always'
```

Now run the following to build your containers:

```
sudo docker-compose up -d
```

## Configuration
To create the replicaset, use the mongo command to access mongodb1 on port 27017 and use rs.initiate to create the replicaset (Adjusting the initiate command based on how many mongodb instances you require).

_NOTE: If you do not have mongo client installed on your Desktop, you can docker exec into the container to run the below._

```
mongo
rs.initiate( {
    _id : "test",
    members: [
        { _id: 0, host: "mongodb1:27017" },
        { _id: 1, host: "mongodb2:27017" },
        { _id: 2, host: "mongodb3:27017" },
    ]
})
```

You can confirm the replicaset status by running the below

```
mongo
rs.status()
```

## Adding a Replica set member
To add a new member to your cluster, run the below command from one of the existing database servers (Will be using mongodb4 for this example):.

```
mongo
rs.add( { host: "mongodb4:27017", priority: 0, votes: 0 } )
```

## Making a “Hidden” Replicaset member
To add a hidden member to your Mongodb cluster (Eg for backups) add the new member to the cluster and set it’s attribute to hidden as below (Will be using mongodb5 for this example):

```
mongo
rs.add( { host: "mongodb5:27017", priority: 0, votes: 0 } )
```

Now use rs.status() to get the “id” of the new replicaset member – Make a note of this _id:

```
mongo
rs.status()
```

Now edit the replicaset configuration to set this new member to “hidden”, replacing id with the value you noted before (Eg 4)

```
cfg = rs.conf()
cfg.members[4].priority = 0
cfg.members[4].hidden = true
rs.reconfig(cfg)
```
