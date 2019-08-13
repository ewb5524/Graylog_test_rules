rule "check hostname (error in server.log if missing)
when
    to_string($message.hostname) == gw
then
...
end

rule "check hostname (content check only if field is present)
when
    has_field("hostname") AND to_string($message.hostname) == gw
then
...
end