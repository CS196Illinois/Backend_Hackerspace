# Databases
## CAP Theorem

Can't have all three at the same time in a distributed database system: <br>

Consistency (every read receives the most recent write or an error)<br>
Availability (every request receives a response, without guarantee that it contains the most recent version of the information)<br>
Partition tolerance (the system continues to operate despite arbitrary partitioning due to network failures)<br>

![CAP Theorem](http://i.stack.imgur.com/a9hMn.png)

In general, you cannot sacrifice partition tolerance. Therefore, you have to make tradeoffs between Consistency and Availability. <br>

How to get around CAP Theorem?

## ACID vs BASE

### ACID

Atomicity: Either the task (or all tasks) within a transaction are performed or none of them are. all -or-nothing <br>
Consistency: The transaction must meet all protocols or rules defined by the system at all times. The transaction does not violate those protocols and the database must remain in a consistent state at the beginning and end of a transaction; there are never any half-completed transactions.<br>
Isolation: No transaction has access to any other transaction that is in an intermediate or unfinished state. <br>
Durability: Once the transaction is complete, it will persist as complete and cannot be undone; it will survive system failure, power loss and other types of system breakdowns.<br>

### BASE

Basically Available: This constraint states that the system does guarantee the availability of the data as regards CAP Theorem; there will be a response to any request. But, that response could still be ‘failure’ to obtain the requested data or the data may be in an inconsistent or changing state, much like waiting for a check to clear in your bank account. <br>
Soft state: The state of the system could change over time, so even during times without input there may be changes going on due to ‘eventual consistency,’ thus the state of the system is always ‘soft.’<br>
Eventual consistency: The system will eventually become consistent once it stops receiving input. The data will propagate to everywhere it should sooner or later, but the system will continue to receive input and is not checking the consistency of every transaction before it moves onto the next one. Werner Vogel’s article “Eventually Consistent - Revisited” covers this topic is much greater detail.<br>


## SQL vs NoSQL

Relational vs Not

## Different Styles of Databases
1) Relational <br>
2) Key-Value <br>
3) Document-Oriented <br>
4) Column-Oriented <br>

## Embedded vs Deployed Databases

![RocksDB](http://image.slidesharecdn.com/rocksdbthehive3-131213153108-phpapp02/95/tech-talk-rocksdb-slides-by-dhruba-borthakur-haobo-xu-of-facebook-63-638.jpg?cb=1386949103)


## Database Implementations

Databases use internal implentations of algorithms to capitalize on runtime tradeoffs

![kd tree](http://groups.csail.mit.edu/graphics/classes/6.838/S98/meetings/m13/kd.gif)
