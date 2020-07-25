#Writing to and reading from Kinesis stream.

aws kinesis put-record  --stream-name nilesh --data '{ "name" : "Shaun", "age" : 31}' --partition-key public
Out
{
    "ShardId": "shardId-000000000000", 
    "SequenceNumber": "49609215945651732182096093941605502081856625961399746562"
}

aws kinesis describe-stream --stream-name nilesh

aws kinesis get-shard-iterator --shard-id shardId-000000000000 --shard-iterator-type TRIM_HORIZON --stream-name nilesh
Out
{
    "ShardIterator": "AAAAAAAAAAEttzgX4eCAgSy+/89hJ3F4Z6OCNeW0EVTqlgxN9sUqLPCZ5zL0cvTVNxLxwES+bOfa5la5pVpD0jTejnGTOBsGdn0Z9IeYq7BL9EE/m6FDvbUahzbn3KTGrDUTo4HWBnR9E4NtDXsGWFdOVq4/Q3Hg0dJE8en2IMC9r/u4jtlYpR4DJcRzVcZh6up4Rx7krqAJkV+YzoXyasqxpPTZt9cz"
}

aws kinesis get-records --shard-iterator "AAAAAAAAAAEttzgX4eCAgSy+/89hJ3F4Z6OCNeW0EVTqlgxN9sUqLPCZ5zL0cvTVNxLxwES+bOfa5la5pVpD0jTejnGTOBsGdn0Z9IeYq7BL9EE/m6FDvbUahzbn3KTGrDUTo4HWBnR9E4NtDXsGWFdOVq4/Q3Hg0dJE8en2IMC9r/u4jtlYpR4DJcRzVcZh6up4Rx7krqAJkV+YzoXyasqxpPTZt9cz"
Out
{
    "Records": [
        {
            "Data": "eyAibmFtZSIgOiAiU2hhdW4iLCAiYWdlIiA6IDMxfQ==", 
            "PartitionKey": "public", 
            "ApproximateArrivalTimestamp": 1595682821.55, 
            "SequenceNumber": "49609215945651732182096093941605502081856625961399746562"
        }
    ], 
    "NextShardIterator": "AAAAAAAAAAHsXrNDlM5PkyuPCK/dxusvtEMCYR7Ez4CaxItEJ6E1vC1/2rHnmXyCo9zEEyVzFqv7HbINLzMjxOBgNn07vPln3xVsejXE2JBBqfXEsCFjbL7VQAK3LPDiZHbx+lEughbpOn5XHNT5QGMWmTBordmKMGa3eYg7o4Acd38WogHGqQudF9DclWritUV8BQ7j+c/x7AemruiOBdAMcALJ1lXT", 
    "MillisBehindLatest": 0
}

echo "eyAibmFtZSIgOiAiU2hhdW4iLCAiYWdlIiA6IDMxfQ==" | base64 -d
Out
{ "name" : "Shaun", "age" : 31}

echo "eyAibmFtZSIgOiAiU2hhdW4iLCAiYWdlIiA6IDMxfQ==" | base64 -D --input -
Out
{ "name" : "Shaun", "age" : 31}

aws kinesis get-shard-iterator --shard-id shardId-000000000000 --shard-iterator-type AT_SEQUENCE_NUMBER --starting-sequence-number "49609215945651732182096093941605502081856625961399746562" --stream-name nilesh

aws kinesis get-shard-iterator --shard-id shardId-000000000000 --shard-iterator-type AFTER_SEQUENCE_NUMBER --starting-sequence-number "49609215945651732182096093941605502081856625961399746562" --stream-name nilesh

aws kinesis get-shard-iterator --shard-id shardId-000000000000 --shard-iterator-type LATEST --stream-name nilesh

aws kinesis get-shard-iterator --shard-id shardId-000000000000 --shard-iterator-type AT_TIMESTAMP --timestamp 1595682821.55 --stream-name nilesh

