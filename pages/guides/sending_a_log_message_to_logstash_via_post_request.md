# Sending a log message to Logstash via POST request

## Linux:

```
curl -H "content-type: application/json" -XPUT 'https://logstash.yourserver.com:8080' -d '{ 
    "details": {
        "IP": "1.2.3.4:443"
    },
    "message": "Test message"
}'
```

## Powershell:

```
$LOGSTASH_MESSAGE = @{
    message="Test message"
    details = @{
        IP="1.2.3.4:443"
    }
}
$JSON_BODY = $LOGSTASH_MESSAGE | convertto-json

$response = Invoke-RestMethod -Uri "https://logstash.yourserver.com:8080" -Method Post -Body $JSON_BODY -ContentType "application/json"
```
